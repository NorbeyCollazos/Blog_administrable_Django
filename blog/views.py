from django.shortcuts import render, redirect
from blog.models import Category, Article, Coment
from django.core.paginator import Paginator


# Create your views here.
def list(request):

    articles = Article.objects.all()

    #paginar los articulos
    paginator = Paginator(articles, 2)

    #obtener el numero de la pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'articles/list.html',{
        'title': 'Artículos',
        'articles': page_articles
    })

def category(request, category_id):

    category = Category.objects.get(id=category_id)
    articles = Article.objects.filter(categories=category_id)

    return render(request, 'categories/category.html',{
        'category': category,
        'articles': articles
    })


def article(request, article_id):

    article = Article.objects.get(id=article_id)
    comentarios = Coment.objects.filter(article=article_id)

    return render(request, 'articles/detail.html',{
        'article_id': article_id,
        'article': article,
        'comentarios': comentarios
    })

def guardar_comentario(request, article_id):

    if request.method == "POST":
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        comentario = request.POST['comentario']

        pagina_actual = request.POST['pagina_actual']

        comentario = Coment(
            nombre= nombre,
            email=correo,
            coment=comentario,
            article_id=article_id
        )

        comentario.save()

        return redirect(pagina_actual)
