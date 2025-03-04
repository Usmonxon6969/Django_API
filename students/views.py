from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Student, Test, TestResult
from .serializers import StudentSerializer, TestSerializer, TestResultSerializer
from django.db.models import Avg, Max

class StudentListCreateView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TestListCreateView(ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestResultListCreateView(ListCreateAPIView):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer

class StudentTestResultsView(APIView):
    def get(self, request, student_id):
        results = TestResult.objects.filter(student_id=student_id)
        serializer = TestResultSerializer(results, many=True)
        return Response(serializer.data)

class TestResultsView(APIView):
    def get(self, request, test_id):
        results = TestResult.objects.filter(test_id=test_id)
        serializer = TestResultSerializer(results, many=True)
        return Response(serializer.data)

class TestAverageScoreView(APIView):
    def get(self, request, test_id):
        average = TestResult.objects.filter(test_id=test_id).aggregate(Avg('score'))
        return Response({'average_score': average['score__avg']})

class TestHighestScoreView(APIView):
    def get(self, request, test_id):
        highest = TestResult.objects.filter(test_id=test_id).aggregate(Max('score'))
        return Response({'highest_score': highest['score__max']})