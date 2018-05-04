from django.contrib import admin
from .models import Category, Product,User_info

# alter admin product page to save current user as author of content
class ProductAdmin(admin.ModelAdmin):
    # save function triggered on form admin
    def save_model(self, request, obj, form, change):
        # set author as user who created/modified the content
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

class MyModelAdmin(admin.ModelAdmin):
    list_display = ['tag_list']

    def get_queryset(self, request):
        return super(MyModelAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

# register admin models forms
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(User_info)