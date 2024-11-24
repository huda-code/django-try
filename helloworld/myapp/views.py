from django.shortcuts import render
from django.http import JsonResponse

# View for JSON response
def hello_world_json(request):
    return JsonResponse({"Message": "Hello World!"})

# View for HTML response
def hello_world_html(request):
    return render(request, 'myapp/hello.html')  # Ensure the template path is correct
