from django.shortcuts import render,  redirect
from .forms import CustomUserCreateForm
#from django.contrib import messages
#from braces.views import GroupRequiredMixin

def cadastrar_usuario(request):
    if request.POST:
        form = CustomUserCreateForm(request.POST)
    else:
        form = CustomUserCreateForm()
    return render(request, 'cadastrar_usuario.html', {
        'form' : form,
    })

def register_view(request):

    if request.POST:
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/login")
    else:
        form = CustomUserCreateForm()

        return render(request, "register/register.html", {"form":form})

        


def login(request):
    return render(request, 'login.html')

def minhas_reservas(request):
    return render(request, 'minhas_reservas.html')

def usuarios(request):
    return render(request, 'usuarios.html')

#from django.views.generic import TemplateView

#class Cadastrar_labView(TemplateView):
    #template_name = 'cadastrar_lab.html'