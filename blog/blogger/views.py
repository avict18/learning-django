from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First blog post content',
        'date_posted': 'August 27, 2024',
        },
    {
            'author': 'John Doe',
            'title': 'Blog Post 2',
            'content': 'Second blog post content',
            'date_posted': 'August 28, 2024'
            }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blogger/home.html',context)