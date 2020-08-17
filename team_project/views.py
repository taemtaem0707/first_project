from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.db.models import Count

# 폼, 모델
from .forms import checkForm
from .models import Check
# 통계 import
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pylab as plt
import csv
from pandas import DataFrame
import os
import time


# Create your views here.
def main(request):
    context = {
    }
    return render(request, 'team_project/main.html', context)


def introduce(request):
    context = {
    }
    return render(request, 'team_project/introduce.html', context)


def crawling(request):
    context = {
    }
    return render(request, 'team_project/crawling.html', context)


def processing(request):
    context = {
    }
    return render(request, 'team_project/processing.html', context)


def visual(request):
    context = {
    }
    return render(request, 'team_project/visual.html', context)


def result(request):

    context = {
    }
    return render(request, 'team_project/result.html', context)


def extension(request):
    context = {
    }
    return render(request, 'team_project/extension.html', context)

def function(request):
    check = Check.objects.order_by('-created_at')[:10] # 모델연결, 생성일자 역순 10개

    my_team = list(Check.objects.values('team1').annotate(count=Count('team1')).order_by('-count')[:5]) # 모델 내 team1을 group by 역순으로 5개
    other_team = list(Check.objects.values('team2').annotate(count=Count('team2')).order_by('-count')[:5])
    team = [my_team, other_team]

    now = time.localtime() # 시간
    now_time = "%04d/%02d/%02d" % (now.tm_year, now.tm_mon, now.tm_mday)

    from team_project import crawling
    crawling_data = crawling.ranking()

    if request.method == 'POST': # 만약 post로 넘어온다면
        form = checkForm(request.POST) # checkForm 입력 값 연결
        if form.is_valid():
            team1=form.data['team1']
            team2=form.data['team2']
            if team1 == team2:
                pass
            else:
                from team_project import function # function.py import
                function.draw(team1, team2) # 사용자가 선택한 두 팀 시각화
                obj = Check(team1=team1, team2=team2)
                obj.save() # 모델 저장
                my_team = list(Check.objects.values('team1').annotate(count=Count('team1')).order_by('-count')[
                               :5])
                other_team = list(Check.objects.values('team2').annotate(count=Count('team2')).order_by('-count')[:5])
                team = [my_team, other_team]
                context = {
                    'form': form,
                    'check': check,
                    'my_team': my_team,
                    'other_team': other_team,
                    'now_time':now_time,
                    'crawling_data' :crawling_data,
                    'team':team,
                }

                return render(request, 'team_project/function.html', context)
        else:
            return HttpResponseRedirect('/function/')
    form = checkForm()
    context = {
        'form': form,
        'check': check,
        'my_team': my_team,
        'other_team': other_team,
        'now_time': now_time,
        'crawling_data': crawling_data,
        'team': team,
    }
    return render(request, 'team_project/function.html', context)

