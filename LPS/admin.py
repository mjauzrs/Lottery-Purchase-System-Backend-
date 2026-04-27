from django.contrib import admin
from .models import LotteryTicket, Order, ElectronicTicket, CustomerProfile, Notification, LotteryDraw

##==================================================================
# These are the different databases in Django admin to keep track of
#===================================================================
admin.site.register(Order)
admin.site.register(ElectronicTicket)
admin.site.register(CustomerProfile)
admin.site.register(LotteryTicket)
admin.site.register(LotteryDraw)
admin.site.register(Notification)
