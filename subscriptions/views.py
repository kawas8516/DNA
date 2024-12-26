
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Subscriber

@csrf_exempt
def save_email(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')

            if email:
                subscriber, created = Subscriber.objects.get_or_create(email=email)
                if created:
                    return JsonResponse({'success': True, 'message': 'Subscription successful!'})
                else:
                    return JsonResponse({'success': False, 'message': 'Email already subscribed.'})
            return JsonResponse({'success': False, 'message': 'Invalid email.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
