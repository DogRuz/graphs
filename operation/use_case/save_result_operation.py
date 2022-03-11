from operation.models import ResultGraph


class SaveResultOperation:
    def __init__(self, graph_id: int, operation_id: int):
        self.graph_id = graph_id
        self.operation_id = operation_id

    def set_graph_id(self, graph_id: int) -> None:
        self.graph_id = graph_id

    def get_graph_id(self) -> int:
        return self.graph_id

    def set_operation_id(self, operation_id: int) -> None:
        self.operation_id = operation_id

    def get_operation_id(self) -> int:
        return self.operation_id

    def execute(self):
        obj = ResultGraph.objects.get(graph_id=self.graph_id)
        obj.operation_id = self.operation_id
        obj.save()
        data = {'operation_id': self.operation_id, 'id': obj.id, 'name_graph': obj.graph_id}
        return data
