from django.contrib import admin
from folderstats.models import File, Folder, Line

# Register your models here.
class FileAdmin(admin.ModelAdmin):
    pass
admin.site.register(File, FileAdmin)

class FolderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Folder, FolderAdmin)

class LineAdmin(admin.ModelAdmin):
    pass
admin.site.register(Line, LineAdmin)