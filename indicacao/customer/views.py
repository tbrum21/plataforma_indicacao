from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse
from django.db.models import Q

# Create your views here.

class CustomerListView(ListView):
    template_name = "customer/customer_list.html"
    paginate_by = 5
    model = Customer

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
           object_list = self.model.objects.filter(
               Q(first_name__icontains=name) | Q(last_name__icontains=name)
               )
        else:
            object_list = self.model.objects.all()
        return object_list

class CustomerCreateView(CreateView): # cria um novo cliente
    template_name = "customer/customer.html" # template para criar um novo cliente
    form_class = CustomerForm # form para criar um novo cliente

    def form_valid(self, form): 
        return super().form_valid(form) # salva o formulário e redireciona para a página de listagem de clientes
    
    def get_success_url(self):
        return reverse("customer:customer_list")


class CustomerUpdateView(UpdateView): # atualiza um cliente existente
    template_name = "customer/customer.html" # template para atualizar um cliente existente
    form_class = CustomerForm # form para atualizar um cliente existente

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id)

    def form_valid(self, form):
        return super().form_valid(form) # salva o formulário e redireciona para a página de listagem de clientes
    
    def get_success_url(self):
        return reverse("customer:customer_list")
    
class CustomerDeleteView(DeleteView): # deleta um cliente existente
     
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id)
    
    def get_success_url(self):
        return reverse("customer:customer_list")