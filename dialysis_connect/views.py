from django.shortcuts import render


def custom_404(request, exception):
    """Custom 404 error page."""
    return render(request, "404.html", status=404)


def custom_500(request):
    """Custom 500 error page."""
    return render(request, "500.html", status=500)


def custom_403(request, template_name="403.html"):
    """Custom 403 error page."""
    return render(request, template_name, status=403)
