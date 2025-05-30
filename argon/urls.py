from django.contrib import admin
from django.urls import path
from apps.dashboard import views

from django.conf import settings  
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard,name='dashboard'),
    path('edit_profile/<int:id>/', views.edit_profile, name='edit_profile'),
    path('delete_profile/<int:id>/', views.delete_profile, name='delete_profile'), 
    path('tables/', views.tables,name='tables'),
    path('profile/', views.profile,name='profile'),
    path('signin/', views.signin,name='signin'),
    path('signup/', views.signup,name='signup'),
     path('export/profiles/', views.export_profiles_xlsx, name='export_profiles'),
    path('export/bitacora/', views.export_bitacora_xlsx, name='export_bitacora'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
