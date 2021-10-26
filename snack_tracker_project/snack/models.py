from django.db import models
from django.contrib.auth import get_user_model

class Snack(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    # get_user_model will give us the name of the table, it returns the name of a class  
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def __str__(self):
        return self.name

# it will take the name from the Snack class
# delete CASCADE it means it will delete in childern as well, same goes to update

