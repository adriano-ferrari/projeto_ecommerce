from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse


class Criar(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('Criar')


class Atualizar(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('Atualizar')


class Login(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('Login')


class Logout(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout')
