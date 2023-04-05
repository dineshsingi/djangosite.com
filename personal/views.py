from django.shortcuts import render
from blog.views import get_blog_queryset
# from personal.models import Question
# from account.models import Account
# python's standard library "attrgetter
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from blog.models import BlogPost

BLOG_POSTS_PER_PAGE = 10


def home_screen_view(request):
    context = {}

    query = ""
    query = request.GET.get('q', '')
    context['query'] = str(query)
    print("home_screen_view: " + str(query))

    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)

    # Pagination
    page = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)

    try:
        blog_posts = blog_posts_paginator.page(page)
    except PageNotAnInteger:
        blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

    context['blog_posts'] = blog_posts

    return render(request, "personal/home.html", context)


# Creating home screen for user account
#
# def home_screen_view(request):
#     context = {}
#     users = Account.objects.all()
#     context['users'] = users
#
#     return render(request, 'personal/home.html', context)


#Creating home screen for model question
# def home_screen_view(request):
#     context = {}
#     # context['some_string'] = "This is the passing string to the view"
#     # context['some_number'] = "DOB: 10-02-2000"
#     # context = {
#     #     'some_string': "This is the passing string to the view",
#     #     'some_number': "DOB: 10-02-2000",
#     # }
#
#     # list_of_values = []
#     # list_of_values.append('first entry')
#     # list_of_values.append('second entry')
#     # list_of_values.append('third entry')
#     # list_of_values.append('fourth entry')
#     # list_of_values.append('fifth entry')
#
#     questions = Question.objects.all()
#     context['questions'] = questions
#
#     return render(request, 'personal/home.html', context)


#Next create the user register without admin console