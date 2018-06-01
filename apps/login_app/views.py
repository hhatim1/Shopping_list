# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from ..wishlist_app.models import Add_item
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "login_app/index.html")


def register(request):
    result = User.objects.registration_validation(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    #messages.success(request, "Successfully registered!")
    return redirect('/items/')


def login(request):
    result = User.objects.user_validation(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    #messages.success(request, "Successfully logged in!")
    return redirect('/items/')


def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')


"""def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'login_app/success.html', context)"""

