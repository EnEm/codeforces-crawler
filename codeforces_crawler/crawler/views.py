from django.shortcuts import render, redirect
from codeforces_crawler.forms import UserIDForm, CompareIDForm
from codeforces_crawler.forms import CompareIDFormset
from .main import crawler_1, crawler_2, crawler_3
import json
import urllib
from collections import Counter
import numpy as np

# Create your views here.

def login(request):
    if request.method == "POST":
        form = UserIDForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            username, rank, dp = crawler_1([str(user)])
            user_rating = crawler_2(str(user))
            dicti = {'user_rating': user_rating, 'username':username[0], 'dp': dp[0] ,'legendary_grandmaster': False, 'international_grandmaster': False, 'grandmaster': False, 'international_master': False, 'master': False, 'candidate_master': False, 'expert': False,'specialist': False, 'pupil': False, 'newbie':False}
            dicti[rank[0].replace(' ','_')] = True
            virtual, contest, unofficial, practice = crawler_3(str(user))
            temp_a = []
            for i in range(len(virtual)):
                temp1 = {}
                temp1['label'] = i
                temp1['y'] = virtual[i]
                temp_a.append(temp1)
            dicti['virtual'] = temp_a
            #print(dicti['virtual'][1500])
            temp_b = []
            for i in range(len(contest)):
                temp1 = {}
                temp1['x'] = i
                temp1['y'] = contest[i]
                temp_b.append(temp1)
            dicti['contest'] = temp_b
            #print(dicti['contest'][1500])
            #temp.clear()
            temp_c = []
            for i in range(len(unofficial)):
                temp1 = {}
                temp1['x'] = i
                temp1['y'] = unofficial[i]
                temp_c.append(temp1)
            dicti['unofficial'] = temp_c
            #print(dicti['unofficial'][1500])
            #temp.clear()
            temp_d = []
            for i in range(len(practice)):
                temp1 = {}
                temp1['x'] = i
                temp1['y'] = practice[i]
                temp_d.append(temp1)
            dicti['practice'] = temp_d
            #print(dicti['practice'][1500])
            #print(dicti)
            return render(request, 'crawler/index.html', context = dicti)
    form = UserIDForm()
    return render(request,'crawler/login.html', {'form':form})

def index(request):
    return render(request, 'crawler/index.html')

def home(request):
    return render(request, 'crawler/home.html')

def compare(request):
    # if request.method == "POST":
    #     form = CompareIDForm(request.POST)
    #     if form.is_valid():
    #         users = []
    #         user1 = form.cleaned_data['user1']
    #         user2 = form.cleaned_data['user2']
    #         username, rank, dp = crawler_1([str(user1), str(user2)])
    #         user_rating = crawler_2(str(user1))
    #         dicti = {'user_rating': user_rating, 'username':username[0], 'dp': dp[0] ,'legendary_grandmaster': False, 'international_grandmaster': False, 'grandmaster': False, 'international_master': False, 'master': False, 'candidate_master': False, 'expert': False,'specialist': False, 'pupil': False, 'newbie':False}
    #         dicti[rank[0].replace(' ', '_')] = True
    #         users.append(dicti)
    #         user_rating = crawler_2(str(user2))
    #         dicti = {'user_rating': user_rating, 'username':username[1], 'dp': dp[1] ,'legendary_grandmaster': False, 'international_grandmaster': False, 'grandmaster': False, 'international_master': False, 'master': False, 'candidate_master': False, 'expert': False,'specialist': False, 'pupil': False, 'newbie':False}
    #         dicti[rank[1].replace(' ','_')] = True
    #         users.append(dicti)
    #         return render(request, 'crawler/compare.html', {'users': users})
    # form = CompareIDForm()
    # return render(request, 'crawler/login.html', {'form': form})
    #template_name = 'crawler/compare_form.html'
    if request.method == 'GET':
         formset = CompareIDFormset(request.GET or None)
    elif request.method == 'POST':
        formset = CompareIDFormset(request.POST)
        if formset.is_valid():
            users = []
            for form in formset:
                user = form.cleaned_data.get('username')
                if user:
                    username, rank, dp = crawler_1([str(user)])
                    user_rating = crawler_2(str(user))
                    dicti = {'user_rating': user_rating, 'username':username[0], 'dp': dp[0] ,'legendary_grandmaster': False, 'international_grandmaster': False, 'grandmaster': False, 'international_master': False, 'master': False, 'candidate_master': False, 'expert': False,'specialist': False, 'pupil': False, 'newbie':False}
                    dicti[rank[0].replace(' ', '_')] = True
                    users.append(dicti)
            return render(request, 'crawler/compare.html', {'users': users})
    return render(request, 'crawler/compare_form.html', {'formset': formset})