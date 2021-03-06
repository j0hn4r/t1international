# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from glitter import block_admin

from .models import Blockquote, FAQ, SignupFormBlock


block_admin.site.register((Blockquote, FAQ, SignupFormBlock))
block_admin.site.register_block(Blockquote, 'Common')
block_admin.site.register_block(FAQ, 'Common')
block_admin.site.register_block(SignupFormBlock, 'Forms')
