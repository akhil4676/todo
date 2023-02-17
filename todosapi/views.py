from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from myapp.models import

# Create your views here.

class TodosView(ViewSet):
    def list(self,request,*args,**kw):
        return Response(data="list of resources")

    def create(self,request,*args,**kw):
        return Response(data="created")

    def retrieve(self,request,*args,**kw):
        return Response(data="detail of an object")

    def update(self,request,*args,**kw):
        return Response(data="updating resources")

    def destroy(self,request,*args,**kw):
        return Response(data="deleted")
