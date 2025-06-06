from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, Bitacora
from .forms import ProfileForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime
from django.http import HttpResponse
import openpyxl
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from apps.dashboard.models import Bitacora
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.models import User

from .models import Profile

# Create your views here.


def signin(request):
    if request.method == 'GET':
        return render(request, 'sign-in.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is None:
            Bitacora.objects.create(
                    user = None,
                    movimiento=f"Intento de inicio de sesión fallido para el usuario: {username}"
                )
            return render(request, 'sign-in.html', {
                'error_match' : 'Usuario o contraseña son incorrectas'
            })
        else:
            Bitacora.objects.create(
                    user = user,
                    movimiento=f"Inicio de sesión exitoso para el usuario: {username}"
                )
            login(request,user)
            return redirect('profile')
#Cerrar sesión
def close(request):
    if request.user.is_authenticated:
        username = request.user.username
        Bitacora.objects.create(movimiento=f"{username} cerró sesión", fecha=now())
    
    logout(request)
    return redirect('signin') 

#Resitrar usuarios
def signup(request):
    if request.method == 'GET':
        return render(request, 'sign-up.html')
    else: 
        print(request.POST)
        #Comparación de contraseñas
        if request.POST['password1'] == request.POST['password2']:
            #Generar usuario
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], 
                    password=request.POST['password1']
                )
                user.save() #Guardar objesto en db
                login(request, user) #Guardar sesión
                
                Bitacora.objects.create(
                    user = user,
                    movimiento=f"Registro exitoso para el usario: {user.username}"
                )

                return redirect('profile')
            except:
                Bitacora.objects.create(
                    user = None,
                    movimiento=f"Intento fallido para el usuario: {request.POST['username']}, Usuario ya existente"
                )
                return render(request, 'sign-up.html', {
                    'error_exists' : 'Usuario ya existe'
                })
        else:
            Bitacora.objects.create(
                    user = None,
                    movimiento=f"Intento de registro fallido: {request.POST['username']}, Las contraseñas no coinciden"
                )
        return render(request, 'sign-up.html', {
                    'error_match' : 'Las contraseñas no coinciden'
                })


def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def bitacora(request):
    #profile_list = Profile.objects.filter(estatus=True, username= 'Gera').order_by('name')
    profile_list = Profile.objects.all().order_by('estatus')
    #filter(estatus=True).order_by('name')
    bitacora_list = Bitacora.objects.all().order_by('-fecha')

    #Buscador perfiles
    search_query = request.GET.get('filter', '')
    if search_query: 
        profile_list = profile_list.filter(
            Q(name__icontains = search_query) |
            Q(email__icontains = search_query) 
        )
    
    #Paginador
    paginator = Paginator(profile_list, 5)
    page_number = request.GET.get('page')
    profiles = paginator.get_page(page_number)

    #-----------------------------------------

    search_query2 = request.GET.get('filter2', '')
    if search_query2: 
        bitacora_list = bitacora_list.filter(
            Q(movimiento__icontains = search_query2) |
            Q(fecha__icontains = search_query2) 
        )
    
    paginator2 = Paginator(bitacora_list, 5)
    page_number2 = request.GET.get('page')
    bitacoras = paginator2.get_page(page_number2)

    context={
        'bitacoras': bitacoras,
        'profiles' : profiles,
        'search_query' : search_query,
        'search_query2' : search_query2,
    }

    return render(request, 'bitacora.html' ,context)

@login_required
def profile(request):
    profile = Profile.objects.filter(user=request.user).first() 
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            if profile is None:
                new_profile = form.save(commit=False)
                new_profile.user=request.user
                print(request.POST, request.FILES)
                new_profile.save() 

                messages.success(request, f'Se guardó el perfil {new_profile.name}')

                #Bitacora
                Bitacora.objects.create(
                    movimiento=f"se creo el perfil: {new_profile.name} con phone {new_profile.phone}"
                )
            else:
                messages.error(request, 'Ya tienes un perfil creado')
            return redirect(to='profile')
    else:
        print('No está mostrando los datos')
        form = ProfileForm()

    context = {
        'profile': profile,
        'form': form
    } 
    return render(request, 'profile.html', context)

@login_required
def editar_profile(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Perfil actualizado con éxito.')
            return redirect('edit_profile')  # o a donde quieras redirigir
        else:
            messages.error(request, '❌ Hay errores en el formulario.')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})


def delete_profile(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    profile.estatus1 = False
    profile.save()
    #profile.delete()

    #Bitacora
    Bitacora.objects.create(
                movimiento=f"se dió de baja el perfil: {profile.name} con phone {profile.phone}"
            )
    return redirect( 'tables')

def export_bitacora_xlsx(request):
    bitacoras = Bitacora.objects.all()
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Bitacora"

    ws.append(["ID", "Movimiento", "Fecha"])

    for b in bitacoras:
        ws.append([b.id, b.movimiento, b.fecha.strftime("%Y-%m-%d %H:%M:%S")])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=bitacora.xlsx'
    wb.save(response)
    return response


def export_profiles(request):
    perfiles = Profile.objects.all()
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Profiles"

    ws.append(["ID", "Username", "Name", "Phone", "Email", "Estatus"])

    for p in perfiles:
        ws.append([
            p.id,
            p.username,
            p.name,
            p.phone,
            p.email,
            'Activo' if p.estatus else 'Inactivo'
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=profiles.xlsx'
    wb.save(response)
    return response