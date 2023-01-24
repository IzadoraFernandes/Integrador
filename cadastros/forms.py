from django import forms
from django.core.mail.message import EmailMessage
import datetime
from .models import Reserva, Sala
from usuario.models import CustomUser
from utilits.test import test

class CadastrarReservaModelForm(forms.ModelForm):
    horario = forms.ChoiceField(choices=test())

    class Meta:
        model = Reserva
        fields = [
            'descricao',
            'data',
            'horario',
            'sala'
        ]

        widgets = {
            'horario': forms.Select(attrs={
                'placeholder': 'Selecione a opção desejada',
                'class': 'form-control'
            }),
            'data': forms.DateInput(attrs={
                'placeholder': 'Selecione a opção desejada',
                'type': 'date',
                'class': 'form-control'
            }),
            'sala': forms.Select(attrs={
                'placeholder': 'Selecione a opção desejada',
                'class': 'form-control'

            }),
            'nome': forms.TextInput(attrs={
                'placeholder': 'Seu nome completo',
                'class': 'form-control'
            }),
            'descricao': forms.Textarea(attrs={
                'placeholder': 'Anotações',
                'class': 'form-control'
            })
        }


class CadastrarSalaModelForm(forms.ModelForm):

    class Meta:
        model = Sala
        fields = [
            'nome',
            'numero',
            'bloco',
            'descricao',
            'capacidade',
            'tipo',
            'laboratorio'
        ]

        widgets = {'nome': forms.TextInput(attrs={
            'placeholder': 'Ex: Laboratório de Informática III',
            'class': 'form-control'
        }),
            'numero': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'bloco': forms.TextInput(attrs={
                'placeholder': 'Ex: 01',
                'class': 'form-control'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'capacidade': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'tipo': forms.TextInput(attrs={
                'class': 'form-control'
            }),

        }
