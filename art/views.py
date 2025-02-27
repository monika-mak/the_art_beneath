from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Art, Category
from .forms import ArtForm


# Create your views here.
def all_art(request):
    """
    A view to show all art, including sorting and search queries
    """

    art = Art.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    # Cofigure search query

    if request.GET:
        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            art = art.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                art = art.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"

            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            art = art.order_by(sortkey)

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse("art"))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query
            )
            art = art.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "art": art,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }

    return render(request, "art/art.html", context)


@login_required
def art_detail(request, art_id):
    """
    A view to show individual art pieces detail.
    """

    art = get_object_or_404(Art, pk=art_id)

    context = {
        "art": art,
    }

    return render(request, "art/art_detail.html", context)


@login_required
def add_art(request):
    """Add a art to the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ArtForm(request.POST, request.FILES)
        if form.is_valid():
            art = (
                form.save()
            )  # redirect to the product detail after art is added
            messages.success(request, "Successfully added art!")
            return redirect(reverse("art_detail", args=[art.id]))
        else:
            messages.error(
                request, "Failed to add art. Please ensure the form is valid."
            )
    else:
        form = ArtForm()

    template = "art/add_art.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_art(request, art_id):
    """Edit a art in the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    art = get_object_or_404(Art, pk=art_id)
    if request.method == "POST":
        form = ArtForm(request.POST, request.FILES, instance=art)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated an art piece Successfully!")
            return redirect(reverse("art_detail", args=[art.id]))
        else:
            messages.error(
                request,
                "Failed to update art. Please ensure the form is valid.",
            )
    else:
        form = ArtForm(instance=art)
        messages.info(request, f"You are editing {art.name}")

    template = "art/edit_art.html"
    context = {
        "form": form,
        "art": art,
    }
    return render(request, template, context)


@login_required
def delete_art(request, art_id):
    """Delete a art in the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    art = get_object_or_404(Art, pk=art_id)
    art.delete()
    messages.success(request, "Deleted an art piece Successfully!")

    return redirect(reverse("art"))
