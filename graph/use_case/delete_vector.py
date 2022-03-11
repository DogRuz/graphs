from graph.error import GraphNotFound
from graph.models import Graphs


class DeleteVector:
    def __init__(self, graph_id: int):
        self.graph_id = graph_id

    def set_graph_id(self, graph_id: int) -> None:
        self.graph_id = graph_id

    def get_graph_id(self) -> int:
        return self.graph_id

    def execute(self) -> int:
        try:
            Graphs.objects.get(id=self.graph_id).delete()
        except Graphs.DoesNotExist:
            raise GraphNotFound()
        return self.graph_id
