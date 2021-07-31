from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path


def home_view(request):
    return redirect('api/v1/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('api/v1/', include('logistic.urls')),
]
