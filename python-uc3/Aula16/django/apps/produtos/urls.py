##
# App - Produto - urls.py
##
from django.urls import path

# CategoriasListarView, ClientesListarView, PedidosListarView,ProdutosListarView,
from .views import (
    ProdutoListView,
)

app_name = "produtos"

urlpatterns = [
    path("", ProdutoListView.as_view(), name="lista"),
    #path("listar/", ProdutosListarView.as_view(), name="produtos_listar"),
    #path("categorias/", CategoriasListarView.as_view(), name="categorias_listar"),
    #path("clientes/", ClientesListarView.as_view(), name="clientes_listar"),
    #path("pedidos/", PedidosListarView.as_view(), name="pedidos_listar"),
]
