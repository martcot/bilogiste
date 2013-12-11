#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, Template, RequestContext
from django.shortcuts import render_to_response
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from app.forms import ContactForm

def index(request):

	return render_to_response('index.html',{},context_instance=RequestContext(request))

def contact(request):

	if request.POST:
		contactForm = ContactForm(request.POST)
		if contactForm.is_valid():
			try:
				message = render_to_string('app/contactEmail.html', {'form': request.POST,}, context_instance=RequestContext(request))
				msg = EmailMultiAlternatives('Contact' + settings.EMAIL_SUFFIX, message, settings.SEND_EMAILS_FROM, [settings.SEND_EMAILS_TO])
				msg.attach_alternative(message, "text/html")
				msg.send()
				contactForm = ContactForm()
				contactForm.message = _(u"Votre message a bien été envoyé.")
				contactForm.mtitle = _(u"Envoit réussi")
				contactForm.mtype = "success"
				
			except :
				contactForm.message = _(u"Une erreur s'est produite lors de l'envoit, veuillez contacter l'administration.")
				contactForm.mtitle = _(u"Erreur")
				contactForm.mtype = "danger"
			
		else:
			contactForm.message = _(u"Tous les champs sont obligatoires.")
			contactForm.mtitle = _(u"Erreur")
			contactForm.mtype = "danger"
			
	else:
		contactForm = ContactForm()
	
	return render_to_response('contact.html',{"contactForm":contactForm,
											  },context_instance=RequestContext(request))
