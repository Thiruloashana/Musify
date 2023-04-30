from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import json

import psycopg2

from .models import users,song


def index(request):
    return render(request, "new1/index.html")
#______________________________________________________________________

def artist(request):
    return render(request, "new1/artist.html")
#______________________________________________________________________

def genre(request):
    return render(request, "new1/genre.html")
#______________________________________________________________________

def mood(request):
    return render(request, "new1/mood.html")
#______________________________________________________________________

def language(request):
    return render(request, "new1/language.html")
#______________________________________________________________________

def movie(request):
    return render(request, "new1/movie.html")
#______________________________________________________________________

def anirudh(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(artistid__exact=1)
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    for i in range (len(l3)):
        if l3[i]==1:
            l3[i]="Anirudh Ravichander"
        elif l3[i]==2:
            l3[i]="A.R.Rahman"
        elif l3[i]==4:
            l3[i]="Ilaiyaraaja"
        elif l3[i]==5:
            l3[i]="Silambarasan TR"
        elif l3[i]==6:
            l3[i]="Vijay"
        elif l3[i]==7:
            l3[i]="Sid Sriram"
    
    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/artistanirudh.html",context1)
#______________________________________________________________________

def rahman(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(artistid__exact=2)
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    for i in range (len(l3)):
        if l3[i]==1:
            l3[i]="Anirudh Ravichander"
        elif l3[i]==2:
            l3[i]="A.R.Rahman"
        elif l3[i]==4:
            l3[i]="Ilaiyaraaja"
        elif l3[i]==5:
            l3[i]="Silambarasan TR"
        elif l3[i]==6:
            l3[i]="Vijay"
        elif l3[i]==7:
            l3[i]="Sid Sriram"

        
    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/artistarrahman.html",context1)
#______________________________________________________________________

def yuvan(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(artistid__exact=7)
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    for i in range (len(l3)):
        if l3[i]==1:
            l3[i]="Anirudh Ravichander"
        elif l3[i]==2:
            l3[i]="A.R.Rahman"
        elif l3[i]==4:
            l3[i]="Ilaiyaraaja"
        elif l3[i]==5:
            l3[i]="Silambarasan TR"
        elif l3[i]==6:
            l3[i]="Vijay"
        elif l3[i]==7:
            l3[i]="Sid Sriram"

        
    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/artistyuvan.html",context1)
#______________________________________________________________________

def raaja(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(artistid__exact=4)
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    
        
    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/artistilaiyaraaja.html",context1)
#______________________________________________________________________

def vijay(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(artistid__exact=6)
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
        
    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/artistvijay.html",context1)
#______________________________________________________________________

def langeng(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(language1__exact="English")
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    for i in range (len(l3)):
        if l3[i]==1:
            l3[i]="Anirudh Ravichander"
        elif l3[i]==2:
            l3[i]="A.R.Rahman"
        elif l3[i]==4:
            l3[i]="Ilaiyaraaja"
        elif l3[i]==5:
            l3[i]="Silambarasan TR"
        elif l3[i]==6:
            l3[i]="Vijay"
        elif l3[i]==7:
            l3[i]="Sid Sriram"

        
    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/languageenglish.html",context1)
#______________________________________________________________________

def langtam(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(language1__exact="Tamil")
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    for i in range (len(l3)):
        if l3[i]==1:
            l3[i]="Anirudh Ravichander"
        elif l3[i]==2:
            l3[i]="A.R.Rahman"
        elif l3[i]==4:
            l3[i]="Ilaiyaraaja"
        elif l3[i]==5:
            l3[i]="Silambarasan TR"
        elif l3[i]==6:
            l3[i]="Vijay"
        elif l3[i]==7:
            l3[i]="Sid Sriram"

        
    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/languagetamil.html",context1)
#______________________________________________________________________

def happy(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(moodid__exact=1)
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    for i in range (len(l3)):
        if l3[i]==1:
            l3[i]="Anirudh Ravichander"
        elif l3[i]==2:
            l3[i]="A.R.Rahman"
        elif l3[i]==4:
            l3[i]="Ilaiyaraaja"
        elif l3[i]==5:
            l3[i]="Silambarasan TR"
        elif l3[i]==6:
            l3[i]="Vijay"
        elif l3[i]==7:
            l3[i]="Sid Sriram"

        
    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/moodhappy.html",context1)
#______________________________________________________________________

def energetic(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(moodid__exact=2)
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    for i in range (len(l3)):
        if l3[i]==1:
            l3[i]="Anirudh Ravichander"
        elif l3[i]==2:
            l3[i]="A.R.Rahman"
        elif l3[i]==4:
            l3[i]="Ilaiyaraaja"
        elif l3[i]==5:
            l3[i]="Silambarasan TR"
        elif l3[i]==6:
            l3[i]="Vijay"
        elif l3[i]==7:
            l3[i]="Sid Sriram"

        
    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/moodenergetic.html",context1)
#______________________________________________________________________

def sad(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(moodid__exact=3)
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    for i in range (len(l3)):
        if l3[i]==1:
            l3[i]="Anirudh Ravichander"
        elif l3[i]==2:
            l3[i]="A.R.Rahman"
        elif l3[i]==4:
            l3[i]="Ilaiyaraaja"
        elif l3[i]==5:
            l3[i]="Silambarasan TR"
        elif l3[i]==6:
            l3[i]="Vijay"
        elif l3[i]==7:
            l3[i]="Sid Sriram"

        
    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/moodsad.html",context1)
#______________________________________________________________________

def lovebeats(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(moodid__exact=5)
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    for i in range (len(l3)):
        if l3[i]==1:
            l3[i]="Anirudh Ravichander"
        elif l3[i]==2:
            l3[i]="A.R.Rahman"
        elif l3[i]==4:
            l3[i]="Ilaiyaraaja"
        elif l3[i]==5:
            l3[i]="Silambarasan TR"
        elif l3[i]==6:
            l3[i]="Vijay"
        elif l3[i]==7:
            l3[i]="Sid Sriram"

        
    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/moodcalm.html",context1)
#______________________________________________________________________

def varisu(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(movieid__exact=2)
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    for i in range (len(l3)):
        if l3[i]==1:
            l3[i]="Anirudh Ravichander"
        elif l3[i]==2:
            l3[i]="A.R.Rahman"
        elif l3[i]==4:
            l3[i]="Ilaiyaraaja"
        elif l3[i]==5:
            l3[i]="Silambarasan TR"
        elif l3[i]==6:
            l3[i]="Vijay"
        elif l3[i]==7:
            l3[i]="Sid Sriram"

        
    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/movievarisu.html",context1)
#______________________________________________________________________

def vikram(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(movieid__exact=3)
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    for i in range (len(l3)):
        if l3[i]==1:
            l3[i]="Anirudh Ravichander"
        elif l3[i]==2:
            l3[i]="A.R.Rahman"
        elif l3[i]==4:
            l3[i]="Ilaiyaraaja"
        elif l3[i]==5:
            l3[i]="Silambarasan TR"
        elif l3[i]==6:
            l3[i]="Vijay"
        elif l3[i]==7:
            l3[i]="Sid Sriram"

    
        
    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/movievikram.html",context1)
#______________________________________________________________________

def vip(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(movieid__exact=4)
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    for i in range (len(l3)):
        if l3[i]==1:
            l3[i]="Anirudh Ravichander"
        elif l3[i]==2:
            l3[i]="A.R.Rahman"
        elif l3[i]==4:
            l3[i]="Ilaiyaraaja"
        elif l3[i]==5:
            l3[i]="Silambarasan TR"
        elif l3[i]==6:
            l3[i]="Vijay"
        elif l3[i]==7:
            l3[i]="Sid Sriram"

        
    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/movievip.html",context1)
#______________________________________________________________________

def classical(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(genreid__exact=4)
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    for i in range (len(l3)):
        if l3[i]==1:
            l3[i]="Anirudh Ravichander"
        elif l3[i]==2:
            l3[i]="A.R.Rahman"
        elif l3[i]==4:
            l3[i]="Ilaiyaraaja"
        elif l3[i]==5:
            l3[i]="Silambarasan TR"
        elif l3[i]==6:
            l3[i]="Vijay"
        elif l3[i]==7:
            l3[i]="Sid Sriram"

        
    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/genreclassical.html",context1)
#______________________________________________________________________

def folk(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(genreid__exact=6)
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    for i in range (len(l3)):
        if l3[i]==1:
            l3[i]="Anirudh Ravichander"
        elif l3[i]==2:
            l3[i]="A.R.Rahman"
        elif l3[i]==4:
            l3[i]="Ilaiyaraaja"
        elif l3[i]==5:
            l3[i]="Silambarasan TR"
        elif l3[i]==6:
            l3[i]="Vijay"
        elif l3[i]==7:
            l3[i]="Sid Sriram"

        
    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/genrefolk.html",context1)
#______________________________________________________________________

def hiphop(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(genreid__exact=3)
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    for i in range (len(l3)):
        if l3[i]==1:
            l3[i]="Anirudh Ravichander"
        elif l3[i]==2:
            l3[i]="A.R.Rahman"
        elif l3[i]==4:
            l3[i]="Ilaiyaraaja"
        elif l3[i]==5:
            l3[i]="Silambarasan TR"
        elif l3[i]==6:
            l3[i]="Vijay"
        elif l3[i]==7:
            l3[i]="Sid Sriram"

        
    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/genrehiphop.html",context1)
#______________________________________________________________________

def jazz(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(genreid__exact=5)
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    for i in range (len(l3)):
        if l3[i]==1:
            l3[i]="Anirudh Ravichander"
        elif l3[i]==2:
            l3[i]="A.R.Rahman"
        elif l3[i]==4:
            l3[i]="Ilaiyaraaja"
        elif l3[i]==5:
            l3[i]="Silambarasan TR"
        elif l3[i]==6:
            l3[i]="Vijay"
        elif l3[i]==7:
            l3[i]="Sid Sriram"

    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/genrejazz.html",context1)
#______________________________________________________________________

def pop(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(genreid__exact=2)
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    for i in range (len(l3)):
        if l3[i]==1:
            l3[i]="Anirudh Ravichander"
        elif l3[i]==2:
            l3[i]="A.R.Rahman"
        elif l3[i]==4:
            l3[i]="Ilaiyaraaja"
        elif l3[i]==5:
            l3[i]="Silambarasan TR"
        elif l3[i]==6:
            l3[i]="Vijay"
        elif l3[i]==7:
            l3[i]="Sid Sriram"

        
    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/genrepop.html",context1)
#______________________________________________________________________

def rock(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.filter(genreid__exact=1)
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    for i in range (len(l3)):
        if l3[i]==1:
            l3[i]="Anirudh Ravichander"
        elif l3[i]==2:
            l3[i]="A.R.Rahman"
        elif l3[i]==4:
            l3[i]="Ilaiyaraaja"
        elif l3[i]==5:
            l3[i]="Silambarasan TR"
        elif l3[i]==6:
            l3[i]="Vijay"
        elif l3[i]==7:
            l3[i]="Sid Sriram"

    context1 = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/genrerock.html",context1)
#______________________________________________________________________

def admins(request):
    context = {
        "data" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
    }
  
    return render(request, "new1/admins.html",context)

#______________________________________________________________________
def signout(request):
    return render(request, "new1/signout.html")
#______________________________________________________________________
def user(request):
    context = {
        "data" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        }
    context1 = {
        "data1" : ['http://wrbbradio.org/wp-content/uploads/2016/10/grey-background-07.jpg','http://wrbbradio.org/wp-content/uploads/2016/10/grey-background-07.jpg','https://wallpaperset.com/w/full/f/6/d/121717.jpg','https://wallpaperset.com/w/full/f/6/d/121717.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg'],
    }
    return render(request, "new1/user.html",context)
#______________________________________________________________________
def music(request):

    l=[1]
    l1=[1]
    l2=[1]
    l3=[1]
    l0=[]
    songs1 = song.objects.all()
    for song1 in songs1:
        l.append(song1.songurl)
        l1.append(song1.imageurl)
        l2.append(song1.songname)
        l3.append(song1.artistid_id)
    for i in range (len(l)-1):
        l0.append(i+1)
    for i in range (len(l3)):
        if l3[i]==1:
            l3[i]="Anirudh Ravichander"
        elif l3[i]==2:
            l3[i]="A.R.Rahman"
        elif l3[i]==4:
            l3[i]="Ilaiyaraaja"
        elif l3[i]==5:
            l3[i]="Silambarasan TR"
        elif l3[i]==6:
            l3[i]="Vijay"
        elif l3[i]==7:
            l3[i]="Sid Sriram"

    context = {
        "data3" : l2,
        "data" : l0,
        #"data3" : [1, "JE", 3, 4, 5, 6, 7, 8, 9, 10,11],
        "data3" : l2,
        #"data1" : [1,'https://wallpaperset.com/w/full/a/9/9/121757.jpg','https://wallpaperset.com/w/full/b/4/c/309918.jpg','https://wallpaperset.com/w/full/e/2/f/121709.jpg','https://wallpaperset.com/w/full/0/3/5/121911.jpg','https://wallpaperset.com/w/full/4/5/3/121734.jpg','https://wallpaperset.com/w/full/9/5/0/121752.jpg','https://wallpaperset.com/w/full/f/4/a/121778.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg','https://wallpaperset.com/w/full/9/b/a/309901.jpg','https://wallpaperset.com/w/full/7/b/2/121764.jpg'],
        "data1" : l1,
        #"data2" : [1,'https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Idhazhin%20Oram.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/3/Why%20This%20Kolaveri.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Jodha%20Akbar/Mulumathy%20Avalathu.mp3','https://www.friendstamilmp3.in/songs2/A%20R%20Rahman%20Hits/Alai%20Payuthe/Pachchai%20Nirame.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Pathala%20Pathala%20Kuttyum%20Pathala.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Vikram%20(2022)/Wasted.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Ranjithame%20Ranjithame%20(Kattu%20Malli%20Katti%20Vachaa).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Varisu%20(2022)/Thee%20Thalapathy%20(Unna%20Parthu%20Siricha).mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/Oothungada%20Sangu.mp3','https://www.friendstamilmp3.in/songs2/A-Z%20Movie%20Songs/Velaiyilla%20Pattathari/What%20A%20Karavad.mp3'],
        "data2" : l,
        "data4" : l3,
    }
    return render(request, "new1/music.html",context)
#______________________________________________________________________




#______________________________________________________________________

def admsignin(request):
    if request.method =='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return redirect('admins')

        else:
            messages.error(request , "Bad crerdentials")
            return redirect('register')

    return render(request, "new1/admsignin.html")

#______________________________________________________________________

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')


        conn = psycopg2.connect("dbname=mydb1 user=myuser1 password=db1234pg")
        with conn.cursor() as cur:
            cur.execute("INSERT INTO trial1_users (username,fname,lname,email,passw) VALUES (%s,%s,%s,%s,%s)",(username,fname,lname,email,pass1))
            conn.commit()

        #myuser = User.objects.create_user(username=username,email=email,password=pass1)
       # myuser.first_name = fname
        #myuser.last_name = lname
       # myuser.save()


        messages.success(request,"Account creation successfull")

        return redirect("signin")

    return render(request, "new1/register.html")

#______________________________________________________________________

def signin(request):
    x=""
    y=""
    if request.method =='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        
        user1 = users.objects.filter(username__exact=username)
        for user in user1:
            x=user.username
            y=user.passw
        print(x)
        if username==x:
            if pass1==y:
           # conn = psycopg2.connect("dbname=mydb1 user=myuser1 password=db1234pg")
           # with conn.cursor() as cur:
            #    cur.execute("SELECT username FROM users WHERE username = %s",(username))
             #   data = cur.fetchone()[0]
               # print(data)
           #     cur.close()
           # conn.close()
                print(user1)
            #login(request,user1)
            #fname = user.first_name
                return redirect("music")

        else:
            messages.error(request , "Bad crerdentials")
            return redirect('signin')

    return render(request, "new1/signin.html")
#______________________________________________________________________

'''
user1 = users.objects.filter(username__exact='2222')
x=user1[0]
if user1.exists():
    print("Hello ",x.username," bye")
else:
    print("No raja available.")

l=[1]
l1=[1]
l2=[1]
l0=[]
songs1 = song.objects.all()
for song1 in songs1:
    l.append(song1.songurl)
    l1.append(song1.imageurl)
    l2.append(song1.songname)
print(len(l)-1)
for i in range (len(l)-1):
    l0.append(i)
print(l0)
'''

l1=[1]
l=[1]
l2=[1]
l3=[1]

l0=[]
songs1 = song.objects.filter(language1__exact="Tamil")
for song1 in songs1:
    l.append(song1.songurl)
    l1.append(song1.imageurl)
    l2.append(song1.songname)
    l3.append(song1.artistid_id)

for i in range (len(l)-1):
    l0.append(i+1)
print(l3)

for i in range (len(l3)):
    if l3[i]==1:
        l3[i]="Anirudh Ravichander"
    elif l3[i]==2:
        l3[i]="A.R.Rahman"
    elif l3[i]==4:
        l3[i]="Ilaiyaraaja"
    elif l3[i]==5:
        l3[i]="Silambarasan TR"
    elif l3[i]==6:
        l3[i]="Vijay"
    elif l3[i]==7:
        l3[i]="Sid Sriram"

#print(l3)
        