# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from .models import Document, DocumentForm
import wmi, os


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('file:list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

##class ListView(ListView):
##    templates_name = "list.html"
##    if request.method == 'POST':
##        form = DocumentForm(request.POST, request.FILES)
##        if form.is_valid():
##            newdoc = Document(docfile=request.FILES['docfile'])
##            newdoc.save()
##
##            # Redirect to the document list after POST
##            return HttpResponseRedirect(reverse('file:list'))
##    else:
##        form = DocumentForm()  # A empty, unbound form
##
##    # Load documents for the list page
##    documents = Document.objects.all()
    
    
