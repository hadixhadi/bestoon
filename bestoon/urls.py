
from django.contrib import admin
from django.urls import path , include
from app import urls
from accounts import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("app.urls")),
    path('accounts/',include("accounts.urls"))
]
