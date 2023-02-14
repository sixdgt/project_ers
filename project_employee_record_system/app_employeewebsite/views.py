from django.shortcuts import render

# Create your views here.
def demo(request):
    context = {
        "class_name": "Django Class",
        "date": "2023-02-14",
        "day": "Tuesday"
    }
    return render(request, 'demo.html', context)