from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

BASE_URL = "https://dirtybits.vercel.app/"


class send_verification_mail(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        subject = "Welcome to the DirtyBits World"
        link = BASE_URL + "auth/verifyUser/" + data["verification_code"]
        # message = f"Hi {data['username']}, Thank You for registering with DirtyBits. \n\nTo activate your account please click on the link given below. \n{link} \n\nTeam DirtyBits @ 2021"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [
            data["email"],
        ]
        context = {"username": data["username"], "activation_link": link}
        msg_html = render_to_string("verificationmail.html", context=context)
        msg = EmailMessage(
            subject=subject, body=msg_html, from_email=email_from, to=recipient_list
        )
        msg.content_subtype = "html"
        msg.send()
        return Response(status=status.HTTP_200_OK)


class send_pass_change_email(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        subject = "DirtyBits | Password Change"
        link = BASE_URL + "auth/resetpassword/" + data["code"]
        # message = f"Hi {data['username']}, Thank You for registering with DirtyBits. \n\nTo activate your account please click on the link given below. \n{link} \n\nTeam DirtyBits @ 2021"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [
            data["email"],
        ]
        context = {"username": data["username"], "activation_link": link}
        msg_html = render_to_string("verificationmail.html", context=context)
        msg = EmailMessage(
            subject=subject, body=msg_html, from_email=email_from, to=recipient_list
        )
        msg.content_subtype = "html"
        msg.send()
        return Response(status=status.HTTP_200_OK)
