from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register([Student,Employee,Course,Room,Day,IshHaqqi,IshHaqqiTuri,Payment,Group,Harajatturi,Roll,Xarajat])
