from django.contrib import admin
from django.urls import path
from .views import BlogList, BlogDetail, BlogCreate, BlogDelete, BlogUpdate, Com, ComDetail ,download_csv, my_view, my_forms,view_esi, upload_form, upload_rdkit, hello_view, rdkit_descriptor, download_rdkit_descriptor, upload_esi,esi_descriptor, download_esi_descriptor, top_view,what_esi,definition_esi,esi_research,contact_form,link_esi,provide,view_rdkit,past_question,question_detail
from . import views






urlpatterns = [
    path('admin/', admin.site.urls),
    
]


urlpatterns = [
    path('list/', BlogList.as_view(), name='list'),
    path('detail/<int:pk>/',BlogDetail.as_view(), name='detail'),
    path('create/',BlogCreate.as_view(), name='create'),
    path('delete/<int:pk>', BlogDelete.as_view(), name='delete'),
    path('update/<int:pk>', BlogUpdate.as_view(), name='update'),
    path('com/', Com.as_view(), name='com'),
    path('comdetail/<int:pk>/', ComDetail.as_view(), name='comdetail'),
    path('download/', download_csv, name='download_csv'),
    path('com_sql/', my_view, name='com_sql'),
    path('form/', my_forms, name='my_forms'),
    path('view_rdkit/', view_rdkit, name='view_rdkit'),
    path('upload/', upload_form, name="upload_form"),
    path('upload_rdkit/', upload_rdkit, name="upload_rdkit"),
    path('hello/', hello_view, name='hello'),
    path('rdkit_descriptor/', rdkit_descriptor, name='rdkit_descriptor'),
    path('download_rdkit_descriptor/', download_rdkit_descriptor, name='download_rdkit_descriptor'),
    path('upload_esi/', upload_esi, name="upload_esi"),
    path('esi_descriptor/', esi_descriptor, name='esi_descriptor'),
    path('download_esi_descriptor/', download_esi_descriptor, name='download_esi_descriptor'),
    path('view_esi/', view_esi, name='view_esi'),
    path('top/', top_view, name='top'),
    path('what_esi/', what_esi, name='what_esi'),
    path('definition_esi/', definition_esi, name='definition_esi'),
    path('esi_research/', esi_research, name='esi_research'),
   # path('contact_form/', contact_form, name='contact_form'),
    path('contact_form/', BlogCreate.as_view(), name='contact_form'),
    path('link_esi/', link_esi, name='link_esi'),
    path('provide/', provide, name='provide'),
    path('past_question', past_question, name='past_question'),
    path('question_deatail/<int:pk>/', question_detail.as_view(), name='question_detail'),
   

]

