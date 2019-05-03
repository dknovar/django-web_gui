from django.contrib import admin

# Register your models here.
from.models import File
from. models import img_bnc
from. models import img_gray
from. models import img_h
from. models import img_s
from. models import img_v
from. models import tb_ciri

admin.site.register(File)
admin.site.register(img_bnc)
admin.site.register(img_gray)
admin.site.register(img_h)
admin.site.register(img_s)
admin.site.register(img_v)
admin.site.register(tb_ciri)