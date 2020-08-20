from django.urls import path,include
from Biblio.views import HomeView

# Create your views here.

urlpatterns = [
   path("", HomeView.as_view(), name = 'home'), 
]