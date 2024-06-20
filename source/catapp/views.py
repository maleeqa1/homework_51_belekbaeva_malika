from django.shortcuts import render
from django.http import HttpResponseRedirect
from catapp.cat_db import Cat
import random
# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request, "home.html")
    else:
        Cat.name = request.POST.get("name")
        return HttpResponseRedirect("/cat_info/")

def cat_info(request):
    if request.method == "GET":
        context = {
            "name": Cat.name,
            "age": Cat.age,
            "avatar" : Cat.avatar,
            "satiety" : Cat.satiety,
            "happiness" : Cat.happiness}
        return render(request, "cat_info.html",context=context)
    else:
        action = request.POST.get("action")
        if action == "feed":
            Cat.feed()
        elif action == "sleep":
            Cat.sleep()
        else:
            Cat.play()

    return HttpResponseRedirect("/cat_info/")

