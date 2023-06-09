from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('register/', views.signup, name="register"),
    path('account/', views.account, name="account"),
]
