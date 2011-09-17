from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.simple import direct_to_template
from django.db.models.loading import get_model
from forms import JoinRequestForm, JoinResponseForm
from models import JoinRequest


@login_required
def submit_request(request, template_name='join/join_request.html',
                   content_type=None, success_url=None, extra_context=None,
                   **kwargs):
    extra_context = extra_context or {}
    if content_type is None:
        content_type = settings.DEFAULT_REALM_TYPE
    app, model = content_type.split('.')
    realm = get_object_or_404(get_model(app, model), **kwargs)
    req = JoinRequest.objects.get_or_create(realm=realm, user=request.user)
    form = JoinRequestForm(request.POST or None, instance=req)
    if form.is_valid():
        req = form.save()
        redirect(success_url or realm.get_absolute_url())
    extra_context['form'] = form
    return direct_to_template(request, template_name, extra_context)


@login_required
def respond_request(request, template_name='join/join_response.html',
                    content_type=None, success_url=None, extra_context=None,
                    **kwargs):
    extra_context = extra_context or {}
    if content_type is None:
        content_type = settings.DEFAULT_REALM_TYPE
    app, model = content_type.split('.')
    realm = get_object_or_404(get_model(app, model), **kwargs)
    if not request.user.has_perm('{0}.host_{1}'.format(app, model), realm):
        return HttpResponseForbidden("<h1>403 Forbidden</h1>")
    req = JoinRequest.objects.get_or_create(realm=realm, user=request.user)
    form = JoinResponseForm(request.POST or None, instance=req)
    if form.is_valid():
        req = form.save()
        if request.is_ajax():
            return # FIXME: some ajax response
        redirect(success_url or realm.get_absolute_url())
    extra_context['form'] = form
    return direct_to_template(request, template_name, extra_context)
