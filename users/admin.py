from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Teams, TeamRoles
from appointments import  models as Appointment_Models


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('user_mobile_number','organization',)}),
    )

class TeamAdmin(admin.ModelAdmin):
    model = Teams

    class Meta:
        verbose_name_plural = "Teams"

class TeamRolesAdmin(admin.ModelAdmin):
    model = Teams

    class Meta:
        verbose_name_plural = "TeamRoles"

class SevicesAdmin(admin.ModelAdmin):
    model = Appointment_Models.Services

    class Meta:
        verbose_name_plural = "TeamRoles"

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Teams, TeamAdmin)
admin.site.register(TeamRoles, TeamRolesAdmin)
admin.site.register(Appointment_Models.Services, SevicesAdmin)