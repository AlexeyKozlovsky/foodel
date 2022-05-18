from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.forms.auth_user_forms import BaseUserChangeForm, BaseUserCreationForm
from core.models import BaseUser, Employee, Businessman, Courier, Address, City, Country, Company, Category, Good, \
    GoodInstance, GoodServing, MarketType, MarketInstance, Market, Bank


class UserAdmin(BaseUserAdmin):
    form = BaseUserChangeForm
    add_form = BaseUserCreationForm

    list_display = ('email', 'phone', 'first_name', 'last_name', 'is_superuser')
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'img')}),
        ('Permissions', {'fields': ('is_superuser',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'first_name', 'last_name', 'password1', 'password2', 'img'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(BaseUser, UserAdmin)

admin.site.register(Employee)
admin.site.register(Businessman)
admin.site.register(Courier)
admin.site.unregister(Group)

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Address)
admin.site.register(Company)
admin.site.register(MarketType)
admin.site.register(Market)
admin.site.register(MarketInstance)
admin.site.register(Category)
admin.site.register(Good)
admin.site.register(GoodInstance)
admin.site.register(GoodServing)
admin.site.register(Bank)
