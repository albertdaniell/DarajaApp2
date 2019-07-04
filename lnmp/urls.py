from django.urls import path
from lnmp.views import LNMPApiView

urlpatterns = [
    path('lnmp/', LNMPApiView.as_view(), name="lnmp callbackurl"),
    # path('snippets/<int:pk>/', views.snippet_detail),
]