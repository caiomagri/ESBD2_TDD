from django.db import models

class List(models.Model):
	pass

class Item(models.Model):
	CHOICES_PRIORITY = [
		('hight', 'alta'),
		('medium', 'média'),
		('low', 'baixa'),
	]

	text = models.TextField(default='')
	list = models.ForeignKey(List,on_delete=models.SET_DEFAULT,default=None)
	priority = models.CharField(
        max_length=6,
        choices=CHOICES_PRIORITY,
        default="low",
    )
