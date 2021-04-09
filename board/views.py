from math import ceil

from django.http import HttpResponseRedirect
from django.shortcuts import render

import board.models as boardmodel

LIST_COUNT = 10


def index(request):
    results = boardmodel.findall()
    data = {"board_list": results}
    return render(request, 'board/index.html', data)


    # page = request.GET.get("p")
    # page = 1 if page is None else int(page)
    #
    # print(page)
    #
    # totalcount = models.count()
    #
    # boardlist = models.findall(page, LIST_COUNT)
    #
    # # paging 정보를 계산
    # pagecount = ceil(totalcount / LIST_COUNT)
    #
    # data = {
    #     "boardlist": boardlist,
    #     'pagecount': pagecount,
    #     'pagecount': 3,
    #     'netpage': 7,
    #     'curpage': 2
    # }
    #
    # return render(request, 'board/index.html')

def view(request):
    no = request.GET['no']
    results = boardmodel.findview(no)
    data = {"viewlist": results}
    return render(request, 'board/view.html', data)

def writeform(request):
    return render(request, 'board/writeform.html')

def write(request):
    title = request.POST['title']
    contents = request.POST['contents']
    authuser = request.session.get('authuser')
    user_no = authuser['no']
    boardmodel.insert(title, contents, '0', '1', '1', '0', user_no)  # title, contents, hit, g_no, o_no, depth, user_no
    return HttpResponseRedirect('/board')

def updateform(request):
    return render(request, 'board/updateform.html')

def update(request):
    no = request.POST['no']
    title = request.POST['title']
    contents = request.POST['contents']
    boardmodel.update(title, contents, no)
    return HttpResponseRedirect('/board')


def deleteform(request):
    return render(request, 'board/deleteform.html')

def delete(request):
    no = request.POST.get('no','')

    boardmodel.delete(no)

    return HttpResponseRedirect('/board')

