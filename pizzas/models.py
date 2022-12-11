from django.db import models

# Create your models here.

class Pizza(models.Model):
   pizza_name = models.CharField(max_length=20)
 
   def __str__(self):
       return self.pizza_name


class Topping(models.Model):
   pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
   topping_name = models.CharField(max_length=40)
 
   #def __str__(self):
       #return self.topping_name
 
 
   class Meta:
       verbose_name_plural = 'toppings'
 
   def __str__(self):
       return f"{self.topping_name[:50]}...."


class Review(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    review = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review
