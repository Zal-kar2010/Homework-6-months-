from django.contrib import admin
from django.urls import path, include
from . import swagger  # импортируем твой swagger.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', include('product.urls')),
   # path('api/v1/users/', include('users.urls')),
   path('api/v1/auth/', include('users.urls')),

]

# Подключаем swagger URL-ы
urlpatterns += swagger.urlpatterns
