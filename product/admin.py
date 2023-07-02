from django.contrib import admin

from product.models import Product,Category,ProductImage,ProductSize,ProductColor
# ProductImage


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['slug','Pname']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['Cname','cimage','slug']
admin.site.register(ProductSize)
admin.site.register(ProductColor)
admin.site.register(ProductImage)

