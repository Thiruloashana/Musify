from django.urls import path
from . import views

urlpatterns = [
    path('signin',views.signin,name="signin"),
    path('',views.index,name="index"),
    path('admsignin',views.admsignin,name="admsignin"),
    path('user',views.user,name="user"),
    path('music',views.music,name="music"),
    path('admins',views.admins,name="admins"),
    path('signout',views.signout,name="signout"),
    path('register/',views.register,name="register"),
    path('artist',views.artist,name="artist"),
    path('genre',views.genre,name="genre"),
    path('mood',views.mood,name="mood"),
    path('language',views.language,name="language"),
    path('movie',views.movie,name="movie"),
    path('anirudh',views.anirudh,name="anirudh"),
    path('rahman',views.rahman,name="rahman"),
    path('ilaiyaraaja',views.raaja,name="ilaiyaraaja"),
    path('yuvan',views.yuvan,name="yuvan"),
    path('vijay',views.vijay,name="vijay"),
    path('happy',views.happy,name="happy"),
    path('energetic',views.energetic,name="energetic"),
    path('sad',views.sad,name="sad"),
    path('lovebeats',views.lovebeats,name="lovebeats"),
    path('varisu',views.varisu,name="varisu"),
    path('vikram',views.vikram,name="vikram"),
    path('vip',views.vip,name="vip"),
    path('pop',views.pop,name="pop"),
    path('rock',views.rock,name="rock"),
    path('hiphop',views.hiphop,name="hiphop"),
    path('classical',views.classical,name="classical"),
    path('jazz',views.jazz,name="jazz"),
    path('folk',views.folk,name="folk"),
    path('languageenglish',views.langeng,name="languageenglish"),
    path('languagetamil',views.langtam,name="languagetamil"),









]