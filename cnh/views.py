from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files import File
from cnh.models import CalvinTbl
from datetime import datetime, timedelta
from cnh.modules import extract


def CalvinView(request):
    d = datetime.today() - timedelta(days=1)
    cf = d.strftime("%Y-%m-%d")
    td = d.strftime("%Y/%m/%d")
    cpic = "cal-{}.gif".format(cf)
    url = "https://www.gocomics.com/calvinandhobbes/{}".format(td)

    cal_latest = CalvinTbl.objects.last()
    if ((not cal_latest) or (cal_latest.published_date.strftime("%Y-%m-%d") != cf)):
        cal_dict = extract.get_calvin(url)

        cal_latest = CalvinTbl()
        cal_latest.title = cpic
        # cal_latest.cnhImgUrl = cont
        cal_latest.cnhImgUrl = cal_dict["url"]
        cal_latest.cnhImg.save(cpic, File(cal_dict["img_temp"]))
        # cal_latest.cnhImgUrl = cal_latest.cnhImg.url
        cal_latest.published_date = cf
        cal_latest.save()

    cal_all = CalvinTbl.objects.all().order_by('published_date')
    return render(request, 'calvin.html', {'cal_all' : cal_all})

