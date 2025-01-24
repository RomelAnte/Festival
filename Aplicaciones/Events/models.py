from django.db import models

# Create your models here.

class TypeUser(models.Model):
    id_type = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class User(models.Model):
    id_use = models.AutoField(primary_key=True)
    ci = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    type_user = models.ForeignKey(TypeUser, on_delete=models.CASCADE)
    
class Literature(models.Model):
    id_lit = models.AutoField(primary_key=True)
    literature = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Festival(models.Model):
    id_fes = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    startDate = models.DateField()
    endDate = models.DateField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Presentation(models.Model):
    id_prese = models.AutoField(primary_key=True)
    scenery = models.CharField(max_length=100)
    date = models.DateTimeField()
    duration = models.IntegerField()
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Entrance(models.Model):
    id_ent = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)

class Sale(models.Model):
    id_sale = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entrace = models.ForeignKey(Entrance, on_delete=models.CASCADE)

class Licence(models.Model):
    id_lic = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    acronnym = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    
class Audit(models.Model):
    id_audit = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    description = models.TextField()
    gender = models.CharField(max_length=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    