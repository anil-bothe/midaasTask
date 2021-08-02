from rest_framework import serializers
from app.models import PrimeNo

class PrimeNoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimeNo
        fields = "__all__"

class GenPrimeNoSerializer(serializers.Serializer):
    algo_id = serializers.IntegerField()
    start_no = serializers.IntegerField()
    end_no = serializers.IntegerField()
    