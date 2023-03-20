from django.db import models
from db import BaseModel
from django.urls import reverse
class Author(BaseModel):
    class Meta(BaseModel.Meta):
        db_table = 'fcv_author'
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})