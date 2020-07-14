from django.shortcuts import render, redirect
from codeforces_crawler.forms import UserIDForm, CompareIDForm
from codeforces_crawler.forms import CompareIDFormset
# Create your views here.

def login(request):
    if request.method == "POST":
        form = UserIDForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            return render(request, 'crawler/profile.html', {'user': user})
    form = UserIDForm()
    return render(request,'crawler/login.html', {'form':form})

def profile(request):
    return render(request, 'crawler/profile.html')

def home(request):
    return render(request, 'crawler/home.html')

def compare(request):
    if request.method == 'GET':
         formset = CompareIDFormset(request.GET or None)
    elif request.method == 'POST':
        formset = CompareIDFormset(request.POST)
        if formset.is_valid():
            users = []
            for form in formset:
                user = form.cleaned_data.get('username')
                if user:
                    users.append(user)
            return render(request, 'crawler/compare.html', {'users': users})
    return render(request, 'crawler/compare_form.html', {'formset': formset})