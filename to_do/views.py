from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.
def get_to_do_list(request):
    results=Item.objects.all()
    return render(request, "to_do_list.html", {'items': results})
    
def create_an_item(request):
    if request.method == "POST":
        #create new form
        form = ItemForm(request.POST, request.FILES)
        #django checks if form is valid and saves if so
        if form.is_valid():
            form.save()
            return redirect(get_to_do_list)
    #if not a post request return an empty form
    else:
        form = ItemForm()

    return render(request, "item_form.html", {'form': form})
#get item where primary key = id
def edit_an_item(request, id):
    item = get_object_or_404(Item, pk=id)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_to_do_list)
    else:
        #item is the instance that we wan to construct the object from
        form = ItemForm(instance=item)
    return render(request, "item_form.html", {'form': form})


def toggle_status(request, id):
    item = get_object_or_404(Item, pk=id)
    item.done = not item.done
    item.save()
    return redirect(get_to_do_list)
