from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Project

# Create your views here.

def tes(request):
    return render(request, "project/tes.html")

def project_detail(request, slug):

    project = get_object_or_404(
        Project,
        slug=slug
    )

    return render(
        request,
        "portfolio/project_detail.html",
        {
            "project": project
        }
    )