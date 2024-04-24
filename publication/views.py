from django.shortcuts import render
from .models import Projects
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

def indexView(request):
    projects = Projects.objects.all()[:3]

    context = {
        "projects": projects
    }

    return render(request, "index.html", context=context)

def projectDetail(request, id):
    project = get_object_or_404(Projects, pk=id)
    project.views = project.views + 1
    project.save()

    context = {
        "project": project
    }

    return render(request, "publication-detail.html", context)

def projectsList(request):

    projects = Projects.objects.all()
    paginator = Paginator(projects, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "pages_obj": page_obj
    }
    return render(request, 'project.html', context)

def privacyList(request):
    return render(request, 'privacy.html', context={})

def termsList(request):
    return render(request, 'terms.html', context={})

def publicationDetail(request):
    return render(request, 'publication-detail.html', context={})