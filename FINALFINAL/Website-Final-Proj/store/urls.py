from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from appstore import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('quotation/', views.quotation_page, name='quotation_page'),

    path('', include('appstore.urls')),

]
