from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField("Date Published")

    @python_2_unicode_compatible
    def __str__(self):
        message = str(self.publication_date) + ": " + str(self.question_text)
        return message


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    @python_2_unicode_compatible
    def __str__(self):
        message = (
            "Ques: %s | Choice: %s | Votes: %s" % (str(self.question),
                                                   str(self.choice_text),
                                                   str(self.votes)))
        return message
