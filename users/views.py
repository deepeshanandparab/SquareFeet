from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from property.models import Property
from .forms import UserRegistrationForm
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created sucessfully for {username}. You can login now.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {'form': form, 'title':'Registration'}
    return render(request, 'users/registration.html', context)

@login_required
def profile(request):
    current_user = request.user.id
    property_list = Property.objects.all().filter(id=current_user)
    print('Property List : ', property_list)
    context = {'title':'Profile','property_list': property_list }
    return render(request, 'users/profile.html', context)

def propertyDetail(request, id):
    property_detail = Property.objects.get(pk=id)
    print("details_list:", property_detail)
    context = {'property_detail': property_detail, 'title':'Property Details'}
    return render(request, 'property/property_detail.html', context)

@login_required
def adminDashboard(request):
    context = {'title':'Admin Dashboard'}
    return render(request, 'users/admin_dashboard.html', context)

