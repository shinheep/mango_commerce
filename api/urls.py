from django.urls import path
from .views.users import SignUp, SignIn, SignOut, ChangePassword
from .views.mangos import MangosView, MangoView

urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('mangos/', MangosView.as_view(), name='mangos'),
    path('mangos/<int:pk>', MangoView.as_view(), name='mango'),
]