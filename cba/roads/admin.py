from django.contrib import admin

from .models import Section


class SectionAdmin(admin.ModelAdmin):
    model = Section
    list_display = (
        'road_section_id', 'road_number', 'road_name', 'section_order'
    )
    search_fields = ('road_section_id', 'road_name',)


admin.site.register(Section, SectionAdmin)
