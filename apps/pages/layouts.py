# -*- coding: utf-8 -*-

from glitter import columns, templates
from glitter.layouts import PageLayout


@templates.attach('glitter_pages.Page')
class SingleColumn(PageLayout):
    billboard_top = columns.Column(width=1080)
    intro = columns.Column(width=960)
    content = columns.Column(width=960)
    footer = columns.Column(width=960)


@templates.attach('glitter_pages.Page')
class Home(PageLayout):
    billboard_top = columns.Column(width=1080)
    intro_half_one = columns.Column(width=480)
    intro_half_two = columns.Column(width=480)
    content = columns.Column(width=960)
    footer = columns.Column(width=960)


@templates.attach('glitter_pages.Page')
class TwoColumn(PageLayout):
    content = columns.Column(width=960)
    sidebar = columns.Column(width=480)
    footer = columns.Column(width=960)
