from django.contrib import admin

from .hooks import AFTER_SAVE_RELATED, AFTER_UPDATE_RELATED


class LifecycleModelAdmin(admin.ModelAdmin):
    def save_related(self, request, form, formsets, change):
        obj = form.instance
        if change:
            super(LifecycleModelAdmin, self).save_related(request, form, formsets, change)
            obj._run_hooked_methods(AFTER_UPDATE_RELATED)
        else:
            super(LifecycleModelAdmin, self).save_related(request, form, formsets, change)
            obj._run_hooked_methods(AFTER_SAVE_RELATED)
