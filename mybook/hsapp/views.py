import operator
from functools import reduce

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import TemplateView, CreateView, UpdateView
from django.views.generic.list import ListView
from .models import *
from .forms import *
import pandas as pd
from io import TextIOWrapper, StringIO


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'hsapp/home.html'



class CreateNewFarmer(CreateView):
    model = Farmer
    form_class = FarmerCreationForm
    template_name = "hsapp/create_farmer.html"
    success_url = reverse_lazy('hsapp:home')



class ProductList(ListView):
    model = Product
    template_name = 'hsapp/product_list.html'

    def get_queryset(self):
        result = super(ProductList, self).get_queryset()

        if 'q' in self.request.GET:
            query = self.request.GET.get('q')
            if 'season' in query:
                month_now = timezone.now().month
                plants_in_season = Plant.objects.filter(season_in__lt=month_now+1, season_out__gt=month_now-1)
                result = result.filter(plant_id__in=[plant.id for plant in plants_in_season])
            else:
                order_key = query
                result.order_by(order_key)
        return result



class DealerInfo(ListView):
    template_name = 'hsapp/dealer_info.html'
    model = Dealer
    context_object_name = 'dealers'
    def get_queryset(self):
        dealers = Dealer.objects.all()
        return dealers



class FarmerList(ListView):
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

