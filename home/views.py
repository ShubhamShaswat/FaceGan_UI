from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
import numpy as np
import os
from django.conf import settings
from django.template import loader

from django.utils.encoding import smart_str
from .models import GeneratedImages
import io
import base64
import cv2
import json
import requests
from PIL import Image
from django.core.files import File

IMAGE_URL ='/static/images/4c1.jpg'

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#this will
def to_base64(frame):
     ret, frame_buff = cv2.imencode('.jpg', frame)
     frame_b64 = base64.b64encode(frame_buff)
     return frame_b64



context={'img': IMAGE_URL }
filename = 'media/img.jpg'

def index(request):
    if request.method == 'POST':
        #this will donwload the generated image
        if request.POST.get('download_btn',None):
            print('download')
            path_to_file = 'media/img.jpg'
            fname = 'img.jpg'
            fl = open(path_to_file,'rb').read()
            response = HttpResponse(fl, content_type='image/jpeg')
            response['Content-Disposition'] = "attachment; filename=%s" % fname

            return response

        #this will generate the fake face and save it to the database
        #if request.POST.get('generate_btn',None) :
        #frame = np.uint8(np.random.randn(128,128))*255
        rs = rest_request(seed=np.random.normal(size=(1,100)))

        frame = np.array(rs.json()['predictions'][0])[...,::-1]*255.
        cv2.imwrite(filename, frame) #to dave the file
        frame_b64 = to_base64(frame)
        #saving  image to models
        #genImg = Image.open()
        newImg = GeneratedImages()
        newImg.img.save('img.jpg',File(open(filename,'rb')))
            #update context dict with new value
        #context.update({'img':('data:image/jpeg;base64, '+ frame_b64.decode("utf-8"))})
        html_template = loader.get_template( 'includes/imageDiv.html')
        return HttpResponse(html_template.render({'img':('data:image/jpeg;base64, '+ frame_b64.decode("utf-8"))}, request))
            #return HttpResponseRedirect('')

        """
        #this will donwload the generated image
        if request.POST.get('download_btn',None):
            path_to_file = 'media/img.jpg'
            fname = 'img.jpg'
            fl = open(path_to_file,'rb').read()
            response = HttpResponse(fl, content_type='image/jpeg')
            response['Content-Disposition'] = "attachment; filename=%s" % fname

            return response
        """
    else:
        return render(request, 'home/index2.html',context)

def about(request) :
    return HttpResponse('About')


#REST request API
def rest_request(seed, url=None):
    if url is None:
        #url = "http://34.71.48.161:8501/v1/models/my_model:predict"
        url = "http://172.17.0.2:8501/v1/models/my_model:predict"
    payload = json.dumps({"signature_name": "serving_default","instances": seed.tolist()})
    response = requests.post(url,data=payload)
    return response
