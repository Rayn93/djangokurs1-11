from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .forms import ItemForm

# Create your views here.


class ItemListView(ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemDetailView(DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemCreateView(LoginRequiredMixin, CreateView):
    form_class = ItemForm
    template_name = 'restaurants/form.html'

    login_url = '/admin/login/'

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(ItemCreateView, self).form_valid(form)


    def get_context_data(self, *args, **kwargs):
        context = super(ItemCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add item'
        return context

    def get_form_kwargs(self):
        kwargs = super(ItemCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs



class ItemUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ItemForm
    template_name = 'restaurants/form.html'
    login_url = '/admin/login/'

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(ItemUpdateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ItemUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update item'
        return context

    def get_form_kwargs(self):
        kwargs = super(ItemUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
