from django.shortcuts import render, redirect
from app.forms import LivrosForm
from app.models import Livros

# Create your views here.
def home(request):
    data = {} #Recebendo um dicionario
    data['db'] = Livros.objects.all()
    return render(request, 'index.html', data)


def formulario(request):
    data = {}
    data['formulario'] = LivrosForm()
    return render(request, 'formulario.html', data)


def create(request):
    formulario = LivrosForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Livros.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Livros.objects.get(pk=pk)
    data['formulario'] = LivrosForm(instance=data['db'])
    return render(request, 'formulario.html', data)


def update(request, pk):
    data = {}
    data['db'] = Livros.objects.get(pk=pk)
    form = LivrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Livros.objects.get(pk=pk)
    db.delete()
    return redirect('home')