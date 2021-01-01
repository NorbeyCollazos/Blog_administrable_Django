from pages.models import Page

def get_pages(request):

    pages = Page.objects.filter(visible='0').order_by('order').values_list('id','title','slug')
    pages_users = Page.objects.filter(visible='1').order_by('order').values_list('id','title','slug')

    return {
        'pages': pages,
        'pages_users': pages_users
    }