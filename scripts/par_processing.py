################################################################################
## Processing ##################################################################
################################################################################

def postprocess(data):
    propagate_graph_classes(data)
    check_strict_connections(data)
    return data

down = lambda x: x.below
up = lambda x: x.above

def propagate_through_pars(parameter, seed_parameters, next_function):
    open = seed_parameters
    visited = set()
    while len(open) != 0:
        entry = open.pop()
        if entry not in visited and entry not in open:
            visited.add(entry)
            open += next_function(entry)
    return list(visited)

def propagate_graph_classes(data):
    for graph_class in data.graph_classes:
        for down_entry in propagate_through_pars(data.parameters, graph_class.contained_in, down):
            down_entry.unbounded_for.append(graph_class)
        for up_entry in propagate_through_pars(data.parameters, graph_class.not_contained_in, up):
            up_entry.bounded_for.append(graph_class)


def check_strict_connections(data):
    for connection in data.connections:
        intersection = set(connection.fr.bounded_for).intersection(set(connection.to.unbounded_for))
        if len(intersection) != 0:
            connection.known_strict = True
