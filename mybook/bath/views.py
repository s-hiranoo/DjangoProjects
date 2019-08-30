from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Member
from .forms import ReservationForm


def index(request):
    members = Member.objects.all().order_by('-done')
    context = {'members': members, 'user': request.user}
    return render(request, 'bath/index.html', context)


def reserve(request):
    member = Member.objects.get(name=request.user.username)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=member)
        if form.is_valid():
            member = form.save(commit=False)
            member.save()
            return redirect('bath:index')
    else:
        form = ReservationForm()

    context = {'member': member, 'form': form, }
    return render(request, 'bath/reserve.html', context)


def done(request, member_id):
    member = get_object_or_404(User, pk=member_id)
    member.done = not member.done
    member.save()
    return redirect('bath:index')


def show_login_user(request):
    user = request.user
    return render(request, 'bath/show_login_user.html', {'user': user})