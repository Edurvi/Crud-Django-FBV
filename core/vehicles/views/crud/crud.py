from django.shortcuts import render, redirect, get_object_or_404
from core.vehicles.models import Category

def crudList(request):
    template_name = 'crud/crud.html'
    data = Category.objects.all()
    text = 'Crud Categorias'
    return render(request, template_name, {'data':data, 'text':text})

def categoryCreate(request):
    category = Category()
    category.name = request.POST['name']
    category.description = request.POST['description']
    category.save()
    return redirect('crud_list')

def categoryDelete(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return redirect('crud_list')
def categoryUpdate(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category.name = name
        category.description = description
        category.save()
        return redirect('crud_list')
    return render(request, 'crud/edit.html', {'category':category})