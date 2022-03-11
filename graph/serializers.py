from rest_framework import serializers


class GraphSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=False, default=None)
    vector = serializers.ListField(child=serializers.FloatField())


class ParentVectorSerializer(serializers.Serializer):
    child_vector = serializers.IntegerField()
    parent_vectors = serializers.ListField(child=serializers.IntegerField())
