from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Student

def student_list(request):
    search_query=request.GET.get('q','')
    if search_query:
        students=Student.objects.filter(name_icontains=search_query)

    else:
        students=Student.objects.all()

    paginator=Paginator(students,5)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)

    return render(request,'students/student_list.html',{
        'page_obj':page_obj,
        'search_query':search_query,

    })





