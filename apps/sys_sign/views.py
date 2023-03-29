from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from mail_tool import do_send_mail
def do_login(request):
    login_message = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print('User name : {}, password {}.'.format(username, password))
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            print('Authenticate succeeded!!!')
            do_send_mail()
            return redirect(reverse('syscode:wordbook_index'))
        else:
            print('Authenticate failed!!!')
            login_message = 'User name or password is not correct!'
    return render(request, 'sys_sign/login.html', context=dict(login_message=login_message))
def do_logout(request):
    logout(request)
    return redirect(reverse('sys_sign:login'))