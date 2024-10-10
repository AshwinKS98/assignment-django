from django.shortcuts import render
from django.http import JsonResponse
from signal_app.models import Rectangle  

def homepage(request):
    return render(request,'homepage.html')

def rectangle_list(request):
    # Fetch all instances of Rectangle
    rectangles = Rectangle.objects.all()

    # Create a list to hold the output
    output = [{'length': rectangle.length, 'width': rectangle.width} for rectangle in rectangles]

    # Return the output as JSON
    return JsonResponse(output, safe=False)