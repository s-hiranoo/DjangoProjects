from random import randint, random
from .models import Dealer, Farmer, FieldOfficer



d_num = 10
f_num = 50
fo_num = 5

locations = []
for i in range(100):
    location = str( int(random()*1000000) )
    locations.append(location)

products = ['tomato', 'potato', 'carrot', 'cucumber', 'apple', 'rice', 'pumpkin', 'ginger', 'cherry', 'onion', 'radish', 'lettuce', 'spinach', 'cabbage']

""" create dealers: name, location """
def create_dealers(num=d_num):
    for i in range(num):
        _name = 'dealer' + str(i+1)
        _location = locations[randint(0, len(locations)-1)]
        Dealer.objects.create(name=_name, location=_location)
    return

""" create farmers: name, product, season, location, (dealer) """
def create_farmers(num=50):
    for i in range(num):
        _name = 'farmer' + str(i+1)
        _product = products[randint(0, len(products)-1)]
        _season = randint(1, 12)
        _location = locations[i]
        _pk = randint(1, 10)
        _dealer = Dealer.objects.get(pk=_pk)
        Farmer.objects.create(name=_name, product=_product, season=_season, location=_location, dealer=_dealer)
    return


""" create field-officers: name, (farmers) """
name_list = ['Alex', 'Debby', 'Jack', 'Jorge', 'Cris', 'Dorothy']
def create_field_officers(num=fo_num):
    for i in range(num):
        _name = name_list[i]
        FieldOfficer.objects.create(name=_name)
    return



#create_dealers(d_num)
#create_farmers(f_num)
#create_field_officers(fo_num)
