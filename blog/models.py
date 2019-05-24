from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    crated_date = models.DateTimeField(default=timezone.now())

    ## publishing! ##
    published_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    #################

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey("blog.Post", related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    text = models.TextField()
    crated_date = models.DateTimeField(default=timezone.now())

    ## aproving! ####
    aproved_comments = models.BooleanField(default=False)

    def aprove(self):
        self.aproved_comments = True 
        self.save()
    #################

    ## where should i send them ??!!
    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text