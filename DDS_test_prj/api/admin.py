from django.contrib import admin

from .models import DDSStatus, DDSType, DDSCategory, DDSSubcategory, FinancialMove


class DDSAdmin(admin.ModelAdmin):
    list_display = ('date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment')
    list_filter = ('date', 'status', 'type', 'category', 'subcategory')
    search_fields = ('comment',)
    date_hierarchy = 'date'
    ordering = ('-date',)

    fieldsets = (
        (None, {
            'fields': ('status', 'type', 'category', 'subcategory', 'amount', 'comment')
        }),
        ('Дата', {
            'fields': ('date',),
            'classes': ('collapse',)
        }),
    )


admin.site.register(DDSStatus)
admin.site.register(DDSType)
admin.site.register(DDSCategory)
admin.site.register(DDSSubcategory)
admin.site.register(FinancialMove, DDSAdmin)
