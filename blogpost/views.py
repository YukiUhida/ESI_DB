from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import BlogModel ,ESIComModel ,question_Model
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.db import connection
from .forms import MyForm
import pandas as pd
import os
from django.conf import settings
import numpy as np
from sqlalchemy import create_engine
import rdkit
from rdkit.Chem import Descriptors
from .rdkit_descriptor import Rdescriptor
from .esi_descriptor import Edescriptor
from .hello import hello

# Create your views here.

class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel

class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel

class BlogCreate(CreateView):
    template_name = 'contact_form.html'
    model = question_Model
    fields = ('question_title','question','public_permission','email_adress')
    success_url = reverse_lazy('past_question')

class BlogDelete(DeleteView):
    template_name = 'delete.html'
    model = BlogModel
    success_url = reverse_lazy('list')


class BlogUpdate(UpdateView):
    template_name = 'update.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')

class Com(ListView):
    template_name = 'com.html'
    model = ESIComModel

class ComDetail(DetailView):
    template_name = 'comdetail.html'
    model = ESIComModel


def download_csv(request):
    # ファイルのパスを指定
    file_path = 'qwerty.csv'
    # ファイルオブジェクトを取得
    file = open(file_path, 'rb')
    # FileResponseを作成して返す
    response = FileResponse(file)
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    return response



def my_view(request):
    # SQLクエリの実行
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM blogpost_esicommodel WHERE molecular_weight >= 1400", [1400])
        results = cursor.fetchall()

    # 結果をビューに渡す
    context = {'results': results}
    return render(request, 'com_sql.html', context)


def my_forms(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if forms.is_valid():
            my_variable = form.cleaned_data['my_variable']
            # 変数my_variableを使って必要な処理を行う
            # ...
    else:
        form = MyForm()

    context = {'form': form}
    return render(request, 'form.html', context)


#5/22
def upload_form(request):
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]  # フォームからCSVファイルを取得

        # ファイルをサーバ側に保存
        with open("submit/file.csv", "wb") as file:
            for chunk in csv_file.chunks():
                file.write(chunk)

        # 成功メッセージを表示するなど、適切な処理を行う

    return render(request, "upload_form.html")





#5/23作成　6/2最終更新

def view_rdkit(request):
    
    
    # CSVファイルのパスを指定
    #csv_path = os.path.join(settings.BASE_DIR, 'rdkit_desc.csv')
    # CSVファイルをPandasのデータフレームとして読み込み
    #df = pd.read_csv(csv_path)
    df=Rdescriptor()
    # データフレームをビューに渡す
    context = {'dataframe': df}
    return render(request, 'rdkit_view.html', context)



#6/5 6/16更新
#def upload_rdkit(request):
#    if request.method == "POST":
#        csv_file = request.FILES["csv_file"]  # フォームからCSVファイルを取得
#
#        # ファイルをサーバ側に保存
#        with open("rdkit/smiles.csv", "wb") as file:
#            for chunk in csv_file.chunks():
#                file.write(chunk)
#
#        # 成功メッセージを表示するなど、適切な処理を行う
#
#    return render(request, "upload_rdkit_form.html")

def upload_rdkit(request):
    file_uploaded = False
    csv_file_extension = None

    if request.method == 'POST' and 'csv_file' in request.FILES:
        csv_file = request.FILES['csv_file']
        
        if csv_file:
            # ファイルが提出されている場合の処理
            file_uploaded = True
            
            # ファイル名の拡張子を取得
            csv_file_extension = csv_file.name.split('.')[-1].lower()

            # 拡張子が 'csv' であるかどうかをチェック
            if csv_file_extension != 'csv':
                file_uploaded = False

            # ファイルをサーバ側に保存
            file_path = os.path.join('rdkit', 'smiles.csv')
            with open(file_path, 'wb+') as file:
                for chunk in csv_file.chunks():
                    file.write(chunk)

    context = {
        'file_uploaded': file_uploaded,
        'csv_file_extension': csv_file_extension
    }

    return render(request, 'upload_rdkit_form.html', context)




def hello_view(request):
    result = hello()  # .pyファイルの関数を呼び出す
    return render(request, 'hello.html', {'result': result})


def rdkit_descriptor(request):
    rdkit_desc = Rdescriptor()  # .pyファイルの関数を呼び出す
    request.session['rdkit_desc'] = rdkit_desc.to_dict()  # 結果をセッションに保管
    return render(request, 'rdkit_view.html')

def download_rdkit_descriptor(request):
    # ファイルのパスを指定
    file_path1 = 'rdkit_to_user/rdkit_descriptor.csv'
    # ファイルオブジェクトを取得
    file1 = open(file_path1, 'rb')
    # FileResponseを作成して返す
    response = FileResponse(file1)
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    return response

#6/6　6/16更新

def upload_esi(request):
    file_uploaded = False
    csv_file_extension = None

    if request.method == 'POST' and 'csv_file' in request.FILES:
        csv_file = request.FILES['csv_file']
        
        if csv_file:
            # ファイルが提出されている場合の処理
            file_uploaded = True
            
            # ファイル名の拡張子を取得
            csv_file_extension = csv_file.name.split('.')[-1].lower()

            # 拡張子が 'csv' であるかどうかをチェック
            if csv_file_extension != 'csv':
                file_uploaded = False

            # ファイルをサーバ側に保存
            file_path = os.path.join('esi', 'smiles.csv')
            with open(file_path, 'wb+') as file:
                for chunk in csv_file.chunks():
                    file.write(chunk)

    context = {
        'file_uploaded': file_uploaded,
        'csv_file_extension': csv_file_extension
    }

    return render(request, 'upload_esi_form.html', context)



def esi_descriptor(request):
    esi = Edescriptor()  # .pyファイルの関数を呼び出す
    request.session['esi'] = esi.to_dict()  # 結果をセッションに保管
    return render(request, 'esi_view.html')

def download_esi_descriptor(request):
    # ファイルのパスを指定
    file_path2 = 'ESI_to_user/esi_descriptor.csv'
    # ファイルオブジェクトを取得
    file2 = open(file_path2, 'rb')
    # FileResponseを作成して返す
    response = FileResponse(file2)
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    return response

def view_esi(request):
    
    
    # CSVファイルのパスを指定
    #csv_path = os.path.join(settings.BASE_DIR, 'rdkit_desc.csv')
    # CSVファイルをPandasのデータフレームとして読み込み
    #df = pd.read_csv(csv_path)
    df=Edescriptor()
    # データフレームをビューに渡す
    context = {'dataframe': df}
    return render(request, 'esi_view.html', context)

#6/8
def top_view(request):
    result="top"
    return render(request, 'top.html', {'result': result})

#6/12
def what_esi(request):
    result="what_esi"
    return render(request, 'what_esi.html', {'result': result})

def definition_esi(request):
    result="definition_esi"
    return render(request, 'definition_esi.html', {'result': result})


def esi_research(request):
    result="definition_esi"
    return render(request, 'esi_research.html', {'result': result})
##aaaaaa
def contact_form(request):
    result="contact_form"
    return render(request, 'contact_form.html', {'result': result})

def link_esi(request):
    result="link_esi"
    return render(request, 'link_esi.html', {'result': result})

def provide(request):
    result="provide"
    return render(request, 'provide.html', {'result': result})


#6/14


class QuestionList(ListView):
    template_name = 'contact_form.html'
    model = question_Model



#6/16

def past_question(request):
    questions = question_Model.objects.filter(public_permission='approval', question_situation='answered')
    return render(request, 'past_question.html', {'questions': questions})

class question_detail(DetailView):
    template_name = 'question_detail.html'
    model = question_Model
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # 条件に合致するデータのみをフィルタリング
        queryset = queryset.filter(public_permission='approval', question_situation='answered')
        return queryset
 