from sendgrid import Mail, SendGridAPIClient

message = Mail(
    from_email="DnaldTrump.usa.president@gmail.com",
    to_emails="zh.cse18@gmail.com",
    subject='Just Fun',
    html_content="Hello I am a great fucker people say me "
)
sg = SendGridAPIClient('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')
response =sg.send(message)
print(response)