#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import serial
from influxdb import InfluxDBClient
import datetime
import timeit
import matplotlib.pyplot as plt


user = 'admin'
password = 'admin'
db_name = 'sensor_read'
host = 'localhost'
port = 8086
ser = serial.Serial('/dev/ttyUSB0')


client = InfluxDBClient(host, port, user, password, db_name)

radio_rx_data = []

tx_end_string = "End of task!"

print("Create database: " + db_name)
client.create_database(db_name)
client.switch_database(db_name)



while True:
    
    points = []
    
    serial_string = ser.readline()
    
    serial_string = serial_string.decode('utf-8')
    
#     if(serial_string == tx_end_string):
#         break;
    
    if(serial_string.startswith(',')):
        sliced_string = serial_string[1:]        
    
        if (sliced_string[0].isdigit() | sliced_string[1].isdigit() ):
            split_string = sliced_string.strip().split(',')
            scale_list = list(map(float,split_string))
            # print(scale_list)
            
            radio_rx_data.extend(scale_list)

            
            for i in scale_list:

                point = {

                "measurement": 'weight_scale',
        #         "time": datetime.datetime.now(),
                "fields": {
                "value": i
                    }
                }
                points.append(point)


                client.write_points(points)


# In[68]:





# In[ ]:





# In[56]:





# In[ ]:





# In[ ]:





# In[ ]:




