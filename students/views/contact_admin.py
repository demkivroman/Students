# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django import forms
from django.core.mail import send_mail

from studentsdb.settings import ADMIN_EMAIL
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ContactForm(forms.Form):   

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(ContactForm, self).__init__(*args, **kwargs)
         
        # this helper object allows us to customize form
        self.helper = FormHelper()


        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
       # self.helper.form_action = reverse('contact_admin')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # form buttons
        self.helper.add_input(Submit('send_button',u'Надіслати'))  

    from_email = forms.EmailField(
        label = u"Ваша Емейл адреса")

    subject = forms.CharField(
        label = u"Заголовок листа",
        max_length=128)

    message = forms.CharField(
        label = u"Текст повідомлення",
        max_length = 2560,  
        widget = forms.Textarea)



class ContactView(FormView):
    template_name = 'contact_form/contact_form.html'
    form_class = ContactForm 
    success_url =  reverse_lazy('contact_admin')
    
    # This method call for valid data

    def form_valid(self, form):
        
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['from_email']

        send_mail(subject, message, from_email, [ADMIN_EMAIL])
        messages.info(self.request, u"Лист надіслано, успішно :)")
    
        return super(ContactView, self).form_valid(form)  




























       

