from operation.models import ResultGraph


class OperationVector:
    def __init__(self, graph_id: int):
        self.graph_id = graph_id

    def set_operation_id(self, graph_id: int) -> None:
        self.graph_id = graph_id

    def get_operation_id(self) -> int:
        return self.graph_id

    def execute(self):
        data = ResultGraph.objects.filter(graph_id=self.graph_id)
        return data