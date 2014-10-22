from django import forms
from crispy_forms.helper import FormHelper

from apps.mail.models.Category import Category
from apps.mail.models.ListDetail import ListDetail


class ListDetailCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_show_errors = True
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        super(ListDetailCreateForm, self).__init__(*args, **kwargs)

    def set_category(self, _list):
        self.fields['category'].choices = [(None, '--------------')] + list(Category.objects.filter(
            list=_list.id).values_list('id', 'name'))

    def set_category_update(self, _list, category):
        self.fields['category'].choices = [(category.id,category.name)] + list(Category.objects.filter(
            list=_list.id).exclude(pk=category.id).values_list('id', 'name'))

    class Meta:
        exclude = ['status', 'list']
        model = ListDetail