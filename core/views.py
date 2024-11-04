import json
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

def count_teams(event):
    registrations = Registration.objects.all()
    teams = 0
    for i in registrations:
        if f"<h1><b>{event}</b></h1>" in i.details:
            teams += 1
    return teams

@csrf_exempt
def index(request):
    all_events = {
        "Hot Seat": [3, 17],
        "Diplomatica": [1, 25],
        "Trade Titans": [3, 25],
        "Spark Tank": [4, 20],
        "Brand Craft": [2, 25],
    }
    events = {}
    for i, j in all_events.items():
        if count_teams(i) < j[1]:
            events[i] = j[0]
    if request.method == "POST":
        if not request.POST.get("registered"):
            return render(request, "index.html", {"error": "incomplete", "events":json.dumps(events)})
        schoolname = request.POST.get("schoolname")
        registered_events = eval(request.POST.get("registered"))
        teacher_name = request.POST.get("teacher-name")
        teacher_number = request.POST.get("teacher-number")
        teacher_email = request.POST.get("teacher-email")

        if not schoolname or not registered_events or not teacher_number:
            return render(request, "index.html", {"error": "incomplete", "events":json.dumps(events)})

        final_data = ""

        if has_duplicates(registered_events.values()):
            return render(request, "index.html", {"error": "duplicate", "events":json.dumps(events)})
        students = []
        for i in registered_events.values():
            final_data += "<h1><b><u>" + i + "</u></b></h1>" + "<br>"
            nop = events[i]
            for k in range(nop):
                name = request.POST.get(f"{i}-p{int(k + 1)}-name").strip().title()
                if name not in students:
                    students.append(name)
                    contact = request.POST.get(f"{i}-p{int(k + 1)}-contact")
                    grade = request.POST.get(f"{i}-p{int(k + 1)}-grade")
                    if not name or not contact:
                        return render(request, "index.html", {"error": "incomplete", "events":json.dumps(events)})
                    final_data += f"""<b>Participant {k+1}</b><br>
                    Name : {name}<br>
                    Contact: {contact}<br>
                    Grade: {grade}<br><br>
                    """
                else:
                    return render(request, "index.html", {"error": "student_duplicate", "events":json.dumps(events)})

        Registration(
            school=schoolname,
            number=len(registered_events),
            teacher_name=teacher_name,
            teacher_email=teacher_email,
            teacher_mobile=teacher_number,
            details=final_data,
        ).save()

        return redirect("thanks/")
    return render(request, "index.html", {"events":json.dumps(events)})


def thanks(request):
    return render(request, "thanks.html")

def rubric(request):
    return render(request, "rubric.html")

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
