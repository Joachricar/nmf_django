from django.contrib import admin

from quickstart.models import *
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter


# Register your models here.
@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    pass

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ensemble)
admin.site.register(Location)
admin.site.register(Participant)
admin.site.register(Pianist)

class EventAdmin(PolymorphicChildModelAdmin):
    base_model = Event
    base_fieldsets = [

    ]

@admin.register(SoloEvent)
class SoloEventAdmin(EventAdmin):
    base_model = SoloEvent
    show_in_index = False

@admin.register(BandEvent)
class BandEventAdmin(EventAdmin):
    base_model = BandEvent
    show_in_index = False

@admin.register(EnsembleEvent)
class EnsembleEventAdmin(EventAdmin):
    base_model = EnsembleEvent
    show_in_index = False

@admin.register(Event)
class ModelAParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = Event
    child_models = (SoloEvent, EnsembleEvent, BandEvent)
    list_filter = (PolymorphicChildModelFilter,)  # This is optional.

