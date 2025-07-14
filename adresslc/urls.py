from django.urls import path
from .views import AddressListCreateView, AddressRetrieveUpdateDeleteView

urlpatterns = [
    path('addresses/', AddressListCreateView.as_view(), name='address-list-create'),
    path('addresses/<int:pk>/', AddressRetrieveUpdateDeleteView.as_view(), name='address-rud'),
]
