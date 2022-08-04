from django.contrib import admin

# Register your models here.
from django.urls import path, include

from django.contrib import store,users,lists

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lists/', include(lists.urls)),
    path('users/', include(users.urls)),
    path('store/', include(store.urls)),
    
]
