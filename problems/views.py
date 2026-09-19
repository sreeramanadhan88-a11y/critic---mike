from django.shortcuts import render, redirect,get_object_or_404
from .forms import ProblemForm, ProblemAssignmentForm
from .models import Problem,ProblemAssignment
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')



def raise_problem(request):

    if request.user.role != 'civilian':
        return redirect('login')

    if request.method == 'POST':
        form = ProblemForm(request.POST, request.FILES)

        if form.is_valid():
            problem = form.save(commit=False)
            problem.user = request.user
            problem.save()

            return redirect('problem_success')

    else:
        form = ProblemForm()

    return render(request, 'problems/raise_problem.html', {
        'form': form
    })

def problem_success(request):
    return render(request,'problems/problem_success.html')

def problem_detail(request, problem_id):

    problem = get_object_or_404(
        Problem,
        id=problem_id
    )

    if request.method == 'POST':

        form = ProblemAssignmentForm(request.POST)

        if form.is_valid():

            assignment = form.save(commit=False)

            assignment.problem = problem
            assignment.assigned_by = request.user

            assignment.save()

            problem.status = 'assigned'
            problem.save()

            return redirect(
                'problem_detail',
                problem_id=problem.id
            )

    else:
        form = ProblemAssignmentForm()

    return render(
        request,
        'problems/problem_detail.html',
        {
            'problem': problem,
            'form': form
        }
    )
@login_required(login_url='/login/')
def take_problem(request, assignment_id):

    if request.user.role != 'department_staff':
        return redirect('login')

    assignment = get_object_or_404(
        ProblemAssignment,
        id=assignment_id
    )

    problem = assignment.problem

    problem.status = 'problem_initiated'
    problem.save()

    return redirect('department_dashboard')