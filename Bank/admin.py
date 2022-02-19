from django.contrib import admin
from Bank.models import FeedBack,CustomerAccount,transectiondetail
from django.contrib import auth

# Register your models here. 
admin.site.register(FeedBack)
admin.site.register(transectiondetail)
admin.site.register(CustomerAccount)


# ADMIN Password: ----------------------------------------
        # User: admin143
        # PassWord: admin123