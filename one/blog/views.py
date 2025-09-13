from django.shortcuts import render
from django.http import Http404

users = [
    {
        'username' :'poriya60',
        'name' : 'poriya',
        'email' : 'poriya@gmail.com',
        'phone_number' : '0123456789',
        'city' : 'karaj'

    },
    {
        'username': 'ali40',
        'name': 'ali',
        'email': 'ali@gmail.com',
        'phone_number': '0123456789',
        'city': 'teh'

    },
    {
        'username': 'sara20',
        'name': 'sara',
        'email': 'sara20@gmail.com',
        'phone_number': '0123456789',
        'city': 'shomal'
    },

]








def all_user(request, username):
    for user in users:
        if user['username'] == username:
            return render(request, 'blog/all_user.html', context={'user': user})
    raise Http404('user is not found')




