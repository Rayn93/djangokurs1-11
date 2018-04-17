from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
import random
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateView

# Create your views here.


# @login_required()
# def restaurant_createview(request):
#     form = RestaurantLocationCreateView(request.POST or None)
#     errors = None
#
#     if form.is_valid():
#
#         if request.user.is_authenticated():
#
#             instance = form.save(commit=True)
#             instance.owner = request.user
#             instance.save()
#             # obj = RestaurantLocation.objects.create(
#             #     name=form.cleaned_data.get('name'),
#             #     location=form.cleaned_data.get('location'),
#             #     category=form.cleaned_data.get('category'),
#             # )
#             return HttpResponseRedirect('/restaurants/')
#         else:
#             return HttpResponseRedirect('/login/')
#
#     if form.errors:
#         errors = form.errors
#
#     template_name = 'restaurants/form.html'
#     context = {'form': form, 'errors': errors}
#     return render(request, template_name, context)



class RestaurantsListView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        queryset = RestaurantLocation.objects.filter(owner=self.request.user)
        #
        # slug = self.kwargs.get('slug')
        # if slug:
        #     queryset = RestaurantLocation.objects.filter(
        #         Q(category__iexact=slug) |
        #         Q(category__icontains=slug)
        #     )
        # else:
        #     queryset = RestaurantLocation.objects.all()

        return queryset


class RestaurantsDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        queryset = RestaurantLocation.objects.filter(owner=self.request.user)
        return queryset

    # Sprawdzenie jak wygląda obiekt
    # def get_context_data(self, *args, **kwargs):
    #     print(self.kwargs)
    #     context = super(RestaurantsDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context



class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateView
    template_name = 'restaurants/form.html'
    success_url = '/restaurants/'

    login_url = '/admin/login/'
    # redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)


    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add restaurant'
        return context


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantLocationCreateView
    template_name = 'restaurants/form.html'
    # success_url = '/restaurants/'
    #
    login_url = '/admin/login/'
    # redirect_field_name = 'redirect_to'

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update restaurant'
        return context


    def get_queryset(self):
        queryset = RestaurantLocation.objects.filter(owner=self.request.user)
        return queryset


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