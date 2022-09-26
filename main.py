import smtplib
my_email = "sagargupta507@yahoo.com"
password = "kumar@098735"
with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="sagargupta800016@gmail.com",
        msg="subject:hello\n\nhello sagar come to my bedroom and please fuck hard me."
    )