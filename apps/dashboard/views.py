from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, Bitacora
from .forms import ProfileForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime
from django.contrib.auth.models import User
from apps.dashboard.models import Profile 
import openpyxl
from django.http import HttpResponse

def dashboard(request):
    return render(request, 'dashboard.html')


def tables(request):
    # Obtener todos los perfiles y bitácoras
    profile_list = Profile.objects.all()
    bitacora_list = Bitacora.objects.all()

    # Filtro para perfiles (nombre o email)
    search_query = request.GET.get('filter', '').strip()
    if search_query:
        profile_list = profile_list.filter(
            Q(name__icontains=search_query) |
            Q(email__icontains=search_query)
        )

    # Paginador para perfiles, 2 por página
    paginator = Paginator(profile_list, 2)
    page_number = request.GET.get('page')
    profiles = paginator.get_page(page_number)

    # Filtro para bitácoras (movimiento o fecha)
    search_query2 = request.GET.get('filter2', '').strip()
    if search_query2:
        bitacora_list = bitacora_list.filter(
            Q(movimiento__icontains=search_query2) |
            Q(fecha__icontains=search_query2)
        )

    # Paginador para bitácoras, 5 por página
    paginator2 = Paginator(bitacora_list, 3)
    page_number2 = request.GET.get('page2')
    bitacoras = paginator2.get_page(page_number2)

    context = {
        'profiles': profiles,
        'bitacoras': bitacoras,
        'search_query': search_query,
        'search_query2': search_query2,
    }

    return render(request, 'tables.html', context)


def profile(request):
    profile = Profile.objects.last()  # Último perfil creado

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            new_profile = form.save()

            messages.success(request, f'Se guardó el perfil {new_profile.name}')

            # Registrar en bitácora
            Bitacora.objects.create(
                movimiento=f"Se creó o actualizó el perfil: {new_profile.name} con teléfono {new_profile.phone}"
            )
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_profile = form.save()
            messages.success(request, f'Perfil {new_profile.name} creado correctamente.')
            return redirect('tables')
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})

def edit_profile(request, id):
    profile = get_object_or_404(Profile, id=id)
    # Obtener el perfil relacionado al usuario

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save()

            # Registro en la bitácora
            Bitacora.objects.create(
                movimiento=f'Se actualizó el perfil: {profile.name} con teléfono {profile.phone}',
                fecha=datetime.now()
            )

            messages.success(request, f'Perfil {profile.name} actualizado correctamente.')
            return redirect('tables')  # Cambia 'tables' por la URL o nombre correcto
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})


def delete_profile(request, id):
    profile = get_object_or_404(Profile, pk=id)
    
    if request.method == 'POST':
        profile.delete()
        messages.success(request, 'Perfil eliminado correctamente.')
        return redirect('tables')

    return render(request, 'confirm_delete.html', {'profile': profile})

def signin(request):
    return render(request, 'sign-in.html')


def signup(request):
    return render(request, 'sign-up.html')


def export_profiles_xlsx(request):
    profiles = Profile.objects.all()

    # Crear libro y hoja
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Profiles"

    # Cabeceras
    ws.append(["ID", "Username", "Name", "Phone", "Email", "Photo"])

    # Datos
    for p in profiles:
        ws.append([p.id, p.username, p.name, p.phone, p.email, p.photo.url if p.photo else ""])

    # Preparar respuesta HTTP para descarga
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=profiles.xlsx'
    wb.save(response)
    return response


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