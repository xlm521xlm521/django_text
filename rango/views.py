from django.shortcuts import render
from rango.models import Page

# Create your views here.
from django.http import HttpResponse
from rango.models import Category

def index(request):
    mycategory=Category.objects.order_by('-likes')[:5]
    mydict={'categories':mycategory}
    return render(request, 'rango/index.html', mydict)
def showpython(request):
    return HttpResponse('hellow python')
def category(request, category_name_slug) :
	context_dict = {}
	try:
		category = Category.objects.get( slug=category_name_slug)
		context_dict['category_name' ] = category.name
		pages = Page.objects.filter( category=category)
		context_dict['pages' ] = pages
		context_dict['category' ] = category
	except Category.DoesNotExist:
		pass
	return render( request, 'rango/category.html' , context_dict)
from rango.forms import CategoryForm

def add_category(request) :
	if request.method == 'POST' :
		form = CategoryForm(request.POST)
		if form. is_valid( ) :
			form.save(commit=True)
			return index(request)
		else:
			print form.errors
	else:
		form = CategoryForm( )
	return render( request, 'rango/add_category.html' , {'form' : form})