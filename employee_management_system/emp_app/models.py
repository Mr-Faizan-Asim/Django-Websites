from django.db import models

class LookUpTable(models.Model):
    value = models.CharField(max_length=255)
    category = models.CharField(max_length=50)

    class Meta:
        unique_together = (('value', 'category'),)
        db_table = 'LookUpTable'


class Department(models.Model):
    department_name = models.CharField(max_length=255)
    status = models.ForeignKey(LookUpTable, on_delete=models.CASCADE)
    manufactured = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'Department'


class Person(models.Model):
    email = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True, unique=True)
    username = models.CharField(max_length=50, unique=True)
    address = models.TextField(null=True, blank=True)
    region = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    cnic = models.CharField(max_length=50, null=True, blank=True, unique=True)
    status = models.IntegerField(null=True, blank=True)
    father_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return  "%s %s %s" %(self.username,self.father_name,self.email)


    class Meta:
        db_table = 'Person'


class Employee(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.ForeignKey(LookUpTable, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Employee'




class Supervisor(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Supervisor'


class Groups(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateField()
    status = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        db_table = 'Groups'


class GroupEmployee(models.Model):
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date_joined = models.DateField()

    class Meta:
        db_table = 'GroupEmployee'
