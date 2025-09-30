from django.shortcuts import render
from serializers import ListingSerializer, BookingSerializer
from rest_framework import viewsets
from .models import Listing, Booking

# Create your views here.
class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    lookup_field = 'slug'

    def index(request):
        return render(request, 'index.html')
    def about(request):
        return render(request, 'about.html')
    def contact(request):
        return render(request, 'contact.html')
    def services(request):
        return render(request, 'services.html')


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer