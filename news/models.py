from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField


# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10, blank = True )

    def __str__(self):
        return self.first_name

    def update_editor(self, attr, value):
        setattr(self, attr, value)
        self.save()

    @classmethod
    def all_editors(cls):
        return cls.objects.all()

    class Meta:
        ordering = ['first_name']

class tags(models.Model):
    name = models.CharField(max_length = 30)

    @classmethod
    def new_tag(cls, tagname):
        cls.objects.create(name = tagname)


    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = CloudinaryField('image')

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news

    @classmethod
    def days_news(cls, date):
        news = cls.objects.filter(pub_date__date = date)
        return news

    @classmethod
    def search_by_title(cls, search_term):
        news = cls.objects.filter(title__icontains = search_term)
        return news