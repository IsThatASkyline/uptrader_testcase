from django import template
from testcase.models import *


register = template.Library()

@register.inclusion_tag('testcase/cats.html')
def draw_menu(menu):
    cats = Category.objects.filter(menu__title=menu).select_related('parent')
    primary_cats = [cat for cat in cats if not cat.parent]
    return {'primary_cats': primary_cats, 'menu': menu}

@register.inclusion_tag('testcase/list_categories.html')
def draw_selected_cat(menu, pk):
    q = Category.objects.filter(menu__title=menu).select_related('parent')
    primary_cats = [cat for cat in q if not cat.parent]
    subcats = [cat for cat in q if cat.parent is not None and cat.parent.title == pk]
    tree = []
    for cat in q:
        if cat.title == pk:
            target_cat = cat
    while True:
        if target_cat.parent is None:
            tree.append(target_cat)
            break
        else:
            tree.append(target_cat)
            target_cat = target_cat.parent
    return {'q': q, 'primary_cats': primary_cats, 'subcats': subcats, 'menu': menu, 'target_cat': pk, 'tree': tree}



@register.inclusion_tag('testcase/infinite_tsukuemi.html')
def draw_subcats(menu, q, tree):
    current_cat = tree[-1]
    tree = tree[0:-1]
    target_cat = tree[0]
    cats = []
    subcats = []
    for cat in q:
        if cat.parent:
            if cat.parent == current_cat:
                cats.append(cat)
            elif cat.parent == target_cat:
                subcats.append(cat)
    return {'q': q, 'menu': menu, 'cats': cats, 'tree': tree, "current_cat": current_cat, 'target_cat': target_cat, 'subcats': subcats}



