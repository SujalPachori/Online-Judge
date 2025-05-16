from django.shortcuts import render,redirect
from problems.models import Problem
from django.template import loader
from django.http import HttpResponse
# from home.forms import VoteForm
from django.contrib.auth.decorators import login_required# Create your views here.

@ login_required
def all_problems(request):
    all_problems = Problem.objects.all()

    context = {
        'all_problems':all_problems,
    }
    template = loader.get_template('all_problems.html')

    return HttpResponse(template.render(context,request))

@login_required
def problem(request,problem_id):
    req_problem = Problem.objects.get(id=problem_id)

    context = {
        'req_problem':req_problem,
    }

    template = loader.get_template('problem.html')

    return HttpResponse(template.render(context,request))