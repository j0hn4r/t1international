from glitter import block_admin

from .models import Billboard, Poster, Signees


block_admin.site.register((Billboard, Poster, Signees))
block_admin.site.register_block(Billboard, 'Common')
block_admin.site.register_block(Poster, 'Common')
block_admin.site.register_block(Signees, 'Common')
