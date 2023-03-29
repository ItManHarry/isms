from django.core.mail import send_mail, BadHeaderError, EmailMessage, EmailMultiAlternatives
def do_send_mail():
    try:
        return send_mail('Test from Django',
              'This is a test mail from django...',
              'guoqian.cheng@hyundai-di.com',
              ['guoqian.cheng@hyundai-di.com'],
              fail_silently=False,
              html_message="<h2 style='color:red'>Html Message</h2>")
    except BadHeaderError:
        return 0
def send_mail_message():
    # email = EmailMultiAlternatives(
    #     subject='Test from django of EmailMessage',
    #     body="EmailMessage body content",
    #     to=['guoqian.cheng@hyundai-di.com'],
    #     cc=['guoqian.cheng@hyundai-di.com'],
    # )
    # email.attach_alternative('<p>This is an <strong>import</strong> message</p>', 'text/html')
    email = EmailMessage(
        subject='Test from django of EmailMessage',
        body='<p>EmailMessage body content, it is very <strong>IMPORT</strong></p>',
        to=['guoqian.cheng@hyundai-di.com'],
        cc=['guoqian.cheng@hyundai-di.com'],
    )
    email.content_subtype = 'html'
    email.attach_file('d:/data.xls')
    email.send()