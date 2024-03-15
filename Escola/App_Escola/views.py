from django.shortcuts import render

# Create your views here.
def abre_index(request):
    return render(request, 'login.html')

def enviar_login(request):
    return render(request, 'pgresposta.html')
