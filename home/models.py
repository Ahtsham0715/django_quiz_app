from django.db import models
import uuid
import random
# Create your models here.



class BaseModel(models.Model):
    uid = models.UUIDField(primary_key = True, editable = False, default= uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now_add=True)    
    
    class Meta:
        abstract = True

class Category(BaseModel):
    category_name = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.category_name
    
class Question(BaseModel):
    category = models.ForeignKey(Category, related_name= 'category' , on_delete=models.CASCADE)
    question = models.CharField(max_length=5000)
    marks = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.question
    
    def get_answers(self):
        answer_objs = list(Answer.objects.filter(question = self))
        random.shuffle(answer_objs)
        return [
            {'answer': answer.answer, 'is_correct': answer.is_correct}
            for answer in answer_objs
        ]

class Answer(BaseModel):
    question = models.ForeignKey(Question, related_name='question_title', on_delete=models.CASCADE)
    answer = models.CharField(max_length=5000)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.answer

    
    