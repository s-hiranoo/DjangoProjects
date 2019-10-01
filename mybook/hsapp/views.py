import operator
from functools import reduce

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView
from django.views.generic.list import ListView
from .models import *
from .forms import *
import pandas as pd
from io import TextIOWrapper, StringIO


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'hsapp/home.html'


class CreateNewFarmer(LoginRequiredMixin, CreateView):
    model = Farmer
    form_class = FarmerCreationForm
    template_name = "hsapp/create_farmer.html"
    success_url = reverse_lazy('hsapp:home')


class ProductList(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'hsapp/product_list.html'


class ProductInSeasonList(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'hsapp/product_list.html'

    def get_queryset(self):
        result = super(ProductInSeasonList, self).get_queryset()
        month_now = timezone.now().month
        plants_in_season_candidate = Plant.objects.filter(season_end__gte=month_now)
        plants_in_season = []
        for plant in plants_in_season_candidate:
            s_in = plant.season_in
            s_end = plant.season_end
            if s_in > s_end:
                plants_in_season.append(plant)
            elif s_in <= month_now:
                plants_in_season.append(plant)

        result = result.filter(plant__in=[plant for plant in plants_in_season])

        return result


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'hsapp/product_detail.html'


class PlantList(LoginRequiredMixin, ListView):
    model = Plant
    template_name = 'hsapp/plant_list.html'


class PlantDetail(LoginRequiredMixin, DetailView):
    model = Plant
    template_name = 'hsapp/plant_detail.html'


class CompanyList(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'hsapp/company_list.html'


class CompanyDetail(LoginRequiredMixin, DetailView):
    model = Company
    template_name = 'hsapp/company_detail.html'


class DealerInfo(LoginRequiredMixin, ListView):
    template_name = 'hsapp/dealer_info.html'
    model = Dealer
    context_object_name = 'dealers'
    def get_queryset(self):
        dealers = Dealer.objects.all()
        return dealers


class FarmerList(LoginRequiredMixin, ListView):
    model = Farmer
    context_object_name = 'farmers'
    template_name = 'hsapp/farmer_list.html'
    #paginate_by = 10

    def get_queryset(self):
        login_user = self.request.user
        farmers = Farmer.objects.all()
        if login_user.groups.filter(name='FO').exists() and (not login_user.is_superuser):
            name = login_user.first_name
            fo = FieldOfficer.objects.get(name=name)
            farmers = fo.farmers.all()

        if "order_by" in self.request.GET:
            order_key = self.request.GET.get('order_by')
            farmers = farmers.order_by(order_key)
        return farmers


class SearchResultsView(ListView):
    model = Farmer
    context_object_name = 'farmers'
    template_name = 'hsapp/farmer_list.html'
    paginate_by = 10

    def get_queryset(self):
        result = super(SearchResultsView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            condition_name = reduce(operator.or_, [Q(name__icontains=q) for q in query_list])
            condition_product = reduce(operator.or_, [Q(product__icontains=q) for q in query_list])

            result = result.filter(condition_name & condition_product)

        return result


def search_test(request):
    farmers = Farmer.objects.all()
    query = ''
    query_list = ''
    if 'q' in request.GET:
        query = request.GET.get('q')
        query_list = query.split()


    template_name = 'hsapp/farmer_list.html'
    context = {'farmers': farmers}
    #return render(request, template_name, context)
    return HttpResponse(query_list)

