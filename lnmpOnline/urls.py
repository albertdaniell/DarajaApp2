from django.urls import path
from lnmpOnline import views

urlpatterns = [
    path('lnmpOnline/', views.LNMPList.as_view(), name="lnmp callbackurl"),
    # path('snippets/<int:pk>/', views.snippet_detail),
]