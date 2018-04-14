from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import random
from django.views.generic import TemplateView

# Create your views here.

def home(request):

    num = random.randint(0, 10000000000000)

    rand_list = [num, random.randint(0, 10000000000000), random.randint(0, 10000000000000)]

    context = {
        "variable": num,
        "list": rand_list,
        "bool": True}

    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


class HomeView(TemplateView):
    template_name = "home.html"



    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)

        num = random.randint(0, 10000000000000)
        rand_list = [random.randint(0, 10000000000000), random.randint(0, 10000000000000), random.randint(0, 10000000000000)]

        print(context)
        context = {
            "variable": num,
            "list": rand_list,
            "bool": True}
        return context


class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(TemplateView):
    template_name = "contact.html"