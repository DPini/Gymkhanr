from django.contrib import admin
from .models import Gymcana,ProvaTest,ProvaCodi,RespostaTest
# Register your models here.


class RespostaTestInline(admin.StackedInline):
    model = RespostaTest

class ProvaTestAdmin(admin.ModelAdmin):
    inlines = [ RespostaTestInline ]

# Register your models here.
admin.site.register(Gymcana)
#admin.site.register(Prova)
admin.site.register(ProvaTest,ProvaTestAdmin)
admin.site.register(ProvaCodi)
admin.site.register(RespostaTest)
