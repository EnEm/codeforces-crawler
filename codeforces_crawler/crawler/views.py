from django.shortcuts import render
from codeforces_crawler.forms import UserIDForm
# Create your views here.

def index(request):
    form = UserIDForm()
    return render(request,'crawler/index.html', {'form': form})