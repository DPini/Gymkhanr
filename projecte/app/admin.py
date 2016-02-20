from django.contrib import admin
from .models import Gymcana,ProvaTest,ProvaCodi,RespostaTest

admin.site.register(RespostaTest)

class RespostaTestInline(admin.StackedInline):
    model = RespostaTest

class ProvaTestAdmin(admin.ModelAdmin):
    #exclude = ('superada')
    inlines = [ RespostaTestInline ]


# Register your models here.
admin.site.register(Gymcana)
#admin.site.register(Prova)
admin.site.register(ProvaTest,ProvaTestAdmin)
admin.site.register(ProvaCodi)
