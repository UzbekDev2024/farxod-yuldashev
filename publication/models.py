from django.db import models

class Projects(models.Model):
    author = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    title = models.CharField(max_length=400)
    body = models.TextField()
    link = models.CharField(max_length=500)
    likeCount = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    publishedDate = models.DateField()

    def __str__(self):
        return self.title

