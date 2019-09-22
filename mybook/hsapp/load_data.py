#from .models import Dealer, Farmer, FieldOfficer

import pandas as pd


def mybool(val):
    if val=='n':
        return False
    return True

def mylist(val):
    lis = list(map(int, val.split()))
    return lis


dealers = pd.read_csv('./data/dealer_list.csv')
farmers = pd.read_csv('./data/farmer_list.csv')
fos = pd.read_csv('./data/fo_list.csv')
n_dealers = len(dealers)
n_farmers = len(farmers)
n_fos = len(fos)



for i in range(n_dealers):
    Dealer.objects.create(
        name=dealers['name'][i],
        location=dealers['location'][i],
    )

for i in range(n_farmers):
    Farmer.objects.create(
        phone=farmers['phone'][i],
        name=farmers['name'][i],
        state_id_number=farmers['state_id_number'][i],
        birth_date=farmers['birth_date'][i],
        dependents=farmers['dependents'][i],
        land_size=int(farmers['land_size'][i]),
        leased_land=mybool(farmers['leased_land'][i]),
        previous_hs_client=mybool(farmers['previous_hs_client'][i]),
        location=farmers['location'][i],
    )


for i in range(n_fos):
    FieldOfficer.objects.create(
        name=fos['name'][i],
        farmer_ids=mylist(fos['farmer_ids'][i]),
    )