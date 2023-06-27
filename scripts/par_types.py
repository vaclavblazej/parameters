
# arrays that collect the data on their definition
class Data:
    def __init__(self):
        self.types = []
        self.parameters = []
        self.connections = []
        self.graph_classes = []

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
    def __init__(self, id, name, hue, notes, abbreviation=None, isgci=None, topics=None):
        data.parameters.append(self)
        self.type = parameter_type
        self.id = id
        self.name = name
        self.abbreviation = abbreviation
        self.hue = hue
        self.notes = notes
        self.isgci = isgci
        self.topics = []
        if topics is not None:
            self.topics = topics
        self.below = []
        self.above = []
        self.bounded_for = []
        self.unbounded_for = []

class DistEntry:
    def __init__(self, id, graph, hue, notes, abbreviation=None, isgci=None):
        data.parameters.append(self)
        self.type = parameter_type
        self.id = id
        self.name = f"distance to {graph.name}"
        self.abbreviation = abbreviation
        self.hue = hue
        self.notes = notes
        self.isgci = isgci
        self.below = []
        self.above = []
        self.bounded_for = []
        self.unbounded_for = []

class UpperBound:
    def __init__(self, id, fr, to, notes):
        data.connections.append(self)
        self.type = bound_type
        self.id = id
        self.fr = fr
        self.to = to
        self.notes = notes
        self.known_strict = False
        self.fr.below.append(self.to)
        self.to.above.append(self.fr)

class Topic:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

class Note:
    def __init__(self, id, url, text):
        self.id = id
        self.url = url
        self.text = text

class GraphClass:
    def __init__(self, id, name, isgci):
        data.graph_classes.append(self)
        self.id = id
        self.name = name
        self.isgci = isgci
        self.contained_in = []
        self.not_contained_in = []

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
