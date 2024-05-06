from django.contrib import admin

from income_models.models import Magazine, Newspaper, Storage, BaseModel


@admin.register(BaseModel)
class BaseModelAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = (
        'stoage_id', 'amount', 'sum_cost', 'operation_date', 'operation_type',
        'active'
    )


@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ('magazine_id', 'title')


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ('newspaper_id', 'title')
