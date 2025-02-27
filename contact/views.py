from django.shortcuts import render, redirect
from .forms import ContactRequestForm


def contact_view(request):
    if request.method == "POST":
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_success")  # Redirect to success page
    else:
        form = ContactRequestForm()

    return render(request, "contact/contact_form.html", {"form": form})


def contact_success(request):
    return render(request, "contact/contact_success.html")
