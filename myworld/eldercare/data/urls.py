from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data/', views.data, name='data'),
    path('dataimport/', views.dataimport, name='dataimport'),
    path('upload/', views.upload, name='upload'),
    path('database/', views.database, name='database'),
    path('dataexport/', views.dataexport, name='dataexport'),
    path('dataentry/', views.dataentry, name='dataentry'),
    # path('process_file/', views.process_file, name='process_file'),
    path('elderinfo/', views.elderinfo, name='elderinfo'),
    path('vehicleinfo/', views.vehicleinfo, name='vehicleinfo'),
    path('centreinfo/', views.centreinfo, name='centreinfo'),
    path('optimize/', views.optimize, name='optimize'),
    path('visualize/', views.visualize, name='visualize'),
]