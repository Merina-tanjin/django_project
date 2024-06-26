from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



#Core


class Cv(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cv')

    def __str__(self):
        return self.user.username


class Skill(models.Model):
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)
    s_name = models.CharField(max_length=500)
    s_level = models.CharField(max_length=500)
    cv_id = models.ForeignKey(Cv, on_delete=models.CASCADE,  related_name='skills')


    def __str__(self):
        return self.s_name



class Experince(models.Model):
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)
    e_office = models.CharField(max_length=500)
    e_position = models.CharField(max_length=500)
    e_duration = models.CharField(max_length=500)

    def __str__(self):
        return self.s_name


class Academic(models.Model):
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)
    a_institution = models.CharField(max_length=500)
    a_year = models.CharField(max_length=500)
    a_award = models.CharField(max_length=500)

    def __str__(self):
        return self.a_institution



class Referee(models.Model):
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)
    r_name = models.CharField(max_length=500)
    r_email = models.CharField(max_length=500)
    r_phone = models.CharField(max_length=500)

    def __str__(self):
        return self.r_name



class cv_pro(models.Model):
   
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cv_pro')
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)
    fname = models.CharField(max_length=500)
    lname = models.CharField(max_length=500)
    mname = models.CharField(max_length=500)
    gender = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    region = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    occupation = models.CharField(max_length=500)
    dob = models.DateField(default='None')
    bio = models.TextField()
    avator = models.ImageField(upload_to='profile/', default='profile/avator.png', null=True)


    def __str__(self):
        return self.fname

    def delete(self, *args, **kwargs):
        self.avator.delete()
        super().delete(*args, **kwargs)

