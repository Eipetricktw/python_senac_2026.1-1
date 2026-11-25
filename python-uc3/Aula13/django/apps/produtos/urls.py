from django.urls import path

from .views import(

    ProdutoListView,
    CategoriaListView,
    ClienteListView,
)

app_name ="produtos"

urlpatterns =[
    path("", ProdutoListView.as_view(), name = "lista"),
    path("categorias/", CategoriaListView.as_view(), name = "listar_categoria"),
    path("clientes/", ClienteListView.as_view(), name = "listar_cliente"),

]