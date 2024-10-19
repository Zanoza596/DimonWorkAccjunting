from django.urls import path

from goods import views

app_name='goods'

urlpatterns = [
    # #Для Postgre
    # path('search/',views.CatalogView.as_view(),name='search'),
    # path('<slug:category_slug>/',views.CatalogView.as_view(),name='index'),
    # path('product/<slug:product_slug>/',views.ProductView.as_view(),name='product'),
    # Для SQLite
    path('search/',views.catalog,name='search'),
    path('<slug:category_slug>/',views.catalog,name='index'),
    path('product/<slug:product_slug>/',views.product,name='product'),

]


