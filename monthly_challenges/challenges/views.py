from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
        response_data = f"<h1>{monthly_challenges[month]}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month does not exist!")


def index(request):
    response_data = []

    for month in monthly_challenges:
        redirect_path = reverse("month-challenge", args=[month])
        response_data.append(
            f"<li><a href='{redirect_path}'>{month.title()}</a></li>"
        )

    response_data = ["<ul>"] + response_data + ["</ul>"]
    return HttpResponse("\n".join(response_data))
