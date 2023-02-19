from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem


def listView(request):
    all_lists = TodoItem.objects.all()
    return render(request, 'index.html', {'lists': all_lists})


def listadd(request):
    new_list = TodoItem(content=request.POST['content'])
    new_list.save()
    return HttpResponseRedirect('/listView')


def deletelist(request, list_id):
    item_del = TodoItem.objects.get(id=list_id)
    item_del.delete()
    return HttpResponseRedirect('/listView')
