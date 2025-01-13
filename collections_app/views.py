from django.shortcuts import render, redirect
from .models import CollectorNote, CustomerTransaction, PaymentPlan
from .forms import CollectorNoteForm

def main(request):
    if request.method == 'POST':
        form = CollectorNoteForm(request.POST)
        if form.is_valid():
            form.save()  # Save the note to the database
            return redirect('main')  # Redirect to the main page to show the updated list of notes
    else:
        form = CollectorNoteForm()

    notes = CollectorNote.objects.all()  # Get all notes
    transactions = CustomerTransaction.objects.all()  # Get all transactions
    plans = PaymentPlan.objects.all()  # Get all payment plans
    return render(request, 'collections_app/main.html', {'form': form, 'notes': notes, 'transactions': transactions, 'plans': plans})
