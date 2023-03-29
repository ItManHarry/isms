from django.core.mail import send_mail
def do_send_mail():
    send_mail('Test from Django',
              'This is a test mail from django...',
              'guoqian.cheng@hyundai-di.com',
              ['guoqian.cheng@hyundai-di.com'],
              fail_silently=False,
              html_message="<h2 style='color:red'>Html Message</h2>")