from . import views
from django.urls import path

urlpatterns = [
    path('load_home_page',views.load_home_page,name='load_home_page'),
    path('load_index_page',views.load_index_page,name='load_index_page'),
]
