from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    month: f"Challenge for {month.title()}"
    for month in [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
    ]
}


def index(request):
    return render(
        request,
        "challenges/index.html",
        {"months": monthly_challenges.keys()},
    )


def monthly_challenge_by_number(request, month):
    try:
        forward_month = list(monthly_challenges.keys())[month - 1]

        redirect_path = reverse(
            "month-challenge", args=[forward_month]
        )  # /challenge/month
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("This month does not exist!")


def monthly_challenge(request, month):
    try:
        return render(
            request,
            "challenges/challenge.html",
            {"month": month, "challenge": monthly_challenges[month]},
        )
    except:
        raise Http404()
