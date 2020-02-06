from django.urls import path
from . import views

urlpatterns = [
    # path('/', views.home, name='home'),
    path('greeting/', views.greeting, name='greeting'),
    path('bleating/', views.ShowBleating.as_view(), name='bleating'),
]   