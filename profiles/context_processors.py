from profiles.models import Profile
from chato.local_settings import email


def header(request):
    return {"profile": Profile.objects.get(email=email)}
