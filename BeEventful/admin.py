from django.contrib import admin
from .models import FeedbackDetails, UserProfile,StaffDetails,FeedbackDetails ,Booking ,EventDetails

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(StaffDetails)
admin.site.register(FeedbackDetails)
admin.site.register(Booking)
admin.site.register(EventDetails)
