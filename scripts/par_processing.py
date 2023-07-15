################################################################################
## Processing ##################################################################
################################################################################

import par_types
from par_types import distanceTo, UpperBound, Note, HasBounded, GraphClass


def postprocess(data):
    generate_distances(data)
    propagate_parent_to_notes(data)
    add_equivalence_note(data)
    set_edge_properties_to_nodes(data)
    propagate_graph_classes(data)
    derive_connection_properties(data)
    return data


def propagate_parent_to_notes(data):
    #  generalize to all data objects
    for graph_class in data.graph_classes:
        for note in graph_class.notes:
            if hasattr(note, 'parent'):
                note.parent = graph_class
    for parameter in data.parameters:
        for note in parameter.notes:
            if hasattr(note, 'parent'):
                note.parent = parameter


def set_edge_properties_to_nodes(data):
    for connection in data.connections:
        connection.fr.below.append(connection.to)
        connection.to.above.append(connection.fr)
    for equivalency in data.equivalencies:
        equivalency.persist.below.append(equivalency.removed)
        equivalency.persist.above.append(equivalency.removed)
        equivalency.removed.below.append(equivalency.persist)
        equivalency.removed.above.append(equivalency.persist)


def generate_distances(data):
    for graph_class in data.graph_classes:
        par = distanceTo(graph_class)
        HasBounded(f"{graph_class.id}_itself", graph_class, par, [
            Note(id=f"{graph_class.id}_itself_note", text="Distance to a graph class contains itself even when no vertices were removed.")
            ])
    inclusion_note = Note(id="!6nm4uH", text="graph inclusion", upper_bound=par_types.LINEAR)
    for graph_inclusion in data.graph_inclusions:
        upperpar = distanceTo(graph_inclusion.subclass)
        lowerpar = distanceTo(graph_inclusion.superclass)
        UpperBound(id=f"{graph_inclusion.id}_par", fr=upperpar, to=lowerpar, notes=[inclusion_note])


def add_equivalence_note(data):
    for eq in data.equivalencies:
        eq.persist.notes.append(Note(id=f"{eq.id}_note", text=f"is equivalent to [{eq.removed.name}](#{eq.removed.id})"))
        eq.removed.notes.append(Note(id=f"{eq.id}_note", text=f"is equivalent to [{eq.persist.name}](#{eq.persist.id}) (see more info there)"))
        eq.persist.equivalent_to.append(eq.removed)
        eq.removed.equivalent_to.append(eq.persist)


def down(entry):
    (graph_class, parameter) = entry
    for nextpar in parameter.below:
        yield (graph_class, nextpar)
    for nextclass in graph_class.subclasses:
        yield (nextclass, parameter)


def up(entry):
    (graph_class, parameter) = entry
    for nextpar in parameter.above:
        yield (graph_class, nextpar)
    for nextclass in graph_class.superclasses:
        yield (nextclass, parameter)


def propagate_through_pars(seed, next_function):
    open = seed
    visited = set()
    while len(open) != 0:
        entry = open.pop()
        if entry not in visited and entry not in open:
            visited.add(entry)
            open += next_function(entry)
    return list(visited)


def propagate_graph_classes(data):
    down_seed = []
    for graph_class in data.graph_classes:
        for parameter in graph_class.contained_in:
            down_seed.append((graph_class, parameter))
    res = propagate_through_pars(down_seed, down)
    for par in data.parameters:
        par.bounded_for = []
    for gc in data.graph_classes:
        gc.has_bounded = []
    for (gc, par) in res:
        par.bounded_for.append(gc)
        gc.has_bounded.append(par)
    up_seed = []
    for graph_class in data.graph_classes:
        for parameter in graph_class.not_contained_in:
            up_seed.append((graph_class, parameter))
    res = propagate_through_pars(up_seed, up)
    for par in data.parameters:
        par.unbounded_for = []
    for gc in data.graph_classes:
        gc.has_unbounded = []
    for (gc, par) in res:
        par.unbounded_for.append(gc)
        gc.has_unbounded.append(par)


def nonisomorphism_witnesses(upper, lower) -> [GraphClass]:
    return list(set(upper.unbounded_for).intersection(set(lower.bounded_for)))


def derive_connection_properties(data):
    for connection in data.connections:
        witnesses = nonisomorphism_witnesses(connection.fr, connection.to)
        if len(witnesses) != 0 and not connection.known_strict:
            connection.known_strict = True
            graph_class = witnesses[0]
            strict_note = Note(connection.id + '_strict', f'This inclusion is proper because [{graph_class.name}](#{graph_class.id}) graph class has bounded [{connection.to.name}](../{connection.to.id}) but unbounded [{connection.fr.name}](../{connection.fr.id})')
            connection.notes.append(strict_note)
        can_move_head_up = False
        for anc in connection.to.above:
            if anc == connection.fr:
                continue
            anc_witnesses = nonisomorphism_witnesses(connection.fr, anc)
            if len(anc_witnesses) == 0:
                can_move_head_up = True
                break
        if not can_move_head_up:
            connection.known_optimal_head = True
        can_move_tail_down = False
        for des in connection.fr.below:
            if des == connection.to:
                continue
            des_witnesses = nonisomorphism_witnesses(des, connection.to)
            if len(des_witnesses) == 0:
                can_move_tail_down = True
                break
        if not can_move_tail_down:
            connection.known_optimal_tail = True
