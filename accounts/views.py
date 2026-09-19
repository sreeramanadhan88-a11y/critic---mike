from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from problems.models import Problem, ProblemAssignment


def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {
        'form': form
    })


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('admin_dashboard')

            if user.role == 'department_staff':
                return redirect('department_dashboard')

            if Problem.objects.filter(user=user).exists():
                return redirect('my_problems')

            return redirect('raise_problem')

        else:
            return render(request, 'accounts/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'accounts/login.html')


@login_required(login_url='/login/')
def admin_dashboard(request):

    if not request.user.is_superuser:
        return redirect('login')

    problems = Problem.objects.all()

    return render(request, 'accounts/admin_dashboard.html', {
        'problems': problems
    })


@login_required(login_url='/login/')
def my_problems(request):

    problems = Problem.objects.filter(
        user=request.user
    )

    return render(
        request,
        'accounts/my_problems.html',
        {
            'problems': problems
        }
    )


@login_required(login_url='/login/')
def department_dashboard(request):

    if request.user.role != 'department_staff':
        return redirect('login')

    assignments = ProblemAssignment.objects.all()

    return render(
        request,
        'accounts/department_dashboard.html',
        {
            'assignments': assignments
        }
    )