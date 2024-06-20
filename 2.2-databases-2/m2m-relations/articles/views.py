from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.order_by(ordering)
    data = []

    for article in articles:
        scopes = article.scopes.order_by('-is_main', 'tag__name')

        data.append(
            {
            'title': article.title,
            'text': article.text,
            'published_at': article.published_at,
            'image': article.image,
            'scopes': scopes
            }
                )

    context = {'object_list': data}

    return render(request, template, context)
