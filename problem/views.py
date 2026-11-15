from django.shortcuts import render,get_object_or_404

# Create your views here.

from rest_framework.views import APIView
from problem.serializers import QuestionSerializers
from exam.models import Assesment
from rest_framework import permissions,authentication
from rest_framework.response import Response
from problem.models import Question
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class QuestionCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,pk=None):

        Assesment_object=get_object_or_404(Assesment,id=pk)

        form_data=request.data

        serializer_instance=QuestionSerializers(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(assesment=Assesment_object)

            return Response(serializer_instance.data)
        else:

            return Response(serializer_instance.errors)

class QuestionRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    serializer_class=QuestionSerializers
    queryset=Question.objects.all()

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAdminUser] 
           
