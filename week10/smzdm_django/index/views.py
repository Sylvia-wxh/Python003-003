from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from .models import Shampoo

# Create your views here.
def home (request):
    pass

# 输出洗护发产品评论到模板
def shampoo_comment(request):
    #condtions = {'stars__gt': 3}
    n = Shampoo.objects.all()
    #comments = n.comment_text[0]
    return render(request, 'index.html', locals())

# 输出查询按钮的数据到模板上面
def search(request):
    q = request.GET.get('q')
    print(q)
    error_msg = ''

    if not q or q =='':
         error_msg = '请输入关键词'
         return render(request, 'errors.html', {'error_msg': error_msg})
    n = comment.objects.filter(comment_text__icontains=q)
    return render(request, 'index.html',locals())