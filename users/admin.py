from django.contrib import admin
from users.models import AuthUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from users.forms import UserCreationForm


# Register your models here.


@admin.register(AuthUser)
class AuthUsrAdmin(BaseUserAdmin):
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email'),
        }),
    )
    search_fields = ('first_name', 'last_name', 'email', 'products__name')

    add_form = UserCreationForm

    def profile_avatar(self, instance):
        return instance.profile.avatar

    profile_avatar.short_description = 'Profile Avatar'

    def get_urls(self):
        return super(BaseUserAdmin, self).get_urls()

    # def product_name(self, instance):
    #     return instance.product.name
    # product_name.short_description = 'Product Name'
