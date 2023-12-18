from django.shortcuts import render, get_object_or_404
from .models import Project
# Create your views here.
def project_list(request):
    return render(request, 'minhaeiro/project-list.html')

def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    expense_list = project.expenses.all()
    return render(request, 'minhaeiro/project-details.html', {'project': project, 'expense_list': expense_list})
