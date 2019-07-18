from django.shortcuts import render
from django.http import HttpResponse
from .models import Data, Client
from .emailsend import send_email



def clientshow(request):
    if(request.method == 'GET'):
        
        try:
            clientsdata = Client.objects.all().order_by("-pk")  
            context = {'clientsdata': clientsdata}
            return render(request, 'clientsview.html', context)
        except:   
            return HttpResponse("<br><h3> There is no client data in the data base. Register some clients and try again </h3>") 

        
            
def datashow(request,pk):
    if(request.method == 'GET'):
    
        clientobject = Client.objects.get(pk = pk) 
        clientdataobject = Data.objects.filter(client = clientobject).order_by("-pk")        

        print(clientobject.name)
        context = {'clientdataobject': clientdataobject, 'clientobject': clientobject }
        
        return render(request, 'tableview.html', context)


    
def datareceive(request):
       
    if(request.method == 'GET'):
        device_serial = request.GET.get("device_serial")
                
        p1vb_meter = request.GET.get("p1vb_meter")
        p2vb_meter = request.GET.get("p2vb_meter")
        p3vb_meter = request.GET.get("p3vb_meter")
          
        p1cb_meter = request.GET.get("p1cb_meter")
        p2cb_meter = request.GET.get("p2cb_meter")
        p3cb_meter = request.GET.get("p3cb_meter")
        
        p1va_meter = request.GET.get("p1va_meter")
        p2va_meter = request.GET.get("p2va_meter")
        p3va_meter = request.GET.get("p3va_meter")
        
        p1ca_meter = request.GET.get("p1ca_meter")
        p2ca_meter = request.GET.get("p2ca_meter")
        p3ca_meter = request.GET.get("p3ca_meter")
          
        print(device_serial)
        
        print(p1vb_meter)
        print(p2vb_meter)
        print(p3vb_meter)
        
        print(p1cb_meter)
        print(p2cb_meter)
        print(p3cb_meter)
        
        print(p1va_meter)
        print(p2va_meter)
        print(p3va_meter)
        
        print(p1ca_meter)
        print(p2ca_meter)
        print(p3ca_meter)
        

        if(device_serial and p1vb_meter and p2vb_meter and p3vb_meter and p1cb_meter and p2cb_meter and p3cb_meter and
           p1va_meter and p2va_meter and p3va_meter and p1ca_meter and p2ca_meter and p3ca_meter):
            
            p1vb_meter_float = float(p1vb_meter)
            p2vb_meter_float = float(p2vb_meter)
            p3vb_meter_float = float(p3vb_meter)
            
            p1cb_meter_float = float(p1cb_meter)
            p2cb_meter_float = float(p2cb_meter)
            p3cb_meter_float = float(p3cb_meter)
            
            p1ca_meter_float = float(p1ca_meter)
            p2ca_meter_float = float(p2ca_meter)
            p3ca_meter_float = float(p3ca_meter)
            
            
            send_email(p1vb_meter_float,  p2vb_meter_float, p3vb_meter_float, p1cb_meter_float, p2cb_meter_float,
                       p3cb_meter_float, p1ca_meter_float, p2ca_meter_float, p3ca_meter_float)
                             
                
            client_object = Client.objects.get(device_serial = device_serial)    
                
            Data(
                    
                client = client_object,
                
                p1vb_meter = p1vb_meter,
                p2vb_meter = p2vb_meter,
                p3vb_meter = p3vb_meter,
                
                p1cb_meter = p1cb_meter,
                p2cb_meter = p2cb_meter,
                p3cb_meter = p3cb_meter,
                
                p1va_meter = p1va_meter,
                p2va_meter = p2va_meter,
                p3va_meter = p3va_meter,
                
                p1ca_meter = p1ca_meter,
                p2ca_meter = p2ca_meter,
                p3ca_meter = p3ca_meter,
                
            ).save()
                  
            return HttpResponse("<br><h3> Pass </h3>")
        else:
            return HttpResponse("<br><h3> Data Missing </h3>")
          
            
def datasend(request):
    if(request.method == 'GET'):
        return render(request, 'datasend.html')
        
        
        
