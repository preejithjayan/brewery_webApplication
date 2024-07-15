from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Redirect root URL to login page
    path('login/', views.login_view, name='login'),  # Example URL pattern for login view
    path('signup/', views.signup_view, name='signup'),  # Example URL pattern for signup view
    path('search/', views.search_view, name='search'),  # Example URL pattern for search view
    path('brewery/<uuid:brewery_id>/', views.brewery_detail_view, name='brewery_detail'),  # Example URL pattern for brewery detail view
    # Add more URL patterns as needed
]
