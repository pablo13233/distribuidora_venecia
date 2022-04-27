from apps.categoria.models import *

def categoria_list(request):
    categorias = Categoria.objects.all()
    
    return {'ctx_categorias':categorias}