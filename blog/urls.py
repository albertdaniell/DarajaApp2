from django.urls import path
from blog import views

urlpatterns = [
    path('blog/', views.blog_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
]