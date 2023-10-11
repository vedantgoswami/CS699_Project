from django.shortcuts import get_object_or_404,render
from django.views.generic import ListView
from django.http import JsonResponse

from .models import Item

# Create your views here.
class HomeView(ListView):
    model = Item
    template_name = "description/index.html"
    context_object_name = "items"
    paginate_by = 10
    def get_template_names(self):
        if self.request.htmx:
            return 'description/components/item-list-elements.html'
        return "description/index.html"

def item_single(request, item):
    item = get_object_or_404(Item, name=item)
    return render(request, "description/single.html",{"item":item})


def get_names(request):
    search = request.GET.get('search')
    payload = []
    if search:
        objs = Item.objects.filter(name__icontains=search)
        for obj in objs:
            payload.append({
                'name': obj.name
            })
    return JsonResponse({
        'status': True,
        'payload': payload
    })
