from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.template.base import VariableDoesNotExist
from random import randint

register = template.Library()


@register.filter(is_safe=True)
def citation(texte):
    res =  "&laquo; %s &raquo;"%(escape(texte))
    return mark_safe(res)

@register.filter
def smart_truncate(text,nb):
    try:
        nb = int(nb)
    except ValueError:
        return text

    if(len(text)<=nb):
        return text

    text = text[:nb+1]

    if text[-1] == ' ':
        return text[:-1]
    else:
        return ' '.join(text.split(' ')[:-1])+'...'

@register.filter
def has_group(user, group_name):
    return user.groups.filter(name = group_name).exists()


# class RandomNode(template.Node):
#     def __init__(self, begin, end):
#         self.begin = begin
#         self.end = end
#
#     def render(self, context):
#         not_exist = False
#         try:
#             begin = template.Variable(self.begin).resolve(context)
#             begin = int(begin)
#         except (VariableDoesNotExist, ValueError):
#             not_exist = self.begin
#
#         try:
#             end = template.Variable(self.end).resolve(context)
#             end = int(end)
#         except (VariableDoesNotExist, ValueError):
#             not_exist = self.end
#
#         if not_exist:
#             raise template.TemplateSyntaxError("%s n'existe pas ou n'est pas un entier" %(not_exist))
#
#         if begin>end:
#             raise template.TemplateSyntaxError('Le premier argument doit etre inférieur au deuxieme')
#
#         return str(randint(begin, end))
#
# @register.tag
# def random(parser, token):
#     try:
#         name, begin, end = token.split_contents()
#
#     except ValueError:
#         msg = "Le tag %s doit contenir deux arguments !"%(token.split_contents()[0])
#         raise template.TemplateSyntaxError(msg)
#
#
#     return RandomNode(begin, end)

@register.simple_tag
def random(begin, end):
    try:
        begin, end = int(begin), int(end)
    except ValueError:
        raise template.TemplateSyntaxError('Bad arugment type in tag random')

    if(begin>end):
        raise template.TemplateSyntaxError('begin>end in tag random')

    return randint(begin, end)
