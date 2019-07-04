from django.urls import path
from mpesa import views

urlpatterns = [
    path('mpesa/', views.mpesa_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
]