from rest_framework import serializers

from layer_study.models import Number

class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = "__all__"

    # def create(self, validated_data):
    #     print(validated_data)
    #     if validated_data.get("number") < 0:
    #         validated_data["text"] = "N"
    #     elif validated_data.get("number") == 0:
    #         validated_data["text"] = "Z"
    #     else:
    #         validated_data["text"] = "P"
    #     return super().create(validated_data)