from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from mail_tool import do_send_mail, send_mail_message, send_mail
from syscode.models import WordBook
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
            # s = do_send_mail()
            # print('Send mail result is : ', s)
            wordbooks = WordBook.objects.all().order_by('-name')
            context = {'wordbooks': wordbooks}
            # send_mail_message(context)
            send_mail('Send mail by Thread',
                      ['guoqian.cheng@hyundai-di.com'],
                      'mails/test.html', context,
                      ['guoqian.cheng@hyundai-di.com'],
                      'Email text body.', 'd:/data.xls')
            return redirect(reverse('syscode:wordbook_index'))
        else:
            print('Authenticate failed!!!')
            login_message = 'User name or password is not correct!'
    return render(request, 'sys_sign/login.html', context=dict(login_message=login_message))
def do_logout(request):
    logout(request)
    return redirect(reverse('sys_sign:login'))