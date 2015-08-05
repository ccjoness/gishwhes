# Create your views here.
from django.shortcuts import render
import random
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from base64 import b64decode
from django.core.files.base import ContentFile
from .models import Image
import uuid

animals = ['alligator', 'ant', 'bear', 'bee', 'bird', 'camel', 'cat', 'cheetah', 'chicken', 'chimpanzee', 'cow',
           'crocodile', 'deer', 'dog', 'dolphin', 'duck', 'eagle', 'fish', 'fly', 'fox', 'frog', 'giraffe', 'goat',
           'goldfish', 'hamster', 'hippopotamus', 'horse', 'kangaroo', 'kitten', 'lion', 'lobster', 'monkey', 'owl',
           'panda', 'pig', 'puppy', 'rabbit', 'scorpion', 'seal', 'shark', 'sheep', 'snail', 'snake', 'spider',
           'squirrel', 'tiger', 'turtle', 'zebra']


def index(request):
    first = random.choice(animals)
    first_h = first[:int(len(first) / 2) + 1]
    second = random.choice(animals)
    while first == second:
        second = random.choice(animals)
    second_h = second[int(len(second) / 2) + 1:]
    name = (first_h + second_h).capitalize()
    img = Image.objects.all().order_by('-id')
    context_dict = {'name': name, 'first': first.capitalize(), 'second': second.capitalize(), 'img': img}
    return render(request, 'index.html', context_dict)


def get_another_name(request):
    if request.method == 'GET':
        first = random.choice(animals)
        first_h = first[:int(len(first) / 2) + 1]
        second = random.choice(animals)
        while first == second:
            second = random.choice(animals)
        second_h = second[int(len(second) / 2) + 1:]
        name = (first_h + second_h).capitalize()
        context_dict = {'name': name, 'first': first.capitalize(), 'second': second.capitalize()}
        # print(request)
        return HttpResponse(json.dumps(context_dict), 'application/javascript')


@csrf_exempt
def img_upload(request):
    print(request.POST)
    if request.method == 'POST':
        img = Image()
        b64_text = request.POST['image']
        title = request.POST['title']
        img.title = title
        img.first = request.POST['first']
        img.second = request.POST['second']
        image_data = b64decode(b64_text)
        img.image = ContentFile(image_data, str(title) + '-' + str(uuid.uuid4()) + '.png')
        img.save()

    return HttpResponse('okay')


def images(request):
    img = Image.objects.all().order_by('-id')
    context_dict = {'img': img}
    return render(request, 'images.html', context_dict)
