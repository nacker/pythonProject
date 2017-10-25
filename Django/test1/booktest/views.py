from django.shortcuts import render
from django.http import *
from .models import *
# from django.template import RequestContext,loader

# Create your views here.
def index(request):
    # return HttpResponse('hello')

    # temp=loader.get_template('booktest/index.html')
    # return HttpResponse(temp.render())

    bookList = BookInfo.objects.all()
    context = {'list': bookList}
    return render(request, 'booktest/index.html',context)

def show(request,id):
    book = BookInfo.objects.get(pk=id)
    heroList = book.heroinfo_set.all()
    context = {'list': heroList}
    return render(request,'booktest/show.html',context)