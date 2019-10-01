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

            if file_name == 'dealer_list':
                Dealer.objects.bulk_create(Dealer(name=df['name'][i], location=df['location'][i]) for i in range(n))
                return redirect('upload:load_csv')

            elif file_name == 'farmer_list':
                Farmer.objects.bulk_create(Farmer(
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
                    ) for i in range(n))
                return redirect('upload:load_csv')

            elif file_name == 'field_officer_list':
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

            elif file_name == 'visit_farmer_list':
                VisitFarmer.objects.bulk_create(VisitFarmer(
                        farmer=Farmer.objects.get(name=df['farmer'][i]),
                        field_officer=FieldOfficer.objects.get(name=df['field_officer'][i]),
                        done_or_appointment=mybool(df['done_or_appointment'][i]),
                        date=mydate(['date'][i]),
                        check_in_time=df['check_in'][i],
                        check_out_time=df['check_out'][i],
                    ) for i in range(n))
                return redirect('upload:load_csv')

            elif file_name == 'visit_dealer_list':
                VisitDealer.objects.bulk_create(VisitDealer(
                        dealer=Dealer.objects.get(name=df['dealer'][i]),
                        field_officer=FieldOfficer.objects.get(name=df['field_officer'][i]),
                        done_or_appointment=mybool(df['done_or_appointment'][i]),
                        date=mydate(df['date'][i]),
                        check_in_time=df['check_in'][i],
                        check_out_time=df['check_out'][i],
                    ) for i in range(n))
                return redirect('upload:load_csv')

            elif file_name == 'plant_list':
                Plant.objects.bulk_create(Plant(
                        name=df['name'][i],
                        species=df['species'][i],
                        season_in=df['season_in'][i],
                        season_end=df['season_end'][i],
                    ) for i in range(n))
                return redirect('upload:load_csv')

            if file_name == 'company_list':
                Company.objects.bulk_create(Company(
                        name=df['name'][i],
                        location=df['location'][i],
                    ) for i in range(n))

                return redirect('upload:load_csv')

            elif file_name == 'product_list':
                Product.objects.bulk_create(Product(
                        plant=Plant.objects.get(name=df['plant'][i]),
                        company=Company.objects.get(name=df['company'][i]),
                        name=df['name'][i],
                        quantity=df['quantity'][i],
                        price=df['price'][i],
                    ) for i in range(n))
                return redirect('upload:load_csv')

            elif file_name == 'prospect_farmer_list':
                ProspectFarmer.objects.bulk_create(ProspectFarmer(
                        farmer=Farmer.objects.get(name=df['farmer'][i]),
                        name=df['name'][i],
                        date=mydate(df['date'][i]),
                    ) for i in range(n))
                return redirect('upload:load_csv')

            elif file_name == 'escalation_list':
                Escalation.objects.bulk_create(Escalation(
                        farmer=Farmer.objects.get(name=df['farmer'][i]),
                        field_officer=FieldOfficer.objects.get(name=df['field_officer'][i]),
                        tmo_call_required=df['tmo_call_required'][i],
                        date=mydate(df['date'][i]),
                    ) for i in range(n))
                return redirect('upload:load_csv')

            elif file_name == 'farmer_plant_list':
                FarmerPlant.objects.bulk_create(FarmerPlant(
                        farmer=Farmer.objects.get(name=df['farmer'][i]),
                        plant=Plant.objects.get(name=df['plant'][i]),
                        plant_period=df['plant_period'][i],
                        major=mybool(df['major'][i]),
                    ) for i in range(n))
                return redirect('upload:load_csv')

            elif file_name == 'dealer_farmer_relation_list':
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

            elif file_name == 'purchase_history_list':
                PurchaseHistory.objects.bulk_create(PurchaseHistory(
                        dealer=Dealer.objects.get(name=df['dealer'][i]),
                        farmer=Farmer.objects.get(name=df['farmer'][i]),
                        product=Product.objects.get(name=df['product'][i]),
                        date=mydate(['date'][i]),
                        quantity=int(df['quantity'][i]),
                    ) for i in range(n))
                return redirect('upload:load_csv')

            elif file_name == 'farmer_interest_list':
                FarmerInterest.objects.bulk_create(FarmerInterest(
                        farmer=Farmer.objects.get(name=df['farmer'][i]),
                        plant=Plant.objects.get(name=df['plant'][i]),
                        interested=mybool(df['interested'][i]),
                        quantity=int(df['quantity'][i]),
                        date=mydate(df['date'][i]),
                    ) for i in range(n))
                return redirect('upload:load_csv')

            elif file_name == 'dealer_product_list':
                DealerProduct.objects.bulk_create(DealerProduct(
                        dealer=Dealer.objects.get(name=df['dealer'][i]),
                        product=Product.objects.get(name=df['product'][i]),
                        quantity=int(df['quantity'][i]),
                        date=mydate(df['date'][i]),
                    ) for i in range(n))
                return redirect('upload:load_csv')

            return redirect('upload:load_csv')
        else:
            return render(request, 'upload/upload.html')

    except NameError:
        context['error_message'] = 'You failed to upload data. Please check file-name and header-name.'
        return render(request, 'upload/upload.html', context)

    except AttributeError:
        context['error_message'] = 'You failed to upload data. Please check file-name and header-name.'
        return render(request, 'upload/upload.html', context)
