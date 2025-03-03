from django.shortcuts import render


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def custom_500(request):
    return render(request, '500.html', status=500)


def custom_403(request, template_name='403.html'):
    return render(request, template_name, status=403)