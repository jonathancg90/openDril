from django.forms import ModelForm
from mail.models.List import List
from crispy_forms.helper import FormHelper


class ListCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_show_errors = True
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        super(ListCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        exclude = ['status']
        model = List