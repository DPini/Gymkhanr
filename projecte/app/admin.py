from django.contrib import admin
from .models import Gymcana,Prova,ProvaTest,ProvaCodi,RespostaTest
# Register your models here.

admin.site.register(Gymcana)
#admin.site.register(Prova)
admin.site.register(ProvaTest)
admin.site.register(ProvaCodi)
admin.site.register(RespostaTest)

class RespostaTestInlineAdmin(admin.TabularInline):
    model = RespostaTest

class ProvaTestAdmin(admin.ModelAdmin):
    inlines = [ RespostaTestInlineAdmin ]
