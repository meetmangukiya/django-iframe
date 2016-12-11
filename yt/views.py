from django.shortcuts import render
from django.http import HttpResponse

def play(request):
    """
    View function for the `/play` endpoint.
    """
    # Setting variables
    ids = set(request.GET.getlist("id", []))
    if ids == []:
        return HttpResponse("You seem to have been stumbled upon a website that is " + 
                            "probably not for you unless you were invited too! " +
                            "Anyways, thanks for passing by!")
    title = None

    # Constructing the context
    context = {
        "ids": ids,
        "title": title if title else "FieryBit | yTif",
    }

    return render(request, 'yt/iframe.html', context)
