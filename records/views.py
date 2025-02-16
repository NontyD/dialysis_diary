from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DialysisRecord
from datetime import timedelta

@login_required
def add_record(request):
    """Allow users to log their dialysis session."""
    if request.method == "POST":
        weight_before = request.POST.get("weight_before")
        systolic_bp = request.POST.get("systolic_bp")
        diastolic_bp = request.POST.get("diastolic_bp")
        initial_drain_volume = request.POST.get("initial_drain_volume")
        total_uf = request.POST.get("total_uf")
        avg_dwell = request.POST.get("avg_dwell")
        lost_dwell = request.POST.get("lost_dwell")
        added_dwell = request.POST.get("added_dwell")
        weight_after = request.POST.get("weight_after")
        comments = request.POST.get("comments")

        # Ensure required fields are filled
        if not weight_before or not systolic_bp or not diastolic_bp or not weight_after:
            messages.error(request, "All required fields must be filled.")
            return render(request, "records/add_record.html")

        # Create new record
        DialysisRecord.objects.create(
            user=request.user,
            weight_before=weight_before,
            systolic_bp=systolic_bp,
            diastolic_bp=diastolic_bp,
            initial_drain_volume=initial_drain_volume,
            total_uf=total_uf,
            avg_dwell=timedelta(hours=int(avg_dwell.split(":")[0]), minutes=int(avg_dwell.split(":")[1])),
            lost_dwell=timedelta(hours=int(lost_dwell.split(":")[0]), minutes=int(lost_dwell.split(":")[1])),
            added_dwell=timedelta(hours=int(added_dwell.split(":")[0]), minutes=int(added_dwell.split(":")[1])),
            weight_after=weight_after,
            comments=comments,
        )

        messages.success(request, "Dialysis record added successfully!")
        return redirect("records_list")  # Redirect to records page

    return render(request, "records/add_record.html")


@login_required
def records_list(request):
    """View past dialysis records."""
    records = DialysisRecord.objects.filter(user=request.user)
    return render(request, "records/records_list.html", {"records": records})
