from django.urls import path

from .views import (
    raise_problem,
    problem_success,
    problem_detail,
    take_problem
)


urlpatterns = [

    path(
        'raise-problem/',
        raise_problem,
        name='raise_problem'
    ),

    path(
        'problem-success/',
        problem_success,
        name='problem_success'
    ),

    path(
        'problem/<int:problem_id>/',
        problem_detail,
        name='problem_detail'
    ),

    path(
        'take-problem/<int:assignment_id>/',
        take_problem,
        name='take_problem'
    ),

]