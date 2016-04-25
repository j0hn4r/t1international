from django import template
from django.shortcuts import resolve_url
from django.utils.six.moves import filter as ifilter

from glitter.pages.models import Page

register = template.Library()


def resolve_page(to, *args, **kwargs):
    """
    Resolve an object/string to a Page.

    The arguments could be:

        * A page: will be returned back immediately.

        * Any other model: the model's `get_absolute_url()` function will be
          called.

        * A view name, possibly with arguments: `urlresolvers.reverse()` will
          be used to reverse-resolve the name.

        * A URL string.

    For anything other than a page, a lookup is done on the URL of the object or
    view, and a Page is returned if it exists. If a page doesn't exist then
    it'll return None.
    """

    # Don't bother with a lookup if we're given None or an empty string
    if not to:
        return None

    try:
        return Page.objects.get(url=resolve_url(to, *args, **kwargs))
    except Page.DoesNotExist:
        pass

    return None


@register.assignment_tag
def get_root_pages(current_page=None):
    current_page = resolve_page(current_page)
    page_list = []

    # Find the root page so the template can highlight it
    if current_page:
        root_page = current_page.get_root()
    else:
        root_page = None

    page_qs = Page.objects.root_nodes().filter(
        show_in_navigation=True, published=True).exclude(current_version=None)

    for i in page_qs:
        page_list.append((i, i == root_page))

    return page_list


@register.assignment_tag
def get_pages_at_level(current_page, level=1):
    current_page = resolve_page(current_page)

    if not current_page:
        return []

    page_and_ancestors = list(current_page.get_ancestors(include_self=True))

    # Page isn't deep enough to show this level of navigation
    if level > current_page.level + 1:
        return []

    parent_page = page_and_ancestors[level - 1]
    page_list = []

    page_qs = parent_page.get_children().filter(
        show_in_navigation=True, published=True).exclude(current_version=None)

    for i in page_qs:
        page_list.append((i, i in page_and_ancestors))

    return page_list


@register.assignment_tag
def tree_from_root(current_page=None):
    current_page = resolve_page(current_page)
    tree = None

    if current_page:
        root_page = current_page.get_root()
        tree = root_page.get_descendants()

    return tree


@register.assignment_tag
def get_page_ancestor_ids(current_page=None):
    current_page = resolve_page(current_page)
    ancestors = []

    if current_page:
        ancestors = current_page.get_ancestors(include_self=True).values_list('id', flat=True)

    return ancestors


@register.inclusion_tag('glitter/navigation/level.html')
def primary_navigation(page=None, css_class='primary'):
    """ Render a list of primary level pages. """
    return {
        'page_list': get_root_pages(current_page=page),
        'css_class': css_class,
    }


@register.inclusion_tag('glitter/navigation/level.html')
def navigation_at_level(page=None, level=1, css_class=None):
    """
    Render a list of pages at a specific navigation level.

    This is an inclusion tag mostly used by secondary_navigation and
    tertiary_navigation - however it exists here incase additional levels of
    navigation are needed.

    At this point it's recommended that you might want to use a page tree for
    navigation instead.
    """
    # Use the level number if this isn't a named navigation level
    if css_class is None:
        css_class = 'level-{}'.format(level)

    return {
        'page_list': get_pages_at_level(current_page=page, level=level),
        'css_class': css_class,
    }


@register.inclusion_tag('glitter/navigation/level.html')
def secondary_navigation(page=None, css_class='secondary'):
    """ Render a list of secondary level pages. """
    return navigation_at_level(page=page, css_class='secondary')


@register.inclusion_tag('glitter/navigation/level.html')
def tertiary_navigation(page=None, css_class='tertiary'):
    """ Render a list of tertiary level pages. """
    return navigation_at_level(page=page, level=2, css_class='tertiary')


def tree_nav_render(queryset, page, root_level, css_class):
    # Avoiding another queryset, but we need to find out if any of the root pages for this
    # navigation are visible - otherwise we don't show it.
    root_pages = ifilter(lambda obj: obj.level == root_level, queryset)
    visible_root_pages = ifilter(
        lambda obj: obj.show_in_navigation and obj.published and obj.current_version_id, root_pages)

    if any(visible_root_pages):
        ancestor_ids = get_page_ancestor_ids(current_page=page)
    else:
        # No root level pages are visible, so don't show the navigation at all
        queryset = Page.objects.none()
        ancestor_ids = []

    return {
        'page_tree': queryset,
        'ancestor_ids': ancestor_ids,
        'css_class': css_class,
        'root_level': root_level,
    }


@register.inclusion_tag('glitter/navigation/tree.html')
def tree_navigation(page=None, max_depth=2, css_class='tree'):
    page = resolve_page(page)

    # Must be all pages which are unpublished or hidden from navigation - can't filter out any at
    # this point otherwise we'll potentially have holes in the page tree. This gets filtered out in
    # the template instead.
    page_qs = Page.objects.exclude(level__gt=max_depth)

    return tree_nav_render(queryset=page_qs, page=page, root_level=0, css_class=css_class)


@register.inclusion_tag('glitter/navigation/tree.html')
def subtree_navigation(page, start_level=1, max_depth=2, css_class='tree'):
    page = resolve_page(page)

    # Sane defaults - incase we can't render this subtree
    page_qs = Page.objects.none()
    tree_root = None
    root_level = 0

    # Current page must be
    if page and page.level >= start_level - 1:
        try:
            tree_root = page.get_ancestors(include_self=True)[start_level-1]
            page_qs = tree_root.get_descendants()
            root_level = tree_root.level + 1
        except IndexError:
            pass

    # Filter out levels we don't need now we have the appropriate queryset
    max_level = root_level + max_depth
    page_qs = page_qs.exclude(level__gt=max_level)

    return tree_nav_render(queryset=page_qs, page=page, root_level=root_level, css_class=css_class)
