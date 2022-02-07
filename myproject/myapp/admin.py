from django.contrib import admin
from myapp.models import register


# Register your models here.
class registerAdmin(admin.ModelAdmin):
	list_didplay=('Name','Cidnumber','Email','Phonenumber','Licensenumber')

admin.site.register(register,registerAdmin)
