from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DialysisRecord
from .forms import DialysisRecordForm
from datetime import datetime, timedelta

@login_required
def add_record(request):
    """View to handle adding a new dialysis record with confirmation."""
    if request.method == "POST":
        form = DialysisRecordForm(request.POST)
        if form.is_valid():
            if "confirm" in request.POST:
                # User confirmed, save the record
                record = form.save(commit=False)
                record.user = request.user
                record.date = datetime.today().date()
                record.save()
                messages.success(request, "Record added successfully!")
                return redirect("records_list")
            else:
                # Show confirmation page
                return render(request, "records/confirm_record.html", {"form": form})
    else:
        form = DialysisRecordForm()

    return render(request, "records/add_record.html", {"form": form})
@login_required
def records_list(request):
    """Display past dialysis records for the logged-in user."""
    records = DialysisRecord.objects.filter(user=request.user).order_by("-date")    


    return render(request, "records/records_list.html", {"records": records})


@login_required
def records_summary(request, period):
    """View to get dialysis records summary for the past week or month."""
    today = datetime.today().date()
    
    if period == "week":
        start_date = today - timedelta(days=7)
    elif period == "month":
        start_date = today - timedelta(days=30)
    else:
        messages.error(request, "Invalid period selected.")
        return redirect("records_list")

    records = DialysisRecord.objects.filter(user=request.user, date__gte=start_date).order_by("-date")
    return render(request, "records/records_summary.html", {"records": records, "period": period})
