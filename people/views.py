from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from . import models, forms

def people_list(request):
    people = models.Person.objects.all().order_by('name')
    print(request.GET.get('search'))
    if request.GET.get('search') is not None:
        people = people.filter(name__icontains=request.GET.get('search'))

    return render(request, 'people_list.html', {'people': people})

def people_new(request):
    new_form = forms.PersonModelForm()
    if request.method == 'POST':
        new_form = forms.PersonModelForm(request.POST, request.FILES)
        if new_form.is_valid():
            new_form.save()
            return redirect('people_list')
    
    return render(request, "people_new.html", {'form': new_form})

def people_edit(request, id):
    person = get_object_or_404(models.Person, id=id)
    edit_form = forms.PersonModelForm(instance=person)
    if request.method == 'POST':
        if request.FILES:
            edit_form = forms.PersonModelForm(request.POST, request.FILES, instance=person)
        else:
            edit_form = forms.PersonModelForm(request.POST, instance=person)        

        if edit_form.is_valid():
            edit_form.save()
            return redirect('people_list')

    return render(request, 'people_edit.html', {'form': edit_form}) 

def people_delete(request, id):
    person = get_object_or_404(models.Person, id=id)
    if request.method == 'POST':
        person.delete()
        return redirect('people_list')
    return render(request, 'people_delete.html') 