from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from blog.models import Category, Article
from mainapp.forms import RegisterForm
from django.core.paginator import Paginator
import sqlite3

#conexon
conexion = sqlite3.connect('db.sqlite3', check_same_thread=False)


#crear el cursor
cursor = conexion.cursor()

# Create your views here.
def index(request):

    articles = Article.objects.all()
    #paginar los articulos
    paginator = Paginator(articles, 2)

    #obtener el numero de la pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'mainapp/index.html',{
        'title': 'Inicio',
        'articles': page_articles
    })

def register_page(request):

    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            objeto = register_form.save()
            
            idr = str(objeto.id)

            cursor.execute("INSERT INTO auth_user_groups (user_id, group_id)VALUES ("+idr+", 1);")
            conexion.commit()

            return redirect('/admin')

    return render(request, 'users/register.html',{
        'title': 'Registro',
        'register_form': register_form
    })
