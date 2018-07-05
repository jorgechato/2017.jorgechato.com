from work.models import Profile


def header(request):
    return {"profile": Profile.objects.last()}
