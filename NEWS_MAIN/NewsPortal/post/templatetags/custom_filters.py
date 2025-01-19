from django import template

register = template.Library()


@register.filter()
def censore(value):
    try:
        value_split = value.split()
        result = ''
        for i in value_split:
            if i[0].isupper():
                i = i[0] + '*' * (len(i) - 1)
            result += i + ' '
    except ValueError:
        print('Применяется тоько к строковым значениям!')

    else:
        return result.strip()
