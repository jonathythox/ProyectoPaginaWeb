from django.contrib import admin


from . models import Telefono, Marca, TelefonoInstance

admin.site.register(Telefono)
admin.site.register(Marca)
admin.site.register(TelefonoInstance)
