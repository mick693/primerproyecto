from django.shortcuts import render
from django.utils import timezone
from .models import Post

def listar_publicacion(request):
    publi=Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request,'blog/listar_publicacion.html',{'publi':publi})
# Create your views here.
