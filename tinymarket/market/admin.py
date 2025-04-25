from django.contrib import admin
from .models import User, Product, ChatMessage, BlockedUser, Payment

# 관리자(admin) 페이지에 등록
admin.site.register(User)
admin.site.register(Product)
admin.site.register(ChatMessage)
admin.site.register(BlockedUser)
admin.site.register(Payment)
