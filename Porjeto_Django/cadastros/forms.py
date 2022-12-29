from django import forms
from django.core.mail.message import EmailMessage
import datetime 

class Cadastrar_reservaForm(forms.Form):
    horario = datetime.datetime.now(label='Horário')