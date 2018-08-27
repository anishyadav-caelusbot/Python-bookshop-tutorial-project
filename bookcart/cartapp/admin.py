
from django.contrib import admin


from .models import customers
# Register your models here.
from .models import orders
from .models import books
from .models import categories
from .models import order_items


class CategoriesAdmin(admin.ModelAdmin):
	list_display=['catname']

admin.site.register(customers)
admin.site.register(orders)
admin.site.register(books)
admin.site.register(categories)
admin.site.register(order_items)


admin.site.register(CategoriesAdmin)



