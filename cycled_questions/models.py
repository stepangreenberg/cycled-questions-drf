from django.db import models


class Creature(models.Model):
    name = models.CharField(
        max_length=200,
        primary_key=True,
    )
    current_question = models.ForeignKey(
        "Question",
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="_creatures_that_choosed_this_question",
    )

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField()
    creature = models.ForeignKey(
        Creature,
        on_delete=models.CASCADE,
        related_name="questions",
    )

    def __str__(self):
        return self.text
