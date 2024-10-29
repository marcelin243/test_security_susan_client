from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

def send_email(from_email:None,to_email=None,subject=None,context=None,template=None):
    """_summary_
    Args:
        from_email (_type_): _string_ celui qui envoi
        to_email (_type_): _string_ destinateur
        subject (_type_): _string_ objet de l'email
        context (_type_): _dictionnaire {}_ contenu de la template
        template (_type_): _string_ qui pointe vers la template a utiliser  
    """
    html_message=render_to_string(template,context)
    message = EmailMultiAlternatives(subject, html_message, from_email, [to_email])
    message.attach_alternative(html_message, "text/html")
    message.send()   
 