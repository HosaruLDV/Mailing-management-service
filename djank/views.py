from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from djank.models import Client, Message, DistributionList


# Create your views here.

class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('first_name', 'last_name', 'middle_name', 'email', 'comment')
    success_url = reverse_lazy('djank:client')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('djank:client')


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('first_name', 'last_name', 'middle_name', 'email', 'comment')
    success_url = reverse_lazy('djank:client')


class MessageListView(ListView):
    model = Message

class MessageCreateView(CreateView):
    model = Message
    fields = ('theme', 'text')
    success_url = reverse_lazy('djank:message')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('djank:message')


class MessageUpdateView(UpdateView):
    model = Message
    fields = ('theme', 'text')
    success_url = reverse_lazy('djank:message')


class DistributionListView(ListView):
    model = DistributionList


class DistributionCreateView(CreateView):
    model = DistributionList
    fields = ('__all__')
    success_url = reverse_lazy('djank:distribution')

class DistributionUpdateView(UpdateView):
    model = DistributionList
    fields = ('__all__')
    success_url = reverse_lazy('djank:distribution')


class DistributionDeleteView(DeleteView):
    model = DistributionList
    success_url = reverse_lazy('djank:distribution')

def send_message(requests):
    print(Client.last_name.all())