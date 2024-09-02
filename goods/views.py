from itertools import product
from typing import Any
from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.db.models.base import Model as Model
from django.http import Http404
from django.shortcuts import get_list_or_404, render
from django.views.generic import DetailView, ListView

from goods.utils import q_search
from main.models import Components

class CatalogView(ListView):
    model=Components
    #queryset=Components.objects.all().order_by("id")
    template_name="goods/catalog.html"
    context_object_name="goods"
    paginate_by=3
    allow_empty=False


    def get_queryset(self) -> QuerySet[Any]:
        category_slug=self.kwargs.get("category_slug")
        #page=request.GET.get('page', 1)
        on_sale=self.request.GET.get('on_sale')
        order_by=self.request.GET.get('order_by')
        query=self.request.GET.get('q', None)

        if category_slug == "all":
            goods = super().get_queryset()
        elif query:
            goods=q_search(query)    
        else:
            goods = super().get_queryset().filter(componentProjCategory__slug=category_slug)
            if not goods.exists():
                raise Http404()

        if on_sale:
            goods=goods.filter(discount__gt=0)

        if order_by and order_by!="default":
            goods=goods.order_by(order_by)

        return goods

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']="KINGKOSHA - Каталог"
        context["slug_url"]=self.kwargs.get("category_slug")
        return context
    
class ProductView(DetailView):

    #model=Components
    #slug_field="slug"
    template_name="goods/product.html"
    slug_url_kwarg="product_slug"
    context_object_name="product"

    def get_object(self, queryset=None):
        product=Components.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context["title"]=self.object.name
        return context

# def catalog(request, category_slug=None):
#     page=request.GET.get('page', 1)
#     on_sale=request.GET.get('on_sale', None)
#     order_by=request.GET.get('order_by', None)
#     query=request.GET.get('q', None)

#     if category_slug == "all":
#         goods = Components.objects.all()
#     elif query:
#         goods=q_search(query)    
#     else:
#         goods = get_list_or_404(Components.objects.filter(componentProjCategory__slug=category_slug))

#     if on_sale:
#         goods=goods.filter(discount__gt=0)

#     if order_by and order_by!="default":
#         goods=goods.order_by(order_by)

#     paginator = Paginator(goods, 3)
#     current_page=paginator.page(int(page))

#     context: dict[str, str] = {
#         "title": "KINGKOSHA - Каталог",
#         "goods": current_page,
#         "slug_url": category_slug,
#     }
#     return render(request, "goods/catalog.html", context)
    

# def product(request, product_slug):

#     product = Components.objects.get(slug=product_slug)

#     context: dict[str, str] = {
#         "product": product,
#     }

#     return render(request, "goods/product.html", context=context)
