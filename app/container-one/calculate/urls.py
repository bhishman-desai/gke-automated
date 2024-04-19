from django.urls import path
from calculate.views import CalculateView

urlpatterns = [
    path('calculate', CalculateView.as_view()),
]
