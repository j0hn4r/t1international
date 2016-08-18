# -*- coding: utf-8 -*-

from glitter import columns, templates
from glitter.layouts import PageLayout


@templates.attach('glitter_pages.Page')
class SingleColumn(PageLayout):
    billboard_top = columns.Column(width=1080)
    intro = columns.Column(width=960)
    billboard_middle = columns.Column(width=1080)
    content = columns.Column(width=960)
    footer = columns.Column(width=960)
    grid_cell_one = columns.Column(width=720)
    grid_cell_two = columns.Column(width=720)
    grid_cell_three = columns.Column(width=720)


@templates.attach('glitter_pages.Page')
class Home(PageLayout):
    billboard_top = columns.Column(width=1080)
    intro_half_one = columns.Column(width=720)
    intro_half_two = columns.Column(width=720)
    grid_cell_one = columns.Column(width=720)
    grid_cell_two = columns.Column(width=720)
    grid_cell_three = columns.Column(width=720)
    grid_cell_four = columns.Column(width=720)
    grid_cell_five = columns.Column(width=720)
    grid_cell_six = columns.Column(width=720)
    content = columns.Column(width=960)
    footer = columns.Column(width=960)


@templates.attach('glitter_pages.Page')
class Grid(PageLayout):
    billboard_top = columns.Column(width=1080)
    grid_cell_one = columns.Column(width=720)
    grid_cell_two = columns.Column(width=720)
    grid_cell_three = columns.Column(width=720)
    grid_cell_four = columns.Column(width=720)
    grid_cell_five = columns.Column(width=720)
    grid_cell_six = columns.Column(width=720)
    grid_cell_seven = columns.Column(width=720)
    grid_cell_eight = columns.Column(width=720)
    grid_cell_nine = columns.Column(width=720)
    grid_cell_ten = columns.Column(width=720)
    grid_cell_eleven = columns.Column(width=720)
    grid_cell_twelve = columns.Column(width=720)
    content = columns.Column(width=960)
    footer = columns.Column(width=960)


@templates.attach('glitter_pages.Page')
class TwoColumn(PageLayout):
    billboard_top = columns.Column(width=1080)
    content = columns.Column(width=960)
    sidebar = columns.Column(width=720)
    footer = columns.Column(width=960)


@templates.attach('glitter_pages.Page')
class Map(PageLayout):
    billboard_top = columns.Column(width=1080)
    content = columns.Column(width=960)
    footer = columns.Column(width=960)


@templates.attach('glitter_news.Post')
class NewsPost(PageLayout):
    content = columns.Column(width=960)

    class Meta:
        template = 'glitter_news/post_detail.html'
