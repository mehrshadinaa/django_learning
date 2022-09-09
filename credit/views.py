from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from json import JSONEncoder
from credit.models import *
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def submit_expense(request):
    """ submit an expense """

    print(request.POST)
    this_text = request.POST['text']
    this_token = request.POST['token']
    this_amount = request.POST['amount']
    this_user = User.objects.filter(token__token = this_token).get()
    date = datetime.now()

    Expense.objects.create(
        user = this_user,
        amount = this_amount,
        date = date,
        text = this_text
    )

    #return HttpResponse("Hello, world. You're at the polls index.")
    return JsonResponse({
        'satus': 'ok'
    }, encoder=JSONEncoder)


@csrf_exempt
def submit_income(request):
    """ submit an income """

    print(request.POST)
    this_text = request.POST['text']
    this_token = request.POST['token']
    this_amount = request.POST['amount']
    this_user = User.objects.filter(token__token = this_token).get()
    date = datetime.now()

    Income.objects.create(
        user = this_user,
        amount = this_amount,
        date = date,
        text = this_text
    )

    #return HttpResponse("Hello, world. You're at the polls index.")
    return JsonResponse({
        'satus': 'ok'
    }, encoder=JSONEncoder)
