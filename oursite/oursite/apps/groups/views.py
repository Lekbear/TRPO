from django.shortcuts import render, redirect
from django.contrib.auth.models import Group


def index(response):
    if response.method == "POST":
        print(group_name)
        my_group = Group.objects.get(name='my_group_name')
        #return HttpResponseRedirect('/home/')

        #my_group.user_set.add(your_user)
        return redirect('/registergroup')
    else:
        return render(response, "/login")
