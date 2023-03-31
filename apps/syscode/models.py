from django.db import models
from db import BaseModel
class WordBook(BaseModel):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return self.name

    class Meta(BaseModel.Meta):
        db_table = 'sys_word'

class WordEnum(BaseModel):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=4)
    word_book = models.ForeignKey(WordBook, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta(BaseModel.Meta):
        db_table = 'sys_enum'