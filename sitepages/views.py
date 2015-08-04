# Create your views here.
from django.shortcuts import render
import random
from django.http import HttpResponse
import json

animals = ['alligator', 'ant', 'bear', 'bee', 'bird', 'camel', 'cat', 'cheetah', 'chicken', 'chimpanzee', 'cow', 'crocodile', 'deer', 'dog', 'dolphin', 'duck', 'eagle', 'fish', 'fly', 'fox', 'frog', 'giraffe', 'goat', 'goldfish', 'hamster', 'hippopotamus', 'horse', 'kangaroo', 'kitten', 'lion', 'lobster', 'monkey', 'owl', 'panda', 'pig', 'puppy', 'rabbit', 'scorpion', 'seal', 'shark', 'sheep', 'snail', 'snake', 'spider', 'squirrel', 'tiger', 'turtle', 'zebra']

def index(request):
	first = random.choice(animals)
	first_h = first[:int(len(first)/2)+1]
	second = random.choice(animals)
	while first == second:
		second = random.choice(animals)
	second_h = second[int(len(second)/2)+1:]
	name = (first_h + second_h).capitalize()
	context_dict = {'name': name, 'first': first.capitalize(), 'second': second.capitalize()}
	return render(request, 'index.html', context_dict)

def get_another_name(request):
	if request.method == 'GET':
		first = random.choice(animals)
		first_h = first[:int(len(first)/2)+1]
		second = random.choice(animals)
		while first == second:
			second = random.choice(animals)
		second_h = second[int(len(second)/2)+1:]
		name = (first_h + second_h).capitalize()
		context_dict = {'name': name, 'first': first.capitalize(), 'second': second.capitalize()}
		# print(request)
		return HttpResponse(json.dumps(context_dict), 'application/javascript')