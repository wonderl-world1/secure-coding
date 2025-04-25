from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('market.urls')),  # market 앱의 url을 가져옴
]
