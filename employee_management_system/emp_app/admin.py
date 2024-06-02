from django.contrib import admin
from . models import Employee, Person, Department,GroupEmployee,Groups,LookUpTable
# Register your models here.


admin.site.register(Employee)
admin.site.register(Person)
admin.site.register(Department)
admin.site.register(LookUpTable)

