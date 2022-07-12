from . import views
from django.urls import path

urlpatterns = [
    path('load_home_page',views.load_home_page,name='load_home_page'),
]
