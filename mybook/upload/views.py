import operator
from functools import reduce

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import Q
from django.views.generic import TemplateView, CreateView, UpdateView
from django.views.generic.list import ListView

import pandas as pd
from io import TextIOWrapper, StringIO
from hsapp.models import *
import datetime

def mybool(val):
    if val=='n':
        return False
    return True


def mylist(val):
    lis = list(map(int, val.split()))
    return lis


def mydate(val):
    now = timezone.now()
    year = now.year
    month = now.month
    day = now.day

    if '-' in val:
        year, month, day = map(int, val.split('-'))
    elif ',' in val:
        year, month, day = map(int, val.split(','))
    elif '/' in val:
        year, month, day = map(int, val.split('/'))
    else:
        year, month, day = map(int, val.split())

    return datetime.datetime(year=year, month=month, day=day)


def load_csv(request):
    context = {}
    try:
        if 'csv' in request.FILES:
            form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
            file_name = str(request.FILES.get('csv')).split('.')[0]
            df = pd.read_csv(form_data)
            n = len(df)

            if 'file_name' == 'dealer_list':
                dealers = []
                for i in range(n):
                    dealer = Dealer(
                        name=df['name'][i],
                        location=df['location'][i],
                    )
                    dealers.append(dealer)

                Dealer.objects.bulk_create(dealers)
                return redirect('upload:load_csv')

            elif 'file_name' == 'farmer_list':
                farmers = []
                for i in range(df):
                    farmer = Farmer(
                        phone=df['phone'][i],
                        name=df['name'][i],
                        state_id_number=df['state_id_number'][i],
                        state_id_picture='data/sample_picture.jpg',
                        birth_date=mydate(df['birth_date'][i]),
                        dependents=df['dependents'][i],
                        land_size=int(df['land_size'][i]),
                        leased_land=mybool(df['leased_land'][i]),
                        previous_hs_client=mybool(df['previous_hs_client'][i]),
                        location=df['location'][i],
                    )
                    farmers.append(farmer)
                Farmer.objects.bulk_create(farmers)
                return redirect('upload:load_csv')

            elif 'file_name' == 'field_officer_list':
                for i in range(n):
                    if df['name'][i] == 'none':
                        FieldOfficer.objects.create(name='none')
                        continue
                    instance = FieldOfficer.objects.create(
                        name=df['name'][i],
                    )
                    farmer_adds_name = df['farmers'][i].split()
                    farmer_adds_instance = Farmer.objects.filter(name__in=farmer_adds_name)
                    instance.farmers.set(farmer_adds_instance)

                return redirect('upload:load_csv')

            elif 'file_name' == 'visit_farmer_list':
                visits = []
                for i in range(n):
                    visit = VisitFarmer(
                        farmer=Farmer.objects.get(name=df['farmer']),
                        field_officer=FieldOfficer.objects.get(name=df['field_officer']),
                        done_or_appointment=mybool(df['done_or_appointment']),
                        date=mydate(['date']),
                        check_in_time=df['check_in'],
                        check_out_time=df['check_out'],
                    )
                    visits.append(visit)
                VisitFarmer.objects.bulk_create(visits)
                return redirect('upload:load_csv')

            elif 'file_name' == 'visit_dealer_list':
                visits = []
                for i in range(n):
                    visit = VisitDealer(
                        dealer=Dealer.objects.get(name=df['dealer']),
                        field_officer=FieldOfficer.objects.get(name=df['field_officer']),
                        done_or_appointment=mybool(df['done_or_appointment']),
                        date=mydate(df['date']),
                        check_in_time=df['check_in'],
                        check_out_time=df['check_out'],
                    )
                    visits.append(visit)
                VisitDealer.objects.bulk_create(visits)
                return redirect('upload:load_csv')

            elif 'file_name' == 'plant_list':
                plants = []
                for i in range(n):
                    plant = Plant(
                        name=df['name'],
                        species=df['species'],
                        season_in=df['season_in'],
                        season_end=df['season_end'],
                    )
                    plants.append(plant)
                Plant.objects.bulk_create(plants)
                return redirect('upload:load_csv')

            elif 'file_name' == 'company_list':
                companies = []
                for i in range(n):
                    company = Company(
                        name=df['name'],
                        location=df['location'],
                    )
                    companies.append(company)
                Company.objects.bulk_create(companies)
                return redirect('upload:load_csv')

            elif 'file_name' == 'product_list':
                products = []
                for i in range(n):
                    product = Product(
                        plant=Plant.objects.get(name=df['plant']),
                        company=Company.objects.get(name=df['company']),
                        name=df['name'],
                        quantity=df['quantity'],
                        price=df['price'],
                    )
                    products.append(product)
                Product.objects.bulk_create(products)
                return redirect('upload:load_csv')

            elif 'file_name' == 'prospect_farmer_list':
                prospects = []
                for i in range(n):
                    prospect = ProspectFarmer(
                        farmer=Farmer.objects.get(name=df['farmer']),
                        name=df['name'],
                        date=mydate(df['date']),
                    )
                    prospects.append(prospect)
                ProspectFarmer.objects.bulk_create(prospects)
                return redirect('upload:load_csv')

            elif 'file_name' == 'escalation_list':
                escalations = []
                for i in range(n):
                    escalation = Escalation(
                        farmer=Farmer.objects.get(name=df['farmer']),
                        field_officer=FieldOfficer.objects.get(name=df['field_officer']),
                        tmo_call_required=df['tmo_call_required'],
                        date=mydate(df['date']),
                    )
                    escalations.append(escalation)
                Escalation.objects.bulk_create(escalations)
                return redirect('upload:load_csv')

            elif 'file_name' == 'farmer_plant_list':
                farmer_plants = []
                for i in range(n):
                    farmer_plant = FarmerPlant(
                        farmer=Farmer.objects.get(name=df['farmer']),
                        plant=Plant.objects.get(name=df['plant']),
                        plant_period=df['plant_period'],
                        major=mybool(df['major']),
                    )
                    farmer_plants.append(farmer_plant)
                FarmerPlant.objects.bulk_create(farmer_plants)
                return redirect('upload:load_csv')

            elif 'file_name' == 'dealer_farmer_relation_list':
                relations = []
                for i in range(n):
                    relation = DealerFarmerRelation(
                        dealer=Dealer.objects.get(name=df['dealer']),
                        farmer=Farmer.objects.get(name=df['farmer']),
                        close_relation=mybool(df['close_relation']),
                    )
                    relations.append(relation)
                DealerFarmerRelation.objects.bulk_create(relations)
                return redirect('upload:load_csv')

            elif 'file_name' == 'purchase_history_list':
                histories = []
                for i in range(n):
                    history = PurchaseHistory(
                        dealer=Dealer.objects.get(name=df['dealer']),
                        farmer=Farmer.objects.get(name=df['farmer']),
                        product=Product.objects.get(name=df['product']),
                        date=mydate(['date']),
                        quantity=int(df['quantity']),
                    )
                    histories.append(history)
                PurchaseHistory.objects.bulk_create(histories)
                return redirect('upload:load_csv')

            elif 'file_name' == 'farmer_interest_list':
                interests = []
                for i in range(n):
                    interest = FarmerInterest(
                        farmer=Farmer.objects.get(name=df['farmer']),
                        plant=Plant.objects.get(name=df['plant']),
                        interested=mybool(df['interested']),
                        quantity=int(df['quantity']),
                        date=mydate(df['date']),
                    )
                    interests.append(interest)
                FarmerInterest.objects.bulk_create(interests)
                return redirect('upload:load_csv')

            elif 'file_name' == 'dealer_product_list':
                dealer_products = []
                for i in range(n):
                    dealer_product = DealerProduct(
                        dealer=Dealer.objects.get(name=df['dealer']),
                        product=Product.objects.get(name=df['product']),
                        quantity=int(df['quantity']),
                        date=mydate(df['date']),
                    )
                    dealer_products.append(dealer_product)
                DealerProduct.objects.bulk_create(dealer_products)
                return redirect('upload:load_csv')

        else:
            return render(request, 'upload/upload.html')

    except NameError:
        context['error_message'] = 'You failed to upload data. Please check file-name and header-name.'
        return render(request, 'upload/upload.html', context)

    except AttributeError:
        context['error_message'] = 'You failed to upload data. Please check file-name and header-name.'
        return render(request, 'upload/upload.html', context)
