from curses import noecho
from traceback import print_tb
from unicodedata import name
from django import views
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views import View
from .models import Inventory, Supplier
from .serializers import InventorySerializer, SupplierSerializer
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)

import urllib


def home(request):
    return HttpResponse("""
        <div style="margin:0 auto;width:200px">
        <a href='/inventory'><h3>Ho to Inventory</h3></a>
        </div>
    """)


class InventoryApiView(APIView):
    def get(self, request, id=None):
        try:
            if id:
                # get the inventory by id
                inventory = Inventory.objects.get(id=id)
                serializer = InventorySerializer(inventory)
                return Response(serializer.data, status=HTTP_200_OK)
            else:
                # Get all the inventories by base on query params
                q = request.build_absolute_uri()
                if '?' in q:
                    q = q.split('?')[1]
                    text = q.split('=')[1]
                    text = urllib.parse.unquote(text)
                    inventory = Inventory.objects.filter(name__icontains=text)
                else:
                    # Get all the inventories by querying the database
                    inventory = Inventory.objects.all()
                serializer = InventorySerializer(inventory, many=True)
                return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=HTTP_400_BAD_REQUEST)


class InventoryView(View):
    def get(self, request, id=None):
        try:
            if id:
                # get the inventory by id
                inventory = Inventory.objects.get(id=id)
                return render(request, 'inventory_details.html', {'inventory': inventory})
            return render(request, 'inventory.html')
        except Exception as e:
            return HttpResponse(
                """
                <h1>Error: {}</h1>
                """.format(str(e))
            )
