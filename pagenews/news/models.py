from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
#from users.models import Profile

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #first_name = models.CharField(max_length=30, blank=True)
    #last_name = models.CharField(max_length=150, blank=True)
    #position = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
            return self.title


    def save(self, *args, **kwargs):
        #profile = Profile.objects.get(user=self.author)
        #self.position = profile.position
        #self.first_name = self.author.first_name
        #self.last_name = self.author.last_name
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})