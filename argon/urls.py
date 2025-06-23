from django.contrib import admin
from django.urls import path
from apps.dashboard import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path

from django.conf.urls.static import static
from apps.tasks import views as task_view


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.dashboard, name='dashboard'),

    # Login con la vista genérica de Django
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # Si usas login personalizado, comenta la de arriba y descomenta esta:
    # path('login/', views.login_view, name='login'),

    # Vistas del perfil
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.editar_profile, name='edit_profile'),  # ✅ usando request.user
    path('delete_profile/<int:id>/', views.delete_profile, name='delete_profile'),

    # Bitácora y exportaciones
    path('bitacora/', views.bitacora, name='bitacora'),
    path('export/bitacora/', views.export_bitacora_xlsx, name='export_bitacora'),
    path('export_profiles/', views.export_profiles, name='export_profiles'),

    # Registro de usuarios
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),

    # Cerrar sesión
    path('close/', views.close, name='close'),
    path('edit_profile/', views.editar_profile, name='edit_profile'),
    path('profile/', views.profile, name='profile'),

    path('tasks/', task_view.tasks, name='tasks'),

  

] 