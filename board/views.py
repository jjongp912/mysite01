from math import ceil

from django.shortcuts import render

from board import models

LIST_COUNT = 10


def index(request):
    results = models.findall()
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

    return render(request, 'board/view.html')

def writeform(request):
    return render(request, 'board/writeform.html')

def updateform(request):
    return render(request, 'board/updateform.html')

