from django.http import HttpResponse
from django.template import loader

from .models import TimeEntry

# Display the latest 5 time entries according to the start date
def index(request):
    latest_time_entry_list = TimeEntry.objects.order_by("-start_date")[:5]
    template = loader.get_template("polls/index.html")
    # output = ", ".join([t.question_text for t in latest_time_entry_list])
    # return HttpResponse(output)
    context = {
        "latest_time_entry_list": latest_time_entry_list
    }
    return HttpResponse(template.render(context, request))
    

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)


def detail(request, time_entry_id):
    response = "You're looking at the time entry %s."
    return HttpResponse(response % time_entry_id)
