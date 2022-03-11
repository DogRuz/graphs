from operation.models import Operations


class GetAllOperations:

    @staticmethod
    def execute():
        operations = Operations.objects.all()
        return operations
