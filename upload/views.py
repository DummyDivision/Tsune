from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import os
import tempfile
import uuid
import shutil
from forms import UploadFileForm
from cardimporter.importer import AnkiImporter
from os import path,removedirs
from tsune.settings.base import PROJECT_DIR

TEMP_DIR = PROJECT_DIR + "/temp"

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'],request.user)
            return HttpResponseRedirect(reverse("deck:deck_list") )
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', RequestContext(request,{'form': form}))



def handle_uploaded_file(f, user):
    # TODO Check if file is actually Anki File beforehand
    temp_path = tempfile.mkdtemp()
    file_path = temp_path + "/" + f.name
    with open(file_path, 'w') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    anki = AnkiImporter()
    try:
        anki.importCollection(file_path,user)
    finally:
        shutil.rmtree(temp_path, ignore_errors=True)

