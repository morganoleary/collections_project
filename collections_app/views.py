from django.shortcuts import render, redirect
from .models import CollectorNote, CustomerTransaction, PaymentPlan
from .forms import CollectorNoteForm

def main(request):
    if request.method == 'POST':
        form = CollectorNoteForm(request.POST)
        if form.is_valid():
            # Save the note to the database
            form.save()
            # Redirect to the main page to show the updated list of notes
            return redirect('main')  
    else:
        form = CollectorNoteForm()

    notes = CollectorNote.objects.all()  
    transactions = CustomerTransaction.objects.all()
    plans = PaymentPlan.objects.all()
    return render(request, 'collections_app/main.html', {'form': form, 'notes': notes, 'transactions': transactions, 'plans': plans})
