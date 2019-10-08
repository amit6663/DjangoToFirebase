from django.urls import path
from . import views

urlpatterns = [
    path('', views.signIn, name='signIn'),
    path('postsign/',views.postsign,name='postsign'),
    path('Logout/',views.logout,name='log')
]
