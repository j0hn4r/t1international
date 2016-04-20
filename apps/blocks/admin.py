from glitter import block_admin

from .models import Billboard


block_admin.site.register(Billboard)
block_admin.site.register_block(Billboard, 'Common')
