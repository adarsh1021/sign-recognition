# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
import base64

# Create your views here.

@csrf_exempt
def index(request):
	
	return render(request, 'train/index.html')

@csrf_exempt
def upload(request):
	context_dict = {'zero': len(os.listdir("data/train/0")),
					'one' : len(os.listdir("data/train/1")),
					'two': len(os.listdir("data/train/2")),
					'three': len(os.listdir("data/train/3")),
					'four': len(os.listdir("data/train/4")),
					'five': len(os.listdir("data/train/5")),
					'six': len(os.listdir("data/train/6")),
					'seven': len(os.listdir("data/train/7")),
					'eight': len(os.listdir("data/train/8")),
					'nine': len(os.listdir("data/train/9"))}
	if request.method == 'POST':
		data = request.POST["base64_img"]
		format, imgstr = data.split(';base64,')
		ext = '.'+format.split('/')[-1] 
		directory = "data/train/"+request.POST['class'][0]
		filename = str(len(os.listdir(directory))+1) + ext
		with open(directory+"/"+filename, "wb") as fh:
		    fh.write(base64.b64decode(imgstr))
		return HttpResponse("success")
	return HttpResponse("fail")
