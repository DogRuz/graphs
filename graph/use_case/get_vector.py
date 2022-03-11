from graph.error import GraphNotFound, VectorsNotFound
from graph.models import Vectors


class GetVector:
    def __init__(self, graph_id: int):
        self.graph_id = graph_id

    def set_graph_id(self, graph_id: int) -> None:
        self.graph_id = graph_id

    def get_graph_id(self) -> int:
        return self.graph_id

    def execute(self):
        vector = []
        values = Vectors.objects.filter(graph=self.graph_id).order_by('index')
        if len(values) == 0:
            raise VectorsNotFound()
        for value in values:
            vector.append(value.value)
        return vector
