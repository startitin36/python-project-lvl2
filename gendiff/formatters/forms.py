from gendiff.formatters import stylish
from gendiff.formatters import json
from gendiff.formatters import plain

forms = {
    'stylish': stylish.form_view,
    'plain': plain.form_view,
    'json': json.form_view
}
