from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from blog.models import Category, Article
from mainapp.forms import RegisterForm
from django.core.paginator import Paginator
import sqlite3
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#conexon
conexion = sqlite3.connect('db.sqlite3', check_same_thread=False)


#crear el cursor
cursor = conexion.cursor()

# Create your views here.
def index(request):
    #para el buscador
    queryset = request.GET.get("buscar")

    articles = Article.objects.filter(public=True)

    if queryset:

        query = Q(title__icontains = queryset)
        query.add(Q(content__icontains = queryset), Q.OR)
        query.add(Q(public=True), Q.AND)

        articles = Article.objects.filter(query)

    #paginar los articulos
    paginator = Paginator(articles, 3)

    #obtener el numero de la pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'mainapp/index.html',{
        'title': 'Inicio',
        'articles': page_articles
    })

def register_page(request):
    #con esta condición verificamos si ha ininiciado sesion para no mostrar la pagina de registro
    if request.user.is_authenticated:
        return redirect('index')
    else:
        register_form = RegisterForm()

        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                objeto = register_form.save()
                
                #idr = str(objeto.id)

                #cursor.execute("INSERT INTO auth_user_groups (user_id, group_id)VALUES ("+idr+", 1);")
                #conexion.commit()
                
                #mensaje de registro exitoso
                messages.success(request, 'Te has registrado correctamente!! Ahora puedes acceder a contenido especial en el blog')

                return redirect('index')

    return render(request, 'users/register.html',{
        'title': 'Registro',
        'register_form': register_form
    })


def login_page(request):

    if request.user.is_authenticated:
        return redirect('index')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.warning(request, 'No te has podido identificar')

    return render(request, 'users/login.html',{
        'title': 'Iniciar sesión'
    })

def logout_user(request):
    logout(request)
    return redirect('login')
