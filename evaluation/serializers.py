
from rest_framework import serializers
from evaluation.models import  Submission
from evaluation.models import Answer

from django.db.models import Sum

class SubmissionSerializer(serializers.ModelSerializer):

    answers=serializers.SerializerMethodField(read_only=True)
    total_score=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model=Submission
        fields="__all__"
        read_only_fields=[fields]


    def get_answers(self,obj):
    
        answer_objects=Answer.objects.filter(submission=obj)
    
        serializer_intance= AnswerSerializer(answer_objects,many=True)
    
        return serializer_intance.data


    def get_total_score(self,obj):

        return Answer.objects.filter(submission=obj).values("marks_awarded").aggregate(total=Sum("marks_awarded")).get("total")
        


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model=Answer
        fields="__all__"
        read_only_fields=["id","submission"]




    