from django.apps import AppConfig
# from django.contrib.admin.apps import AdminConfig

class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'

# class MyShopAdminConfig(AdminConfig):
#     default_site = 'admin.MyShopAdminSite'