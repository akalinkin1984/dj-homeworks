from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    object_list = Article.objects.all().order_by(ordering)

    for article in object_list:
        scopes = article.scopes.all()
        for scope in scopes:
            if scope.is_main:
                gl_tag = scope.tag.name
        tags_list = sorted([scope.tag.name for scope in scopes])
        print(tags_list)
        # for scope in scopes:
        # #     print(scope.tag, scope.is_main)
        # # print('____________')
        #     scope.order_by(scope.tag)
        # tag_list = []
        # for tag in article.scopes.all():
        #     if tag.get('is_main'):
        # #         tag_list.append(tag)
        #         print('1')
        # print(article.scopes)
        # print(article.scopes.all())
    context = {'object_list': object_list}

    # # используйте этот параметр для упорядочивания результатов
    # # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = '-published_at'

    return render(request, template, context)
