from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DialysisRecord
from .forms import DialysisRecordForm
from datetime import datetime, timedelta

@login_required
def add_record(request):
    """View to handle adding a new dialysis record."""
    if request.method == "POST":
        form = DialysisRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)  # Don't save to the DB yet
            record.user = request.user  # Assign the logged-in user
            record.date = datetime.today().date()  # Auto-set today's date
            record.save()  # Now save it to the DB
            messages.success(request, "Record added successfully!")
            return redirect("records_list")  # Redirect to the records list
    else:
        form = DialysisRecordForm()  # Display an empty form
    
    return render(request, "records/add_record.html", {"form": form})  # Pass form to template

@login_required
def records_list(request):
    """View to display the user's dialysis records."""
    records = DialysisRecord.objects.filter(user=request.user).order_by("-date")
    return render(request, "records/records_list.html", {"records": records})

@login_required
def edit_record(request, record_id):
    """View to handle editing an existing dialysis record."""
    record = get_object_or_404(DialysisRecord, id=record_id, user=request.user)

    if request.method == "POST":
        form = DialysisRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully!")
            return redirect("records_list")
    else:
        form = DialysisRecordForm(instance=record)
    
    return render(request, "records/edit_record.html", {"form": form, "record": record})

@login_required
def delete_record(request, record_id):
    """View to handle deleting a dialysis record."""
    record = get_object_or_404(DialysisRecord, id=record_id, user=request.user)
    
    if request.method == "POST":
        record.delete()
        messages.success(request, "Record deleted successfully!")
        return redirect("records_list")

    return render(request, "records/delete_record.html", {"record": record})

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

@login_required
def dashboard(request):
    """Dashboard page with quick links to app features."""
    return render(request, "users/dashboard.html")
