from django import forms
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from movie.models import Movie


class ContactForm(forms.Form):
	name = forms.CharField(label=_("Name"), max_length=255)
	email = forms.EmailField(label=_("Email"))
	phone = forms.IntegerField(label =_("Phone"))
	body = forms.CharField(label=_("Body"), widget = forms.Textarea)


class ContactView(FormView):
	template_name = "contacts.html"
	form_class = ContactForm
	success_url = reverse_lazy('contact-us')
	
	def form_valid(self, form):
		# message = "{email} said: ".format(
		# 	email=form.cleaned_data.get('email'))
		# message += "\n\n{0}".format(form.cleaned_data.get('body'))
		# send_mail(
		# 	subject=form.cleaned_data.get('theme').strip(),
		# 	message=message,
		# 	from_email=form.cleaned_data.get('email'),
		# 	recipient_list=['e_marshev@mail.ru'],
		# )

		send_mail(
			message=form.cleaned_data.get('body'),
			from_email=form.cleaned_data.get('email'),
			recipient_list=['e_marshev@mail.ru'],
		)
		messages.success(self.request, 'Сообщение отправлено.')		
		return super(ContactView, self).form_valid(form)

class HomePageView(TemplateView):
	template_name = "index.html"
	model = Movie

	def get_context_data(self, **kwargs):
		context = super(HomePageView, self).get_context_data(**kwargs)
		context['movies'] = Movie.objects.filter(media_content='m')
		context['serials'] = Movie.objects.filter(media_content='s')
		context['animes'] = Movie.objects.filter(media_content='a')
		context['tvs'] = Movie.objects.filter(media_content='t')

		return context

