from django.db import models

class Category(models.Model):
	name = models.CharFieuld(max_length=150,)
