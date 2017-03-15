from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required(), name='dispatch')
class BaseCreateView(CreateView):
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_by = self.request.user
        instance.save()
        messages.success(self.request, "%s was successfully added." % self.form_class.Meta.model.__name__)
        return HttpResponseRedirect(self.get_redirect_url(instance))

    def get_redirect_url(self, instance):
        raise NotImplementedError("Method get_redirect_url should be implemented")


@method_decorator(login_required(), name='dispatch')
class BaseUpdateView(UpdateView):
    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your changes have been saved.")
        return HttpResponseRedirect(self.request.path)