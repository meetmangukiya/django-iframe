from django.shortcuts import render
from django.http import HttpResponse

def play(request):
    """
    View function for the `/` endpoint.
    """
    supported_quality = {
        'low': 'small',
        'medium': 'medium',
        'high': 'large',
        'hd': 'hd720',
        'hq': 'hd1080',
        'hr': 'highres'
        'default': 'default'
    }

    # Setting variables
    ids = set(request.GET.getlist("id", []))
    quality = request.GET.get("quality", "default")
    if not ids:
        return HttpResponse("You seem to have been stumbled upon a website that is " +
                            "probably not for you unless you were invited too! " +
                            "Anyways, thanks for passing by!")
    title = None

    # Constructing the context
    context = {
        "ids": ids,
        "title": title if title else "FieryBit | yTif",
        "quality": supported_quality[quality]
    }

    return render(request, 'yt/iframe.html', context)
