from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
import random
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateView

# Create your views here.



# def restaurants_listview(request):
#     template_name = 'restaurants/restaurants-list.html'
#     queryset = RestaurantLocation.objects.all()
#     context = {
#         'object_list': [12, 432, 1234, 9821],
#         'restaurants_list': queryset,
#     }
#     return render(request, template_name, context)


def restaurant_createview(request):
    form = RestaurantLocationCreateView(request.POST or None)
    errors = None

    if form.is_valid():
        form.save()
        # obj = RestaurantLocation.objects.create(
        #     name=form.cleaned_data.get('name'),
        #     location=form.cleaned_data.get('location'),
        #     category=form.cleaned_data.get('category'),
        # )
        return HttpResponseRedirect('/restaurants/')
    if form.errors:
        errors = form.errors

    template_name = 'restaurants/form.html'
    context = {'form': form, 'errors': errors}
    return render(request, template_name, context)



class RestaurantsListView(ListView):

    def get_queryset(self):
        # print(self.kwargs)

        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()

        return queryset


class RestaurantsDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

    # Sprawdzenie jak wygląda obiekt
    # def get_context_data(self, *args, **kwargs):
    #     print(self.kwargs)
    #     context = super(RestaurantsDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context


class RestaurantCreateView(CreateView):
    form_class = RestaurantLocationCreateView
    template_name = 'restaurants/form.html'
    success_url = '/restaurants/'


# def home(request):
#
#     num = random.randint(0, 10000000000000)
#
#     rand_list = [num, random.randint(0, 10000000000000), random.randint(0, 10000000000000)]
#
#     context = {
#         "variable": num,
#         "list": rand_list,
#         "bool": True}
#
#     return render(request, "home.html", context)
#
#
# def about(request):
#     return render(request, "about.html")
#
#
# def contact(request):
#     return render(request, "contact.html")
#


#
# class HomeView(TemplateView):
#     template_name = "home.html"
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(HomeView, self).get_context_data(*args, **kwargs)
#
#         num = random.randint(0, 10000000000000)
#         rand_list = [random.randint(0, 10000000000000), random.randint(0, 10000000000000), random.randint(0, 10000000000000)]
#
#         print(context)
#         context = {
#             "variable": num,
#             "list": rand_list,
#             "bool": True}
#         return context
#
#
# class AboutView(TemplateView):
#     template_name = "about.html"
#
# class ContactView(TemplateView):
#     template_name = "contact.html"