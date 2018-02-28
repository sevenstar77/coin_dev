from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.
class AccountInfoAPIView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        pass

class AccountDetailAPIView(RetrieveUpdateDestroyAPIView):
    def get(self):
        pass
    def patch(self, request, *args, **kwargs):
        pass