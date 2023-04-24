from django.shortcuts import render
from .forms import ImageForm


def image_view(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            img_obj = form.instance

            return render(request, 'image_form.html', context={'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'image_form.html', context={'form': form})











