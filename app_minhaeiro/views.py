from django.shortcuts import render

# Create your views here.
def project_list(request):
    return render(request, 'minhaeiro/project-list.html')

def project_detail(request, project_slug):
    return render(request, 'minhaeiro/project-details.html')