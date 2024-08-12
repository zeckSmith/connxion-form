
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import CustomUserCreationForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"vous etre connecté avec succes !!")
            return redirect('connexion')
            
        else:
            return render(request, 'inscription.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'inscription.html', {'form': form})
    
    # return HttpResponse("Erreur: requête non prise en charge.")

    


def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            #si les information de l'utilisateurs son valide alors connecte le
            login(request, user)
            return redirect('acceuil')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de pase incorect")
    
    return render(request, 'connexion.html')

@login_required
def acceuil(request):
    return render(request, 'acceuil.html')

def deconnexion(request):
    logout(request)
    return redirect('connexion')