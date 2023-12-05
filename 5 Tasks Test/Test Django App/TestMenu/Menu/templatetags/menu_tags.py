from django import template
from Menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('Menu/menu_item.html', takes_context=True)
def draw_menu(context, parent_item, current_url):
    child_items = MenuItem.objects.filter(parent=parent_item)
    return {'child_items': child_items, 'parent_item': parent_item, 'current_url': current_url, 'context': context}

