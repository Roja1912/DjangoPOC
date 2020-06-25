from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import UserRequesting

class RequestSerializer(ModelSerializer):

    class Meta:
        model = UserRequesting
        fields = [
            'request_id',
            'accept',
        ]

    def create(self, validated_data):
        """
        Insert ingestion data to database
        :param validated_data:
        :return:
        """
        instance = UserRequesting.objects.create(**validated_data)
        return instance

    def get_data(self):
        data = UserRequesting.objects.all()
        return data
#
# class RequestSerializerListSerializer(serializers.ModelSerializer):
#     """
#     IngestionInventoryListSerializer class define serializer to list inventory
#     """
#     ingestion_inventory = RequestSerializer(many=True, queryset=RequestUser.objects.all())
#
#     class Meta:
#         model = RequestUser
#         fields = [
#             'ingestion_inventory',
#         ]