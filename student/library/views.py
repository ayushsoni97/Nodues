from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Student, Choice
from django.urls import reverse


# Create your views here.

def index(request):
    students_list = Student.objects.all()
    template = loader.get_template('library/index.html')
    context = {
        'students_list': students_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    return render(request, 'library/detail.html', {'student': student})


def results(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'library/results.html', {'student': student})


def vote(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    try:
        selected_choice = student.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'library/detail.html', {
            'student': student,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('library:results', args=(student.id,)))
