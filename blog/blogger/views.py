from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam minus, error optio numquam sequi amet autem iste assumenda necessitatibus alias repellat culpa et quas, tempora eius eveniet ipsam ducimus dolorem?',
        'date_posted': 'August 27, 2024',
        },
    {
            'author': 'John Doe',
            'title': 'Blog Post 2',
            'content': 'tested well ',
            'date_posted': 'August 28, 2024'
            }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blogger/home.html',context)

def about(request):
    return render(request, 'blogger/about.html',{'title':'about-page    '})  # render the about.html template