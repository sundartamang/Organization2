from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import (
    AboutUs,
    Activity,
    BankInformation,
    Carasoul,
    Cause,
    Contact,
    ContactMessage,
    Donor,
    Donation,
    Gallery,
    GalleryTitle,
    Member,
    Program   
)

# Register your models here.
class ProgramAdmin(admin.ModelAdmin): 
    exclude = ('slug',)
    
class GalleryInlineAdmin(admin.TabularInline):
    model = Gallery
    extra = 1

class GalleryTitleAdmin(admin.ModelAdmin):
    inlines = [GalleryInlineAdmin]


class ActivityAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(AboutUs)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(BankInformation)
admin.site.register(Carasoul)
admin.site.register(Cause)
admin.site.register(Contact)
admin.site.register(ContactMessage)
admin.site.register(Donor)
admin.site.register(Donation)
admin.site.register(GalleryTitle, GalleryTitleAdmin)
admin.site.register(Gallery)
admin.site.register(Member)
admin.site.register(Program, ProgramAdmin)