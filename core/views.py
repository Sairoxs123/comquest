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
        teacher_number = request.POST.get("teacher-number")

        if not schoolname or not registered_events or not teacher_number:
            return render(request, "index.html", {"error": "incomplete"})

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
            nop = events[i]
            for k in range(nop):
                name = request.POST.get(f"{i}-p{int(k + 1)}-name")
                contact = request.POST.get(f"{i}-p{int(k + 1)}-contact")
                if not name or not contact:
                    return render(request, "index.html", {"error": "incomplete"})
                final_data += f"""<b>Participant {k+1}</b><br>
                Name : {name}<br>
                Contact: {contact}<br>
                """

        Registration(
            school=schoolname,
            number=len(registered_events),
            teacher_contact=teacher_number,
            details=final_data,
        ).save()

        return redirect("thanks/")
    return render(request, "index.html")


def thanks(request):
    return render(request, "thanks.html")

def owner(request):
    registered = Registration.objects.all()
    if request.session.get("logged_in"):
        return render(request, "owner.html", {"registered": registered})

    return redirect("/owner/login/")


def owner_login(request):
    if request.method == "POST":
        if request.POST.get("password") == "comquest@jssps":
            request.session["logged_in"] = True
            return redirect("/owner")
        else:
            return render(request, "owner_login.html", {"error": "password"})
    return render(request, "owner_login.html")
