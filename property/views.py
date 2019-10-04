from django.shortcuts import render
from .models import Property

def propertyList(request):
    property_list = Property.objects.all()
    context = {
        'property_list': property_list,
        'title':'Property'
    }
    return render(request, 'property/property.html', context)

def propertyDetail(request, id):
    property_detail = Property.objects.get(pk=id)
    print("details_list:", property_detail)
    context = {'property_detail': property_detail, 'title':'Property Details'}
    return render(request, 'property/property_detail.html', context)
