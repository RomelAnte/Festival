from django.contrib import admin
from .models import TypeUser, User, Literature, Festival, Presentation, Entrance, Sale

# Register your models here.
admin.site.register(TypeUser)
admin.site.register(User)
admin.site.register(Literature)
admin.site.register(Festival)
admin.site.register(Presentation)
admin.site.register(Entrance)
admin.site.register(Sale)
