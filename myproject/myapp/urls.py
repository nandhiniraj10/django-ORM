from django.urls import path
from . import views

urlpatterns = [
    path('create_data/', views.create_data, name='create_data'),
    path('show_authors/', views.show_authors, name='show_authors'),
    path('filter_books/', views.filter_books, name='filter_books'),
    path('aggregate_data/', views.aggregate_data, name='aggregate_data'),
    path('annotate_data/', views.annotate_data, name='annotate_data'),
    path('complex_query/', views.complex_query, name='complex_query'),
]
