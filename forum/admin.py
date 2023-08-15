from django.contrib import admin
from .models import *

admin.site.register(Forum)
admin.site.register(ForumPost)
admin.site.register(ForumPostComment)
admin.site.register(ForumAdmin)
admin.site.register(ForumCategory)
admin.site.register(ForumPostLike)
