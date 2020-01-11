from django.shortcuts import render, redirect
from .models import Gym
from .forms import GymCreate
from django.http import HttpResponse
import os
from django.conf import settings
from django.http import HttpResponse, Http404

from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    shelf = Gym.objects.all()
    return render(request, 'gymapp/premium.htm', {'shelf': shelf})

    
def upload(request):
    upload = GymCreate()
    if request.method == 'POST':
        upload = GymCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'gymapp/upload_form.htm', {'upload_form':upload})


             
def update_form(request, gym_id):
    gym_id = int(gym_id)
    try:
        values = Gym.objects.get(id = gym_id)
    except Gym.DoesNotExist:
        return redirect('index')
    gym_form = GymCreate(request.POST or None, instance = values)
    if gym_form.is_valid():
       gym_form.save()
       return redirect('index')
    return render(request, 'gymapp/upload_form.htm', {'upload_form':gym_form})




def delete_form(request, gym_id):
    gym_id = int(gym_id)
    try:
        values = Gym.objects.get(id = gym_id)
    except Gym.DoesNotExist:
        return redirect('index')
    values.delete()
    return redirect('index')

"""

Search Functionality

"""

# def search_hai(request):
#         return render (request, 'gymapp/premium.htm')


def search_function_hai(request):
    if request.method =='GET':
        finds = request.GET['hacsac']

        if finds:
            match = Gym.objects.filter(Q(workoutname__icontains=finds))
                                     
            if match:                
                return render(request,'gymapp/upload_form.htm', {'sac':match})
            else:
                messages.error(request, "The word, You type did  not Exist")
                # return HttpResponse("The word, You type was not Exist")

        else:
            return HttpResponseRedict('gymapp/premium.htm')  
    return render(request, 'gymapp/premium.htm')         


    ###########################################
    # def download(request, path):
    #     file_path = os.path.join(settings.MEDIA_ROOT, path)
    # if os.path.exists(file_path):
    #     with open(file_path, 'rb') as fh:
    #         response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
    #         response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
    #         return response
    # raise Http404   