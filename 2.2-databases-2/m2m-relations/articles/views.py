from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.order_by(ordering).all()
    data = []

    for article in articles:
        scopes = article.scopes.all()
        print(scopes)
        gl_tag = None
        tags = []
        for scope in scopes:
            if scope.is_main:
                gl_tag = scope.tag.name
            else:
                tags.append(scope.tag.name)
        print(gl_tag)
        print(tags)
        result_tags = tags.append(gl_tag)
        data.append({
            'title': article.title,
            'text': article.text,
            'published_at': article.published_at,
            'image': article.image,
            'scopes': {'tag': {'name': gl_tag}}
        })
        print(result_tags)
        # gl_tag = article.scopes.filter(is_main=True)
        # print(gl_tag)
        # os_tag = article.scopes.filter(is_main=False).order_by()
        # print(os_tag)
        # data.append({
        #     'title': article.title,
        #     'text': article.text,
        #     'published_at': article.published_at,
        #     'image': article.image,
        #     'tag': gl_tag + os_tag
        # })
        # scopes = article.scopes.all()
        # for scope in scopes:
        #     if scope.is_main:
        #         gl_tag = scope.tag.name
        # tags_list = sorted([scope.tag.name for scope in scopes])
        # print(tags_list)
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
    context = {'object_list': articles}


    # # используйте этот параметр для упорядочивания результатов
    # # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = '-published_at'

    return render(request, template, context)
