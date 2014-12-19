from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from apps.mail.models.Template import Template
from apps.mail.models.Business import Business


class TemplateCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_show_errors = True
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        super(TemplateCreateForm, self).__init__(*args, **kwargs)

    def set_business(self, business):
        self.fields['business'].choices = [(business.id, business.name)] + list(Business.objects.exclude(
            pk=business.id).values_list('id', 'name'))

    class Meta:
        exclude = ['status']
        model = Template