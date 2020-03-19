from django.shortcuts import render
from codeforces_crawler.forms import UserIDForm, CompareIDForm
from .main import crawler_1, crawler_2
import json
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
            return render(request, 'crawler/index.html', dicti)
    form = UserIDForm()
    return render(request,'crawler/login.html', {'form':form})

def index(request):
    return render(request, 'crawler/index.html')

def compare(request):
    if request.method == "POST":
        form = CompareIDForm(request.POST)
        if form.is_valid():
            users = []
            user1 = form.cleaned_data['user1']
            user2 = form.cleaned_data['user2']
            username, rank, dp = crawler_1([str(user1), str(user2)])
            user_rating = crawler_2(str(user1))
            dicti = {'user_rating': user_rating, 'username':username[0], 'dp': dp[0] ,'legendary_grandmaster': False, 'international_grandmaster': False, 'grandmaster': False, 'international_master': False, 'master': False, 'candidate_master': False, 'expert': False,'specialist': False, 'pupil': False, 'newbie':False}
            dicti[rank[0].replace(' ', '_')] = True
            users.append(dicti)
            user_rating = crawler_2(str(user2))
            dicti = {'user_rating': user_rating, 'username':username[1], 'dp': dp[1] ,'legendary_grandmaster': False, 'international_grandmaster': False, 'grandmaster': False, 'international_master': False, 'master': False, 'candidate_master': False, 'expert': False,'specialist': False, 'pupil': False, 'newbie':False}
            dicti[rank[1].replace(' ','_ ')] = True
            users.append(dicti)
            return render(request, 'crawler/compare.html', {'users': users})
    form = CompareIDForm()
    return render(request, 'crawler/login.html', {'form': form})