from graph.models import AdjacencyMatrix


class GetAncestors:
    def __init__(self, graph_id: int):
        self.graph_id = graph_id

    def set_graph_id(self, graph_id: int) -> None:
        self.graph_id = graph_id

    def get_graph_id(self) -> int:
        return self.graph_id

    def execute(self):
        data = AdjacencyMatrix.get_all_ancestors(graph_id=self.graph_id)
        return data
