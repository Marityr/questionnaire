from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View

from .models import UserData
from .forms import UserDataForm


class FormProfile(View):
    """данные пользователя"""

    def get(self, request) -> render:
        template_name = 'nwe/formprofile.html'
        form = UserDataForm()

        try:
            userdata = UserData.objects.get(username=request.user)
        except UserData.DoesNotExist:
            userdata = 'none'

        context = {
            'form': form,
            'userdata': userdata
        }
        
        return render(request, template_name, context)

    def post(self, request):
        user = request.user
        userdata = UserData()
        if request.method == 'POST':
            form = UserDataForm(request.POST)
            try:
                userdata = UserData.objects.get(username=request.user)
                userdata.age = request.POST['age']
                userdata.gender = request.POST['gender']
                userdata.massa = request.POST['massa']
                userdata.purpose = request.POST['purpose']
                userdata.decision = request.POST['decision']
                userdata.problem = request.POST['problem']
                userdata.save()
            except UserData.DoesNotExist:
                userdata.username = request.user
                userdata.age = request.POST['age']
                userdata.gender = request.POST['gender']
                userdata.massa = request.POST['massa']
                userdata.purpose = request.POST['purpose']
                userdata.decision = request.POST['decision']
                userdata.problem = request.POST['problem']
                userdata.save()

        return redirect('quizes:home')
