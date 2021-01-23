from django.shortcuts import render
from Hotel.models import *
from Hotel.form import *
# Create your views here.

def find_room(Detail):
    vis=[]
    for i in range(0,11):
        vis.append(0)

    count=0
    for i in Detail:
        vis[i.room_no]=1
        count+=1

    if count>=10:
        return -1

    for i in range(1, 11):
        if vis[i]==0:
            return i


def index(request):

    if(request.method == "POST"):
        name= request.POST.get('Name')
        in_date=request.POST.get('Start_Date')
        out_date=request.POST.get('End_Date')
        if in_date>out_date:
            return render(request, "warning.html", {})

        Detail=hotel_data.objects.all().order_by('checkout_date').filter(checkout_date__gte=in_date).filter(checkin_date__lte=out_date)

        room_no=find_room(Detail)
        if room_no!=-1:
          model=hotel_data()
          model.checkin_date=in_date
          model.checkout_date=out_date
          model.customer_name=name
          model.room_no=room_no
          model.save()
          return render(request,"result.html",{"name":name,"in_date":in_date,"out_date":out_date,"room_no":room_no})
        else:
            return render(request,"not_available.html",{"name":name,"in_date":in_date,"out_date":out_date})

    else:
       data=hotel_form()
    return render(request,"index.html",{"data":data})



def result(request):
    return render(request,"result.html",)

def test(request):
    return render(request,"testing.html",)

#write your own function to call names.html it should show all the data with url extension "summary/"
def print_data(request):
    detail=hotel_data.objects.all()
    return render(request,"print_data.html",{"details":detail})

def search(request):
    if (request.method == "POST"):
         name = request.POST.get('Search_Name')
         detail=hotel_data.objects.all().filter(customer_name=name)
         print("Details : ")
         for i in detail:
             print(i.customer_name)
             print(i.room_no)
             print(i.checkin_date)
             print(i.checkout_date)
             print("---------")
         return render(request,"print_data.html",{"details":detail})
    else:
        return render(request,"search.html",{})



