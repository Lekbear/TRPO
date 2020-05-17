from django.shortcuts import render, redirect


def index(response):
    if response.method == "POST":
        return redirect('/registergroup')
    else:
        return render(response, "groups/index.html")

    