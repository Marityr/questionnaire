from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View

from .models import UserData
from .forms import UserDataForm


class FormProfile(View):
    """данные пользователя"""

    def get(self, request) -> render:
        template_name = 'nwe/formprofile.html'

        try:
            userdata = UserData.objects.get(username=request.user)
            data = {
                'age': userdata.age,
            }
            form = UserDataForm(instance=userdata)
            print('11')
        except UserData.DoesNotExist:
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
            print(request.POST)
            form = UserDataForm(request.POST)
            try:
                userdata = UserData.objects.get(username=request.user)
                userdata.age = request.POST['age']
                userdata.gender = request.POST['gender']
                userdata.massa = request.POST['massa']
                userdata.purpose = request.POST['purpose']
                userdata.decision = request.POST['decision']
                userdata.problem = request.POST['problem']
                userdata.problem_two = request.POST['problem_two']
                userdata.problem_fre = request.POST['problem_fre']
                userdata.save()
            except UserData.DoesNotExist:
                userdata.username = request.user
                userdata.age = request.POST['age']
                userdata.gender = request.POST['gender']
                userdata.massa = request.POST['massa']
                userdata.purpose = request.POST['purpose']
                userdata.decision = request.POST['decision']
                userdata.problem = request.POST['problem']
                userdata.problem_two = request.POST['problem_two']
                userdata.problem_fre = request.POST['problem_fre']
                userdata.save()

        return redirect('quizes:home')
