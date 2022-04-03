from ast import operator
from unittest import result
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from random import randrange
# Create your views here.

def calculator(reqeust):
    # return HttpResponse('계산기 기능 구현입니다.')

    # 데이터 확인
    num1 = reqeust.GET.get('num1')
    num2 = reqeust.GET.get('num2')
    operators = reqeust.GET.get('operators')
    # 계산
    if(operators == '+'):
        result = int(num1) + int(num2)
    elif(operator == '-'):
        result = int(num1) - int(num2)
    elif(operator == '*'):
        result = int(num1) * int(num2)
    elif(operator == '/'):
        result = int(num1) / int(num2)
    else:
        result = 0
    # 응답
    return render(reqeust, 'calculator.html', {'result': result}) 

def lotto(reqeust):
    return render( reqeust, 'lotto.html')

def lottoResult(reqeust):
    # 데이터 확인
    coin =reqeust.GET.get('coin')
    result = []
    #번호 생성
    for idx in range(int(coin)):
        tem = []
        for idx in range(5):
            tem.append(randrange(100))
        result.append(tem)

    #응답
    return render(reqeust, 'lottoResult.html', {'coin' : coin, 'result' : result})
    # return render(reqeust, 'lottoResult.html')