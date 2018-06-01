# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Add_item
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from ..login_app.models import User

# Create your views here.
def index(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user.first_name,
        'users': User.objects.all(),
        'items': Add_item.objects.filter(joined_by=user),
        'other_items': Add_item.objects.exclude(joined_by=user)
    }
    return render(request, 'wishlist_app/display.html', context)


def create(request):
    print 'inside create method'
    if request.method == 'POST':
        errors = Add_item.objects.item_validation(request.POST)
        if len(errors):  # if there's errors -- see models.py for error list!
            for error in errors.iteritems():
                messages.error(request, error)
            return redirect('/items/add_item')
        else:
            user = User.objects.get(id=request.session['user_id'])
            item = Add_item.objects.create(
                item=request.POST['item'], added_by=user)
            item.joined_by.add(user)
            item.save()
            return redirect('/items/')
    else:
        return redirect('/items/')


def info(request, item_id):
    item = Add_item.objects.get(id=item_id)
    context = {

        'item': item,
        # 'other_users': User.objects.exclude(created_items__created_by=item.created_by)
    }
    return render(request, 'wishlist_app/info.html', context)


def add_item(request):
    return render(request, 'wishlist_app/add_item.html')


def leave_item(request, item_id):
    item = Add_item.objects.get(id=item_id)
    user = User.objects.get(id=request.session['user_id'])
    item.joined_by.remove(user)
    item.save()
    return redirect('/items/')


def join_item(request, item_id):
    item = Add_item.objects.get(id=item_id)
    user = User.objects.get(id=request.session['user_id'])
    item.joined_by.add(user)
    item.save()
    return redirect('/items/')


def delete(request, item_id):
    item = Add_item.objects.get(id=item_id)
    item.delete()
    return redirect('/items/')