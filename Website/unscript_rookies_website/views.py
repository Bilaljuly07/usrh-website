from django.shortcuts import render
from .models import Sponsors
from operator import itemgetter
from itertools import groupby
# Create your views here.

def index(request):

    Te= Sponsors.objects.filter(types__iexact = "Title")

    At = Sponsors.objects.filter(types__iexact = "Asstitle")

    Pt = Sponsors.objects.filter(types__iexact = "Platinum")

    Gd = Sponsors.objects.filter(types__iexact = "Gold")
    
    Kp = Sponsors.objects.filter(types__iexact = "Knowledge")

    Ik = Sponsors.objects.filter(types__iexact = "In_Kind")

    Mp = Sponsors.objects.filter(types__iexact = "Media")

    Cp =Sponsors.objects.filter(types__iexact = "Community")

    Tc = Sponsors.objects.filter(types__iexact = "Technology")

    Sp = Sponsors.objects.filter(types__iexact = "Streaming")

    Tp = Sponsors.objects.filter(types__iexact = "Travel")

    Fd = Sponsors.objects.filter(types__iexact = "Food")

    dic = {'Title': Te, 'Asstitle': At, 'Platinum': Pt, 'Gold': Gd, 'Knowledge': Kp, 'In_Kind': Ik, 'Media': Mp, 'Community': Cp, 'Technology': Tc, 'Streaming': Sp, 'Travel': Tp, 'Food': Fd, }
    Te1 = len(dic['Title'])
    At1 = len(dic['Asstitle'])
    Pt1 = len(dic['Platinum'])
    Gd1 = len(dic['Gold'])
    Kp1 = len(dic['Knowledge'])
    Ik1 = len(dic['In_Kind'])
    Mp1 = len(dic['Media'])
    Cp1 = len(dic['Community'])
    Tc1 = len(dic['Technology'])
    Sp1 = len(dic['Streaming'])
    Tp1 = len(dic['Travel'])
    Fd1 = len(dic['Food'])

    return render(request, 'index.html', {'Title': Te, 'Asstitle': At, 'Platinum': Pt, 'Gold': Gd, 'Knowledge': Kp, 'In_Kind': Ik, 'Media': Mp, 'Community': Cp, 'Technology': Tc, 'Streaming': Sp, 'Travel': Tp, 'Food': Fd, 'Title1': Te1, 'Asstitle1': At1, 'Platinum1': Pt1, 'Gold1': Gd1, 'Knowledge1': Kp1, 'In_Kind1': Ik1, 'Media1': Mp1, 'Community1': Cp1, 'Technology1': Tc1, 'Streaming1': Sp1, 'Travel1': Tp1, 'Food1': Fd1})