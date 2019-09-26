import operator
from functools import reduce

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

class HomeView(TemplateView):
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
        farmers = Farmer.objects.all()
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



########  load csv file  #########################################################################

def mybool(val):
    if val=='n':
        return False
    return True

def mylist(val):
    lis = list(map(int, val.split()))
    return lis

def upload(request):
    debug = False
    context = {}
    if 'csv' in request.FILES:
        if 'dealer' in str(request.FILES['csv']):
            context['key'] = 'dealer'
            form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
            dealers = pd.read_csv(form_data)
            n = len(dealers)
            for i in range(n):
                Dealer.objects.create(
                    name=dealers['name'][i],
                    location=dealers['location'][i],
                )
            return redirect('hsapp:upload')

        elif 'farmer' in str(request.FILES['csv']):
            form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
            farmers = pd.read_csv(form_data)
            n = len(farmers)
            context['key'] = 'farmer'
            for i in range(n):
                Farmer.objects.create(
                    phone=farmers['phone'][i],
                    name=farmers['name'][i],
                    state_id_number=farmers['state_id_number'][i],
                    state_id_picture='data/sample_picture.jpg',
                    birth_date=farmers['birth_date'][i],
                    dependents=farmers['dependents'][i],
                    land_size=int(farmers['land_size'][i]),
                    leased_land=mybool(farmers['leased_land'][i]),
                    previous_hs_client=mybool(farmers['previous_hs_client'][i]),
                    location=farmers['location'][i],
                )
            return redirect('hsapp:upload')

        elif 'fo' in str(request.FILES['csv']):
            form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
            fos = pd.read_csv(form_data)
            n = len(fos)
            for i in range(n):
                FieldOfficer.objects.create(
                    name=fos['name'][i],
                    farmer_ids=mylist(fos['farmer_ids'][i]),
                )

            return redirect('hsapp:upload')

    else:
        return render(request, 'hsapp/upload.html', context)
