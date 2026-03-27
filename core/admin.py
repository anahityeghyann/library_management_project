from django.contrib import admin
from django.contrib.auth.models import User

from .models import *

admin.site.register(Libraryuser)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(BookCopy)
admin.site.register(Loan)
