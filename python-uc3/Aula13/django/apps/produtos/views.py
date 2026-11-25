from django.views.generic import ListView
from .models import Categoria, Cliente, Pedido, Produto

class ProdutoListView(ListView):
    # 'model': Informa ao Django qual tabela do banco de dados sera consultada

    model = Produto
    template_name = "produtos/lista_produtos.html"

    context_object_name = "produtos"

    queryset = Produto.objects.select_related("categoria")

class CategoriaListView(ListView):
      
    model = Categoria
    template_name = "produtos/lista_categoria.html"
    
    context_object_name = "categorias"
    
    # queryset = Produto.objects.select_related("categoria")

class ClienteListView(ListView):
      
    model = Cliente
    template_name = "produtos/lista_cliente.html"
    
    context_object_name = "clientes"
    
    # queryset = Produto.objects.select_related("categoria")

