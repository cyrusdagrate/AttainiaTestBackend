from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    
    users = [
    {
        "id": 0,
        "username": "ana",
        "last_login": "2019-08-20T22:15:09.926Z",
        "login_count": 0,
        "project_count": 12
    },
    {
        "id": 1,
        "username": "tim",
        "last_login": "2019-08-20T22:15:09.926Z",
        "login_count": 23,
        "project_count": 234
    },
    {
        "id": 23,
        "username": "kyle",
        "last_login": "2019-08-20T22:15:09.926Z",
        "login_count": 4,
        "project_count": 2354
    },
    {
        "id": 34,
        "username": "alex",
        "last_login": "2019-08-20T22:15:09.926Z",
        "login_count": 0,
        "project_count": 6563
    },
    {
        "id": 234,
        "username": "glenn",
        "last_login": "2019-08-20T22:15:09.926Z",
        "login_count": 1,
        "project_count": 3452
    },
    {
        "id": 633,
        "username": "cort",
        "last_login": "2019-08-20T22:15:09.926Z",
        "login_count": 1000,
        "project_count": 2345
    },
    {
        "id": 693,
        "username": "sean",
        "last_login": "2019-08-20T22:15:09.926Z",
        "login_count": 3,
        "project_count": 8654
    },
    {
        "id": 623,
        "username": "violet",
        "last_login": "2019-08-20T22:15:09.926Z",
        "login_count": 0,
        "project_count": 4028
    },
    {
        "id": 665,
        "username": "nik",
        "last_login": "2019-08-20T22:15:09.926Z",
        "login_count": 0,
        "project_count": 4428
    }
]

    # context = {'comments' : comments}
    
    # return render(request, 'index.html', context)
    
    return JsonResponse({'users' : users})