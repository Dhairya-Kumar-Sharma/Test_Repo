from django.apps import AppConfig


class ModifierAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modifier_admin'
    verbose_name: str = "Users"
