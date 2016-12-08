from django.shortcuts import render

def play(request):
    """
    View function for the `/play` endpoint.
    """
    # Setting variables
    ids = request.GET.getlist("id", [])
    title = None

    # Constructing the context
    context = {
        "ids": ids,
        "title": title if title else "FieryBit | yTif",
    }

    return render(request, 'yt/iframe.html', context)
