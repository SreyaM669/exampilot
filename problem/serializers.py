
from rest_framework import serializers

from problem.models import Question

class QuestionSerializers(serializers.ModelSerializer):

    class Meta:

        model=Question

        fields="__all__"

        read_only_fields=["id","assesment","created_at"]