from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.views.decorators.csrf import ensure_csrf_cookie
from store.models import Book, Category, Writer

@ensure_csrf_cookie
def search(request):
	search = request.GET.get('q')
	books = Book.objects.all()
	if search:
		books = books.filter(
			Q(name__icontains=search)|Q(category__name__icontains=search)|Q(writer__name__icontains=search)

		)

	paginator = Paginator(books, 10)
	page = request.GET.get('page')
	books = paginator.get_page(page)

	context = {
		"book": books,
		"search": search,
	}
	return render(request, 'store/category.html', context)
