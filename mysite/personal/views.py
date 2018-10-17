from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content' : ['Contact info:', 'brookska@g.cofc.edu']})

def projects(request):
    return render(request, 'personal/projects.html')

def blog(request):
    return render(request, 'personal/blog.html')
