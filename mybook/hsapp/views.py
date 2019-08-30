from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Farmer, FieldOfficer


class FarmerList(ListView):
    model = Farmer
    context_object_name = 'farmers'
    template_name = 'hsapp/farmer_list.html'
    paginate_by = 10

    def get_queryset(self):
        farmers = Farmer.objects.all()
        if "order_by" in self.request.GET:
            order_key = self.request.GET.get('order_by')
            farmers = farmers.order_by(order_key)
        return farmers


def farmerlist(request):
    farmers = Farmer.objects.all()
    if "order_by" in request.GET:
        order_key = request.GET.get('order_by')
        farmers = farmers.order_by(order_key)

    template_name = 'hsapp/farmer_list.html'
    context = {'farmers': farmers}
    return render(request, template_name, context)
