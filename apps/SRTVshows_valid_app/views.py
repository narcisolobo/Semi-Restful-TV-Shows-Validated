from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Show

def index(request):
    return redirect('/shows')

def shows(request):
    data = {
        'shows' : Show.objects.all(),
    }
    return render(request, 'SRTVshows_valid_app/index.html', data)

def new(request):
    return render(request, 'SRTVshows_valid_app/add_show.html')

def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        Show.objects.create(title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release-date'],
        description=request.POST['description'])
        messages.success(request, 'Show successfully added.')
        id = str(Show.objects.last().id)
        return redirect('/shows/'+id)

def display(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show' : show
    }
    return render(request, 'SRTVshows_valid_app/display.html', context)

def edit(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show' : show
    }
    return render(request, 'SRTVshows_valid_app/edit_show.html', context)

def update(request, id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+str(id)+'/edit')
    else:
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release-date']
        show.description = request.POST['description']
        show.save()
        context = {
            'show' : show
            }
        messages.success(request, 'Show successfully edited.')
        return redirect('/shows/'+str(show.id), context)

def destroy(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')