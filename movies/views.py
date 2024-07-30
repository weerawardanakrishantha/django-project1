from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

data={
    'movies':[
        {
            'id':2,
            'title':'jawan',
            'year':2023
                
        },
        {
            'id':3,
            'title':'raze',
            'year':2017
        }
    ]
        
}

def movies(request):
    return render(request, 'movies/movies.html',data)
