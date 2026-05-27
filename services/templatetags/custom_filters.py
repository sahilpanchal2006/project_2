from django import template
from django.forms import Textarea, Select, ClearableFileInput, FileInput

register = template.Library()

@register.filter(name='split')
def split(value, key):
    """
    Splits a string by a given delimiter.
    Usage: {{ string_value|split:"," }}
    """
    if not value:
        return []
    return [item.strip() for item in value.split(key)]

@register.filter(name='is_textarea')
def is_textarea(field):
    """
    Returns True if the field's widget is a Textarea.
    """
    return isinstance(field.field.widget, Textarea)

@register.filter(name='is_select')
def is_select(field):
    """
    Returns True if the field's widget is a Select widget.
    """
    return isinstance(field.field.widget, Select)

@register.filter(name='is_file')
def is_file(field):
    """
    Returns True if the field's widget is a File widget.
    """
    return isinstance(field.field.widget, (ClearableFileInput, FileInput))


@register.filter(name='read_time')
def read_time(html_content):
    """
    Calculates estimated reading time in minutes based on word count.
    Assumes 200 words per minute.
    """
    if not html_content:
        return 1
    # Strip HTML tags
    import re
    clean_text = re.sub(r'<[^>]+>', '', html_content)
    words = clean_text.split()
    word_count = len(words)
    minutes = max(1, round(word_count / 200))
    return minutes


