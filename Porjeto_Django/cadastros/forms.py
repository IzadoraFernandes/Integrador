from django import forms
from django.core.mail.message import EmailMessage
import datetime 
from .models import Reserva, Sala, Laboratorio

class CadastrarReservaModelForm(forms.ModelForm):
    
    class Meta:
        model = Reserva
        fields = [
            'nome', 
            'descricao',
            'data',
            'horario',
            'sala'
        ]

        widgets = {
            'horario': forms.Select(attrs={
                'placeholder': 'Selecione a opção desejada',
            }),
            'data': forms.DateInput(attrs={
                'placeholder': 'Selecione a opção desejada',
                'type':'date'
            }),
            'salas': forms.Select(attrs={
                'placeholder': 'Selecione a opção desejada',
                
            }),
        }

class CadastrarLaboratorioModelForm(forms.ModelForm):
    
    class Meta:
        model = Laboratorio
        fields = [
            'nome', 
            'descricao'
        ]
        
        

class CadastrarSalaModelForm(forms.ModelForm):
    
    class Meta:
        model = Sala
        fields = [
            'nome', 
            'numero',
            'bloco', 
            'descricao',
            'capacidade'
        ]

        widgets = {'tipo': forms.Select(attrs={
                
                'placeholder': 'Selecione a opção desejada',
            }),}