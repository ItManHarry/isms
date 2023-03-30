from django.db import models
from db import BaseModel
from django.core.exceptions import ValidationError
def validate_wordbook_code(new_code):
    if WordBook.objects.filter(code=new_code.upper()):
        raise ValidationError('字典代码重复！')
class WordBook(BaseModel):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=4, unique=True, validators=[validate_wordbook_code])

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