from django.db import models


class ComplexNumber(models.Model):
    real_number = models.FloatField("Real number part")
    img_number = models.FloatField("Img number part")

    def __str__(self):
        return complex(self.real_number, self.img_number)
