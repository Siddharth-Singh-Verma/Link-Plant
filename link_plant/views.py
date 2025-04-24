from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import  Profile, Link
# Create your views here.

def landing_view(request):
    # Replace 'your-slug-here' with your actual profile slug or dynamically get it
    my_profile = Profile.objects.first()  # Or filter for the current user
    return render(request, 'link_plant/landing.html', {'my_profile': my_profile})


class LinkListView(ListView):
    model = Link # this will use the default template name: link_list.html
    #(modelname_list.html)

class LinkCreateView(CreateView):
    # functional way : create forms.py file & form
    # check if this was a post or get request
    # return an empty form or or save the form data
    # class based way : use CreateView ,it expects template model_form -> link_form.html
    #(model_name_form.html)
    #means it auto render that template so you create it
    model = Link
    fields = "__all__"
    success_url = reverse_lazy('link-list')

class LinkUpdateView(UpdateView):
    # create a form
    # check if a get request or a put request
    # either render the form or update and save in our db
    # use UpdateView ,it expects template model_form -> link_form.html same as create
    model = Link
    fields = ['text','url']
    success_url = reverse_lazy('link-list')

class LinkDeleteView(DeleteView):
    # take in a id/pk of an object 
    # query to db for that object
    # check if it exists -> delete the object
    # return some template or forward to user to some url
    # use DeleteView: expects template model_confirm_delete -> link_confirm_delete.html
    model = Link
    success_url = reverse_lazy('link-list')
    # form to submit to delete the item
    # expect a template name model_confirm_delete.html
    # link_confirm_delete.html

def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    context = {
        "profile": profile,
        "links": links
    }
    return render(request, 'link_plant/profile.html', context)