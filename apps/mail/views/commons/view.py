# -*- coding: utf-8 -*-

from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
import json


class JSONResponseMixin(object):
    """
    A mixin that allows you to easily serialize simple data such as a dict or
    Django models.
    """
    content_type = "application/json"

    def get_response_content_type(self):
        if self.content_type is None:
            raise ImproperlyConfigured("%(cls)s is missing a content type. "
                                       "Define %(cls)s.content_type, or override "
                                       "%(cls)s.get_content_type()." % {
                                           "cls": self.__class__.__name__
                                       })
        return self.content_type

    def render_json_response(self, context_dict, status_code=None):
        """
        Limited serialization for shipping plain data. Do not use for models
        or other complex or custom objects.
        """
        json_context = json.dumps(context_dict, cls=DjangoJSONEncoder, ensure_ascii=False)
        response = HttpResponse(json_context, content_type=self.get_response_content_type())

        if status_code == 400:
            return HttpResponseBadRequest(response)
        else:
            return response

    def render_json_object_response(self, objects, **kwargs):
        """
        Serializes objects using Django's builtin JSON serializer. Additional
        kwargs can be used the same way for django.core.serializers.serialize.
        """
        json_data = serializers.serialize("json", objects, **kwargs)
        return HttpResponse(json_data, content_type=self.get_response_content_type())


class LoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        path = self.request.get_full_path()

        if self.request.user.is_authenticated():
            if path.startswith('/panel/admin'):
                if self.request.user.is_superuser:
                    return super(LoginRequiredMixin, self).dispatch(
                        self.request, *args, **kwargs)
                else:
                    messages.warning(self.request,
                                     "Usted no tiene permiso para ingresar a esta pagina",
                                     fail_silently=True)
                    return HttpResponseRedirect(
                        self.request.user.get_home_url())
            else:
                return super(LoginRequiredMixin, self).dispatch(self.request,
                                                                *args,
                                                                **kwargs)
        else:
            return super(LoginRequiredMixin, self).dispatch(
                request, *args, **kwargs)
