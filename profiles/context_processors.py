from profiles.models import Profile
from chato.settings import email


def header(request):
    return {"profile": Profile.objects.get(email=email)}
