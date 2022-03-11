from rest_framework import serializers


class OperationsSerializer(serializers.Serializer):
    operation = serializers.IntegerField()
    vectors = serializers.ListField(child=serializers.IntegerField())


class ResultSerializer(serializers.Serializer):
    graph_id = serializers.IntegerField()
    operation_id = serializers.IntegerField()