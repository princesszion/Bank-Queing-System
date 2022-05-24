import multiprocessing
from collections import deque
from datetime import datetime, date, time
import time as astime
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import BookingForm
from .models import Mybooking, Branch, Teller, Shift

from rq import Queue
from redis import Redis
import django_rq
from django_rq import job

# Create your views here.
processes = []

redis_conn = Redis()
# q = Queue(connection=redis_conn)
queue = Queue('default', connection=redis_conn)

def setup(request):
    b1 = Branch.objects.create(name="Remera", location="Remera")
    b2 = Branch.objects.create(name="Nyabugogo", location="Nyabugogo")
    b3 = Branch.objects.create(name="Kimironko", location="Kimironko")
    s1 = Shift.objects.create(startTime=time(12,36), endTime=time(23), duration=(
            datetime.combine(date.today(), time(23)) - datetime.combine(date.today(), time(12,36))).total_seconds())
    s2 = Shift.objects.create(startTime=time(14,8), endTime=time(23,10), duration=(
            datetime.combine(date.today(), time(23,10)) - datetime.combine(date.today(),
                                                                        time(23,8))).total_seconds())
    for branch in Branch.objects.all():
        t1 = Teller.objects.create(branchId=branch.id)
        # t1 = Teller.objects.create(branchId=branch.id)
        # t1 = Teller.objects.create(branchId=branch.id)

    for shift in Shift.objects.all():
        # print(str(shift.startTime))
        # schedule.every().day.at(str(shift.startTime)).do(startShift, shift=shift)
        # print("shift scheduled")
        for branch in Branch.objects.all():
            Mybooking.objects.create(branch=branch.id, service="random service", shift=shift.id)
            Mybooking.objects.create(branch=branch.id, service="random service", shift=shift.id)
            Mybooking.objects.create(branch=branch.id, service="random service", shift=shift.id)
            Mybooking.objects.create(branch=branch.id, service="random service", shift=shift.id)
    return redirect('index')


# def startShiftTimer(shift):
#     print("a shift timer started")
#     loop = asyncio.new_event_loop()
#     loop.create_task(run_at(shift.startTime, startShift(shift)))
#     loop.run_forever()

def destroy(request):
    Mybooking.objects.all().delete()
    Branch.objects.all().delete()
    Teller.objects.all().delete()
    Shift.objects.all().delete()
    # schedule.clear()
    return redirect('index')


def index(request):
    branches = Branch.objects.all()
    return render(request, 'index.html', {'branches': branches})


def inShiftBound(shiftId):
    shift = Shift.objects.get(id=shiftId)
    # print(str(shift))
    # print(str(shift.endTime))
    if datetime.combine(date.today(), shift.endTime) >= datetime.now():
        return False
    else:
        print("shift ended")
        return True

def assignTeller(shiftId, teller):
    # print("removing")
    if len(Mybooking.objects.filter(shift=shiftId, branch=teller.branchId)) != 0 or Mybooking.objects.filter(shift=shiftId, branch=teller.branchId):
        currentCustomer = deque(Mybooking.objects.filter(shift=shiftId, branch=teller.branchId)).popleft()
        print("removing")
        astime.sleep(currentCustomer.estimatedTime)
        print("deleted")
        currentCustomer.delete()
        assignTeller(shiftId, teller)
    else:
        print("Queue empty")


def startShift(request, shiftId, branchId):
    # multiprocessing.set_start_method('fork', force=True)
    print("Shift started")
    # shift = Shift.objects.filter(id=shiftId)
    for teller in Teller.objects.filter(branchId=branchId):
        queue = django_rq.get_queue('default', default_timeout=None)
        queue.enqueue(assignTeller, args=(shiftId, teller,))
        # q.enqueue(assignTeller, (shiftId, teller))
        # assignTeller(shiftId, teller)
    return redirect('viewBranchQueue', branchId=branchId)



def book(request):
    bookings = Mybooking.objects.all()
    branches = Branch.objects.all()
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        # if inShiftBound(form['shift'].value()):
        #     startShift(form['shift'].value())
        return redirect('viewBranchQueue', branchId=form['branch'].value())
    print("Created!!")
    return render(request, 'bookings.html', {'branches': branches , 'form': form})


def deleteItem(request, pk):
    task = Mybooking.objects.get(id=pk)
    task.delete()
    return redirect('bookings')

def viewBranchQueue(request, branchId):
    bookings = []
    shifts = []
    branches = Branch.objects.all()
    for shift in Shift.objects.all():
        shifts.append(shift)
        bookings.append(Mybooking.objects.filter(branch= branchId, shift= shift.id))
    shift_iter = iter(shifts)
    return render(request, 'branchQueue.html', {'branchBookings': zip(shifts,bookings), 'branches': branches, 'shifts': Shift.objects.all(), 'branchId':branchId})


def updateItem(request, pk):
    booking = Mybooking.objects.get(id=pk)
    updateForm = BookingForm(instance=booking)
    if request.method == 'POST':
        updateForm = BookingForm(request.POST, instance=booking)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('bookings')
    return render(request, 'updateItem.html', {'todo': booking, 'updateform': updateForm})
