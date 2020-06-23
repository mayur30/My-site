from django.shortcuts import render

# Create your views here.
def My_first_blog(request):
    return render(request,'blogs/post_list.html')
