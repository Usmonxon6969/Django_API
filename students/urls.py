from django.urls import path
from .views import (
    StudentListCreateView, StudentRetrieveUpdateDestroyView,
    TestListCreateView, TestRetrieveUpdateDestroyView,
    TestResultListCreateView, StudentTestResultsView,
    TestResultsView, TestAverageScoreView, TestHighestScoreView
)

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-detail'),
    path('tests/', TestListCreateView.as_view(), name='test-list-create'),
    path('tests/<int:pk>/', TestRetrieveUpdateDestroyView.as_view(), name='test-detail'),
    path('results/', TestResultListCreateView.as_view(), name='testresult-list-create'),
    path('results/student/<int:student_id>/', StudentTestResultsView.as_view(), name='student-test-results'),
    path('results/test/<int:test_id>/', TestResultsView.as_view(), name='test-results'),
    path('results/test/<int:test_id>/average/', TestAverageScoreView.as_view(), name='test-average-score'),
    path('results/test/<int:test_id>/highest/', TestHighestScoreView.as_view(), name='test-highest-score'),
]