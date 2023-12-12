from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Project
from .forms import ProjectForm

# Create your views here.
# Functional based view
# Create a project
# def project_create(request):
#     if request.method == "POST":
#         form = ProjectForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("projects:project_list"))
#     else:
#         form = ProjectForm()
#
#     return render(request, "projects/project_form.html", { "form": form, })
#
#
# # Retrieve project list
# def project_list(request):
#     projects = Project.objects.all()
#     return render(request, "projects/project_list.html", { "projects": projects,})
#
#
# # Retrieve a single project
# def project_detail(request, pk):
#     project = get_object_or_404(Project, pk=pk)
#     return render(request, "projects/project_detail.html", { "project": project, })
#
#
# # Update a single project
# def project_update(request, pk):
#     project_obj = get_object_or_404(Project, pk=pk)
#     if request.method == 'POST':
#         form = ProjectForm(instance=project_obj, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("projects:project_detail", args=[pk,]))
#     else:
#         form = ProjectForm(instance=project_obj)
#
#     return render(request, "projects/project_form.html", { "form": form, "object": project_obj})
#
#
# # Delete a single project
# def project_delete(request, pk):
#     project_obj = get_object_or_404(Project, pk=pk)
#     project_obj.delete()
#     return redirect(reverse("projects:project_list"))

# Class Based Views
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView

class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('projects:project_list')

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('projects:project_list')

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('projects:project_list')
