from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=60)
    retired = models.BooleanField(default=False)

    artists = models.ManyToManyField("people.Artist")

    def __str__(self) -> str:
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=40, unique=True)
    release_date = models.DateField()
    selling_price = models.FloatField()
    author = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}: {self.author}"

class Song(models.Model):
    title = models.CharField(max_length=60)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    order = models.IntegerField()
    mp3_file = models.FileField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.order}: {self.title} ({self.album})"