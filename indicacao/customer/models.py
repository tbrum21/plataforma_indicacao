from django.db import models
from django.urls import reverse

# Create your models here.

# Modelo de cliente com os campos:
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    birth_date = models.DateField()
    area_code = models.CharField(max_length=3)
    phone = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=8)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True define o campo com a data e hora atual quando o objeto é criado
    updated_at = models.DateTimeField(auto_now=True) # auto_now=True atualiza o campo com a data e hora atual sempre que o objeto é salvo
       
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}' # sempre que o objeto é chamado e não especificado o nome do campo, retorna o nome do cliente
    
    def get_full_phone_number(self):
        return f'({self.area_code}) {self.phone}' # retorna o número de telefone com o código de área
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}' # retorna o nome completo do cliente
    
    def get_full_address(self):
        return f'{self.address} - {self.city} - {self.state} - {self.zip_code}' # retorna o endereço completo do cliente
    
    def get_absolute_url(self):
        return reverse("customer:customer_update", kwargs={"id": self.id}) # retorna a url do cliente
    
    def get_delete_url(self):
        return reverse("customer:customer_delete", kwargs={"id": self.id}) # retorna a url do cliente
    
class Meta:
    db_table = 'clientes' # define o nome da tabela no banco de dados


