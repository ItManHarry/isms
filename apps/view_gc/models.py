from django.db import models
from db import BaseModel
class Publisher(BaseModel):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=32)
    province = models.CharField(max_length=32)
    web_site = models.URLField()

    def __str__(self):
        return self.name

    class Meta(BaseModel.Meta):
        db_table = 'stu_publisher'
        ordering = ['-name']
class Author(BaseModel):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=64)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta(BaseModel.Meta):
        db_table = 'stu_author'
class Book(BaseModel):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publish_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta(BaseModel.Meta):
        db_table = 'stu_book'