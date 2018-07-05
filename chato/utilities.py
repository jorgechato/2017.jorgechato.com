import os
from chato.settings import MEDIA_ROOT


def content_name(instance, filename):
    print(instance)
    print(filename)
    image = os.path.exists(
        os.path.join(
            MEDIA_ROOT,
            filename,
        )
    )
    if image:
        os.remove(
            os.path.join(
                MEDIA_ROOT,
                filename,
            )
        )
    return image
