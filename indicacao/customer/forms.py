from django import forms
from .models import Customer

class DateInput(forms.DateInput):
    input_type = "date"
class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(label="Nome")
    last_name = forms.CharField(label="Sobrenome")
    email = forms.EmailField(label="Email")
    birth_date = forms.DateField(label="Data de Nascimento", widget=DateInput())
    area_code = forms.RegexField(label="DDD", regex=r"^\+?1?[0-9]{1,3}$", error_messages={"invalid": "Número de DDD inválido"}) # regex para validar o DDD
    phone = forms.RegexField(label="Telefone", regex=r"^\+?1?[0-9]{1,9}$", error_messages={"invalid": "Número de telefone inválido"}) # regex para validar o telefone
    zip_code = forms.RegexField(label="CEP", regex=r"^\+?1?[0-9]{1,9}$", error_messages={"invalid": "CEP inválido"}) # regex para validar o CEP // CANCELAR OBRIGATORIEDADE DO CEP
    state = forms.CharField(label="Estado")
    city = forms.CharField(label="Cidade")
    address = forms.CharField(label="Endereço")
    

    class Meta: 
        model = Customer
        fields = ["first_name", "last_name", "email", "birth_date", "area_code", "phone", "zip_code", "state", "city", "address"]


