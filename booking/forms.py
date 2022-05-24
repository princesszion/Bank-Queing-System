from django import forms
from .models import Branch, Mybooking, Shift
SERVICES = [
    ('Pay school fees', 'Pay schools fees'),
    ('Create a bank account', 'Create a bank account'),
    ('Deposit money', 'Deposit money'),
    ('Take a loan', 'Take a loan'),
]
BRANCHES = []
for branch in Branch.objects.all():
    BRANCHES.append((branch.id, str(branch.name)))

SHIFTS = []
for shift in Shift.objects.all():
    SHIFTS.append((shift.id, (str(shift.startTime) + " - " + str(shift.endTime))))

class BookingForm(forms.ModelForm):
    branch = forms.CharField(max_length=100, widget=forms.Select(attrs={
        'class':"form-select", 'id':"inputGroupSelect01"
    }, choices= BRANCHES))
    service = forms.CharField(max_length=100, widget=forms.Select(attrs={
        'class':"form-select", 'id':"inputGroupSelect02"
    },choices=SERVICES))
    shift = forms.CharField(max_length=50, widget=forms.Select(attrs={
        'class':"form-select", 'id':"inputGroupSelect03"
    }, choices=SHIFTS))

    class Meta:
        model = Mybooking
        fields = ['branch', 'service', 'shift']
        # fields = '__all__'