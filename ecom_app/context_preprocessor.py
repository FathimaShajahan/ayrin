from . models import Category

def menu_Links(request):
    
    Links = Category.objects.all()
    return dict(Links=Links)