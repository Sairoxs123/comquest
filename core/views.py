from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *

def has_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True  # Duplicate found
        seen.add(item)
    return False  # No duplicates found

@csrf_exempt
def index(request):
    events = {
        "Hot Seat": 3,
        "Diplomatica": 1,
        "Trade Titans": 3,
        "Spark Tank": 3,
        "Brand Craft": 2,
    }
    if request.method == "POST":
        schoolname = request.POST.get("schoolname")
        registered_events = eval(request.POST.get("registered"))
        number = len(registered_events)
        teacher_number = request.POST.get("teacher-number")
        try:
            x = Registration.objects.get(school=schoolname)
            return render(request, "index.html", {"error": "done"})
        except:
            pass

        final_data = ""

        if has_duplicates(registered_events.values()):
            return render(request, "index.html", {"error": "duplicate"})

        for i in registered_events.values():
            final_data += "<h1><b>" + i + "</b></h1>" + "<br>"
            #event_details = {}
            nop = events[i]
            for k in range(nop):
                name = request.POST.get(f"{i}-p{int(k + 1)}-name")
                contact = request.POST.get(f"{i}-p{int(k + 1)}-contact")
                final_data += f"""<b>Participant {k+1}</b><br>
                Name : {name}
                Contact: {contact}<br>
                """

        Registration(school=schoolname, number=number, teacher_contact=teacher_number, details=final_data).save()

        return redirect("thanks/")
    return render(request, "index.html")

def thanks(request):
    return render(request, "thanks.html")

def admin(request):
    registered = Registration.objects.all()
    return render(request, "admin.html", {"registered":registered})
