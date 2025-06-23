from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.db.models import Q 
from django.core.paginator import Paginator
from .models import Tasks

@login_required
def tasks(request):
    profile = request.user.profile_set.first()
    tasks_list =Tasks.objects.filter(profile=profile).order_by('nombre')

    search_query = request.GET.get('filter', '')

    if search_query:
        tasks_list = tasks_list.filter(
            Q(nombre__icontains=search_query) | Q(descripcion__icontains=search_query)
        )

    # Paginador
    paginator = Paginator(tasks_list, 3)  # 3 tareas por página
    page_number = request.GET.get('page')
    tasks_paginated = paginator.get_page(page_number)

    context = {
        'tasks': tasks_paginated
    }
    return render(request, 'tasks.html', context)
