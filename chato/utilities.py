import os
from slugify import slugify
from chato.settings import MEDIA_ROOT
from django.utils.deconstruct import deconstructible


@deconstructible
class UploadPath:

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]

        if hasattr(instance, 'slug'):
            filename = '{}.{}'.format(instance.slug, ext)
        elif hasattr(instance, 'title'):
            filename = '{}.{}'.format(instance.title, ext)
        elif hasattr(instance, 'company_name'):
            filename = '{}.{}'.format(slugify(instance.company_name), ext)
        else:
            filename = '{}.{}'.format(instance.pk, ext)

        image = os.path.join(
            self.path,
            filename,
        )

        file_path = os.path.join(MEDIA_ROOT, image)
        if os.path.exists(file_path):
            os.remove(file_path)

        return image
