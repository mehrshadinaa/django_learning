from django.contrib import admin
from .models import Expense, Token

admin.site.register(Expense)
admin.site.register(Token)
