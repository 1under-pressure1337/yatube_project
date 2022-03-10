from django.http import HttpResponse

# Create your views here.

# Главная страница


def index(request):
    return HttpResponse('Главная страница')


# Страница с постами, отфильтрованными по группе
def group_posts(request, any_slug):
    return HttpResponse('Список постов')
