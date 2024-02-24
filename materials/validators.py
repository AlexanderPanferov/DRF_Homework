import re

from rest_framework.serializers import ValidationError


class ValidateYoutubeUrl:
    """Проверка ссылки"""

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        reg = re.compile('https://youtube.com')
        tmp_val = dict(value).get(self.fields)
        if not bool(reg.match(tmp_val)):
            raise ValidationError('Неправильная ссылка')
