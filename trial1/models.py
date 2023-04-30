from django.db import models
#from .models import mood, genre, artist, movie

class users(models.Model):
    username = models.CharField(max_length=50, unique=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    passw = models.CharField(max_length=100)

class movie(models.Model):
    movieid=models.IntegerField()
    moviename=models.CharField(max_length=50)
    year1=models.IntegerField()

class mood(models.Model):
    moodid=models.IntegerField()
    moodname=models.CharField(max_length=50)

class genre(models.Model):
    genreid=models.IntegerField()
    genrename=models.CharField(max_length=50)

class artist(models.Model):
    artistid=models.IntegerField()
    artistname=models.CharField(max_length=50)

class song(models.Model):
    songid=models.IntegerField()
    songname=models.CharField(max_length=50)
    imageurl=models.CharField(max_length=500)
    songurl=models.CharField(max_length=500)
    language1=models.CharField(max_length=50)
    movieid=models.ForeignKey(movie, on_delete=models.CASCADE)
    artistid=models.ForeignKey(artist, on_delete=models.CASCADE)
    genreid=models.ForeignKey(genre, on_delete=models.CASCADE)
    moodid=models.ForeignKey(mood, on_delete=models.CASCADE)

#user1= users.objects.all()
#for user in user1:
 #   print(user.username, user.fname, user.email, user.passw)
#for user in user1:
   # print(user.username)

user1 = users.objects.filter(username__exact='kavushik')
for user in user1:
    print(user.username, user.fname, user.email, user.passw)
    x=user.username
print(x)

art1 = artist.objects.filter(artistid__exact=1)
for art in art1:
    print(art.artistid,art.artistname)

gen1 = genre.objects.filter(genreid__exact=1)
for gen in gen1:
    print(gen.genreid,gen.genrename)

son1 = song.objects.filter(songid__exact=1)
for son in son1:
    print(son.songid,son.songname,son.imageurl,son.songurl,son.language1,son.moodid_id,son.movieid_id,son.artistid_id,son.genreid_id)
#user1 = users.objects.filter(fname__startswith='A')

#users1 = users.objects.filter(username__exact='2222')

#if users1.exists():
 #   print("Hello, raja!")
#else:
 #   print("No raja available.")

