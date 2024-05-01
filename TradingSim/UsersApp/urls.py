from django.urls import path
from .views import signup_user, login_user, logout_user, delete_account

app_name = 'user'

urlpatterns = [
    path("signup/", signup_user, name="signup"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("delete-account/", delete_account, name="delete-account")
]
# router for Users App