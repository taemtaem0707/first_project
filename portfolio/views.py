from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
# from third.models import Restaurant
# from third.forms import RestaurantForm
from django.http import HttpResponseRedirect




# Create your views here.
def loading(request):
    context = {
    }
    return render(request, 'portfolio/loading.html', context)


def main(request):
    context = {
    }
    return render(request, 'portfolio/main.html', context)


def info(request):
    context = {
    }
    return render(request, 'portfolio/info.html', context)


def portfolio(request):
    context = {
    }
    return render(request, 'portfolio/portfolio.html', context)


def team_project(request):
    context = {
    }
    return render(request, 'portfolio/team_project.html', context)


def certificates(request):
    context = {
    }
    return render(request, 'portfolio/certificates.html', context)


def blog(request):
    context = {
    }
    return render(request, 'portfolio/blog.html', context)