import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Brewery, Review
from django.urls import reverse
import uuid

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('search')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('search')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

def search_view(request):
    query = request.GET.get('q', '')
    search_by = request.GET.get('by', 'city')
    breweries = []

    if query:
        url = f'https://api.openbrewerydb.org/breweries?by_{search_by}={query}'
        response = requests.get(url)
        if response.status_code == 200:
            breweries = response.json()

    return render(request, 'search.html', {'breweries': breweries})

# views.py


def brewery_detail_view(request, brewery_id):
    brewery = get_object_or_404(Brewery, id=brewery_id)
    reviews = brewery.review_set.all()  # Assuming a related_name of 'review_set' for the reviews
    return render(request, 'brewery_detail.html', {'brewery': brewery, 'reviews': reviews})


def some_view(request):
    brewery_id = 'ddf69cff-978e-47b6-b42e-75f102418bd0'
    brewery_id_int = int(uuid.UUID(brewery_id).int)
    url = reverse('brewery_detail', kwargs={'brewery_id': brewery_id_int})