from django.apps import apps, AppConfig
from django.contrib import admin

admin.site.site_header = "BRIDE Sandbox DB Models"
admin.site.site_title = "BRIDE Sandbox DB Admin Area"
admin.site.index_title = "Welcome to the BRIDE Sandbox DB Admin Area"

models = apps.get_models()

for model in models:
  try:
    admin.site.register(model)
  except admin.sites.AlreadyRegistered:
    pass
  

