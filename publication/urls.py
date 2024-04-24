from django.urls import path
from .views import indexView, projectsList, privacyList, termsList, publicationDetail, projectDetail

urlpatterns = [
    path('', indexView, name='index'),
    path('projects', projectsList, name='projectsList'),
    path('project<int:id>', projectDetail, name='project-detail'),
    path('privacy', privacyList, name='privacyList'),
    path('terms', termsList, name='termsList'),
    path('publication-detail', publicationDetail, name='publication-detail')
]