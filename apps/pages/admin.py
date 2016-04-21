# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from glitter import block_admin

from .models import Blockquote


block_admin.site.register((Blockquote))
block_admin.site.register_block(Blockquote, 'Common')
