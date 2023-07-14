
# arrays that collect the data on their definition
class Data:
    def __init__(self):
        self.types = []
        self.parameters = []
        self.connections = []
        self.graph_classes = []
        self.graph_inclusions = []
        self.equivalencies = []
        self.sources = []

    def get(self, id):
        for entry in self.all_values():
            if hasattr('id', entry) and entry.id == id:
                return entry
        return None

    def all_values(self):
        for attr in [a for a in dir(self) if not a.startswith('__')
                     and not callable(getattr(self, a))]:
            for entry in attr:
                yield entry


data = Data()

################################################################################

class CustomType:
    def __init__(self, id, name, description):
        data.types.append(self)
        self.id = id
        self.name = name
        self.description = description

parameter_type = CustomType(
        id = "!TrvG50",
        name = "parameter",
        description = "Instance of this type represents a graph Parameter in the context of Parameterized complexity. They are associated with meta-data, e.g., an approximate (and highly oppinionated) importance, and upper_bounds that says whether for this parameter $k$ and any graph there is a computable function $f$ such that another parameter is upper bound by $f(k)$."
        )

bound_type = CustomType(
        id = "!jgWdIT",
        name = "upper bounds",
        description = "Connection between two parameters that describes that if the first one is K then the second one is at most f(K) where f is a computable function. Alternatively, one can think about this relation as that the second one is potentially smaller for a wider class of graphs"
        )

graph_type = CustomType(
        id = "!JpeEf9",
        name = "graph",
        description = "A graph class that is (preferrably) linked to ISGCI (https://www.graphclasses.org/). Classes that do not have impact on the parameter picture ought to be omitted."
        )

################################################################################

class Parameter:
    def __init__(self, id, name=None, notes=None):
        assert(isinstance(name, str))
        assert(isinstance(notes, list))
        data.parameters.append(self)
        self.type = parameter_type
        self.id = id
        self.name = name
        if notes is None:
            notes = []
        self.notes = notes
        self.below = []
        self.above = []
        self.bounded_for = []
        self.unbounded_for = []
        self.visible = True


def distanceTo(graph_class) -> Parameter:
    dist_id = graph_class.id + '_dist'
    for par in data.parameters:
        if par.id == dist_id:
            return par
    name = graph_class.name
    def_note = Note(id=dist_id + '_def', text=f'Number of vertices that need to be removed so that the rest belongs to [{graph_class.name}](#{graph_class.id}) graph class.')
    return Parameter(dist_id, f'distance to {name}', [def_note])


MIN_NONE = 0
LINEAR = 1
POLYNOMIAL = 2
EXPONENTIAL = 3
MAX_NONE = 100

class UpperBound:
    def __init__(self, id, fr, to, notes):
        assert(isinstance(fr, Parameter))
        assert(isinstance(to, Parameter))
        data.connections.append(self)
        self.type = bound_type
        self.id = id
        self.fr = fr
        self.to = to
        self.notes = notes
        self.known_strict = False
        self.known_optimal_tail = False
        self.known_optimal_head = False
        self.upper_bound = MAX_NONE
        self.lower_bound = MIN_NONE
        for note in notes:
            if isinstance(note, Note) or isinstance(note, Cite):
                self.upper_bound = min(self.upper_bound, note.upper_bound)
                self.lower_bound = max(self.lower_bound, note.lower_bound)

class Equivalent:
    def __init__(self, id, persistant_par, merged_par, notes):
        data.equivalencies.append(self)
        self.id = id
        self.persist = persistant_par
        self.removed = merged_par
        self.notes = notes

class Abbreviation:
    def __init__(self, abbreviation):
        self.abbreviation = abbreviation

class AKA:
    def __init__(self, name, notes=None):
        self.name = name
        if notes is None:
            notes = []
        self.notes = notes

class ISGCI:
    def __init__(self, code):
        self.parent = None
        self.code = code

class Topic:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

class Note:
    def __init__(self, id, text, upper_bound=MAX_NONE, lower_bound=MIN_NONE):
        self.id = id
        self.text = text
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

class GraphClass:
    def __init__(self, id, name, notes):
        data.graph_classes.append(self)
        self.id = id
        self.name = name
        self.notes = notes
        self.contained_in = []
        self.not_contained_in = []
        self.subclasses = []
        self.superclasses = []

def connected(name, graph_class, notes) -> GraphClass:
    conn_id = graph_class.id + '_connected'
    res = data.get(conn_id)
    if res is not None:
        return res
    res = GraphClass(conn_id, name, notes)
    Inclusion(id=f'{graph_class.id}_con_rel',
              superclass=graph_class,
              subclass=res,
              notes=[])
    for sub in graph_class.subclasses:
        subentry = data.get(sub.id)
        if subentry is not None:
            Inclusion(id=f'{res.id}_{subentry.id}',
                      superclass=res,
                      subclass=subentry,
                      notes=[])
    for sup in graph_class.superclasses:
        supentry = data.get(sup.id)
        if supentry is not None:
            Inclusion(id=f'{supentry.id}_{res.id}',
                      superclass=supentry,
                      subclass=res,
                      notes=[])
    return res

class Inclusion:
    def __init__(self, id, superclass, subclass, notes):
        data.graph_inclusions.append(self)
        self.id = id
        self.superclass = superclass
        self.subclass = subclass
        self.notes = notes
        self.subclass.superclasses.append(self.superclass)
        self.superclass.subclasses.append(self.subclass)

class HasBounded:
    def __init__(self, id, graph_class, parameter, notes):
        assert isinstance(graph_class, GraphClass)
        assert isinstance(parameter, Parameter)
        self.id = id
        self.graph_class = graph_class
        self.parameter = parameter
        self.notes = notes
        self.graph_class.contained_in.append(parameter)

class HasUnbounded:
    def __init__(self, id, graph_class, parameter, notes):
        assert isinstance(graph_class, GraphClass)
        assert isinstance(parameter, Parameter)
        self.id = id
        self.graph_class = graph_class
        self.parameter = parameter
        self.notes = notes
        self.graph_class.not_contained_in.append(parameter)

class Source:
    def __init__(self, id, sourcekey, args):
        data.sources.append(self)
        self.id = id
        self.sourcekey = sourcekey
        self.args = args

class Cite:
    def __init__(self, id, **kwargs):
        self.id = id
        assert ('url' in kwargs) or ('source' in kwargs)
        self.kwargs = kwargs
        self.upper_bound = MAX_NONE
        if 'upper_bound' in kwargs:
            self.upper_bound = kwargs['upper_bound']
        self.lower_bound = MIN_NONE
        if 'lower_bound' in kwargs:
            self.lower_bound = kwargs['lower_bound']
