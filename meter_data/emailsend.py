# -*- coding: utf-8 -*-

from django.core.mail import send_mail
from django.conf import settings
from .models import Client


def send_email(p1vb_meter_float,  p2vb_meter_float, p3vb_meter_float, p1cb_meter_float, p2cb_meter_float,
    p3cb_meter_float, p1ca_meter_float, p2ca_meter_float, p3ca_meter_float):
    
    
    client_of_interest = Client.objects.get(email = 'rukundo.justus@gmail.com')
        
    client_name = client_of_interest.name
    
    emailflag = 0
    message = ''
    header = ''
    current_thresh = 0.35
    
    volt_low_thresh = 50
    volt_high_thresh = 200
       
    print('VOLTAGE 1 BEFORE METER', p1vb_meter_float)
    print('VOLTAGE 2 BEFORE METER', p2vb_meter_float)
    print('VOLTAGE 3 BEFORE METER', p3vb_meter_float)
    
    
    print('CURRENT 1 BEFORE METER', p1cb_meter_float)
    print('CURRENT 2 BEFORE METER', p2cb_meter_float)
    print('CURRENT 3 BEFORE METER', p3cb_meter_float)
    
    print('CURRENT 1 AFTER METER', p1ca_meter_float)
    print('CURRENT 2 AFTER METER', p2ca_meter_float)
    print('CURRENT 3 AFTER METER', p3ca_meter_float)
    
    
        
    
    
    if((p1vb_meter_float < volt_low_thresh) and ((p2vb_meter_float > volt_high_thresh) or (p3vb_meter_float > volt_high_thresh))):
        print('PHASE 1 OFF')
        emailflag = 1
        header = 'PHASE OFF'
        message = 'The system has recorded at phase 1 is off for client '
    
    
    if((p2vb_meter_float < volt_low_thresh) and ((p1vb_meter_float > volt_high_thresh) or (p3vb_meter_float > volt_high_thresh))):
        print('PHASE 2 OFF')
        emailflag = 1
        header = 'PHASE OFF'
        message = 'The system has recorded at phase 2 is off for client '
        
    if((p3vb_meter_float < volt_low_thresh) and ((p1vb_meter_float > volt_high_thresh) or (p2vb_meter_float > volt_high_thresh))):
        print('PHASE 3 OFF')
        emailflag = 1
        header = 'PHASE OFF'
        message = 'The system has recorded at phase 3 is off for client '
        
        
    if((p1cb_meter_float - p1ca_meter_float) > current_thresh):
        emailflag = 1
        header = 'METER BYPASS'
        message = 'The system has recorded a bypass on phase 1 for client, '
        
        
    if((p2cb_meter_float - p2ca_meter_float) > current_thresh):
        emailflag = 1
        header = 'METER BYPASS'
        message = 'The system has recorded a bypass on phase 2 for client, '
        
    
    if((p3cb_meter_float - p3ca_meter_float) > current_thresh):
        emailflag = 1
        header = 'METER BYPASS'
        message = 'The system has recorded a bypass on phase 3 for client, '
    
        
    if emailflag == 1:
        send_mail(
                header,
                message  + client_name,
                settings.EMAIL_HOST_USER,
                ['alkaleos10@gmail.com', 'rukundo.justus@gmail.com'],
                fail_silently = False
                )
        
    
    
   
