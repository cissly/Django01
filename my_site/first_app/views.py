from django.shortcuts import render
# from django.http.response import HttpResponse,HttpResponseNotFound,Http404, HttpResponseRedirect, HttpResponseRedirectBase
from django.urls import reverse
# Create your views here.

def simple_view(req):
    return render(req, 'first_app/example.html')



# articles = {
#     'sports': 'Sports Page',
#     'finance': 'Finance Page',
#     'politics': 'Politics Page'
# }

# def news_view(req, topic):
#     try:
#         result = articles[topic]
#         return HttpResponse(articles[topic])
#     except:
#         # result = 'No page for that topic!'
#         # return HttpResponseNotFound(result)
#         raise Http404('404 GENERIC ERROR')

# def add_view(req, num1, num2):
#     result = num1 +num2
#     return HttpResponse(str(result))


# def num_page_view(req, num_page):
#     topics_list = list(articles.keys())
#     topic = topics_list[num_page]

#     #webpage = reverse('topic-page',args=[topic])
#     return HttpResponseRedirect(reverse('topic-page',args=[topic]))