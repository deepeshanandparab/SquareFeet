from django.urls import path
from .views import propertyList
from .views import propertyDetail

urlpatterns = [
    path('', propertyList, name='property_list'),
    path('<id>', propertyDetail, name='property_detail')
]