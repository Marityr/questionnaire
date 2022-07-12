from tabnanny import verbose
from django.db import models


class Feedback(models.Model):

    RATE_CHOICE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )

    userID = models.CharField(verbose_name='UserID', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data add') 
    email = models.CharField(verbose_name='Email', max_length=255)
    rate = models.CharField(verbose_name='Rate', choices=RATE_CHOICE, default=5, max_length=2)
    like = models.TextField(verbose_name='like')
    dislike = models.TextField(verbose_name='dislike')

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'

    def __str__(self) -> str:
        return str(self.id)
