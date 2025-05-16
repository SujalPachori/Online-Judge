from django.urls import path
from problems.views import all_problems ,problem

urlpatterns = [
    path("", all_problems, name="all-problems"),
    path("problem/<int:problem_id>/", problem, name="problem"),

]