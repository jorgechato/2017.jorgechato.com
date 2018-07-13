import os
from slugify import slugify
from chato.settings import MEDIA_ROOT


def content_name(path):

    def wrapper(instance, filename):
        ext = filename.split('.')[-1]

        if instance.slug:
            filename = '{}.{}'.format(instance.slug, ext)
        elif instance.title:
            filename = '{}.{}'.format(instance.title, ext)
        elif instance.company_name:
            filename = '{}.{}'.format(slugify(instance.company_name), ext)
        elif instance.email:
            filename = '{}.{}'.format(slugify(instance.email), ext)
        else:
            filename = '{}.{}'.format(instance.pk, ext)

        image = os.path.join(
            path,
            filename,
        )

        file_path = os.path.join(MEDIA_ROOT, image)
        if os.path.exists(file_path):
            os.remove(file_path)

        return image

    return wrapper
