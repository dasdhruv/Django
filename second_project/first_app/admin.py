from django.contrib import admin
# Let us add our model to our admin so that no tom dick harry comes and alter our database
from first_app.models import Topic, Webpage, AccessRecord
# Register your models here.

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
