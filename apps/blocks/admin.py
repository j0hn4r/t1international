from glitter import block_admin

from .models import Billboard, VideoBanner, Poster, Signees


block_admin.site.register((Billboard, VideoBanner, Poster, Signees))
block_admin.site.register_block(Billboard, 'Common')
block_admin.site.register_block(VideoBanner, 'Common')
block_admin.site.register_block(Poster, 'Common')
block_admin.site.register_block(Signees, 'Common')
