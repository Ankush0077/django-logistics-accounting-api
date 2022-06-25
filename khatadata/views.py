from .models import Party,PartyTransaction,Supplier,SupplierTransaction,Driver,DriverTransaction
from .serializers import PartySerializer,PartyTransactionSerializer,SupplierSerializer,SupplierTransactionSerializer,DriverSerializer,DriverTransactionSerializer
from rest_framework import viewsets

class PartyModelViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    
class DriverModelViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    
class SupplierModelViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    
class PartyTransactionModelViewSet(viewsets.ModelViewSet):
    queryset = PartyTransaction.objects.all()
    serializer_class = PartyTransactionSerializer
    
class DriverTransactionModelViewSet(viewsets.ModelViewSet):
    queryset = DriverTransaction.objects.all()
    serializer_class = DriverTransactionSerializer
    
class SupplierTransactionModelViewSet(viewsets.ModelViewSet):
    queryset = SupplierTransaction.objects.all()
    serializer_class = SupplierTransactionSerializer