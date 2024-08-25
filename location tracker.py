import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
import opencage
from opencage.geocoder import OpenCageGeocode
import folium
import time
import prettytable as pt
import webbrowser
#===========================================================================================================================================
try:
    
    def location(number):
        phone=phonenumbers.parse(number)
        locationn = geocoder.description_for_number(phone,"en")
        time.sleep(3)
        print(f"COUNTRY TO WHICH THIS NUMBER BELONGS :{locationn}")
        #return locationn
    def simcompany(number):
        phone=phonenumbers.parse(number)
        car=carrier.name_for_number(phone,"en")
        time.sleep(3)
        print(f"CARRIER COMPANY : {car}")
        return car
    def timezonee(number):
        phone=phonenumbers.parse(number)
        #time=timezone.time_zones_for_number(phone)
        locationn = geocoder.description_for_number(phone,"en")
        timee=timezone.time_zones_for_number(phone)
        time.sleep(3)
        print(f"NUMBER BELONG TO {timee} TIME ZONE")
        return timee
    def mapp(number,query):
        key = "9a3867c96c5647949bec1a37c95521e1" 
        geocoder = OpenCageGeocode(key)
        result = geocoder.geocode(query)
        lat = result[0]['geometry']['lat']
        lng = result[0]['geometry']['lng']
        print(f"LATITUDE AND THE LONGITUDE OF THE LOCATION AS PER FOUND {lat},{lng}")
        my_map = folium.Map(location=[lat,lng], zoom_start=9)
        folium.Marker([lat, lng], popup= query).add_to(my_map)
        my_map.save("location.html")
        print("LOCATION FOUND !!")
        print("TAKING MAP INTO ACCOUNT...")
        print("WAIT FOR A WHILE")
        time.sleep(4)
        webbrowser.open("location.html")
        return lat , lng
#======================================================================================================================================================
except:
    print("SORRY FOR SOME INCONVINIENCE CAUSED !!! SOME ERROR OCCURED")
    
menu=""""
        **********************************************************************
              LOCATION TRACKER           ==>      M A I N     M E N U                                                         |
        **********************************************************************
                                1.COUNTRY
                                2.CARRIER COMPANY
                                3.TIMEZONE
                                4.MAP LOACTION AND LATITUDE , LONGITUDE
                                5.ALL
                                6.EXIT
                                7.ABOUT   
          ----------------------------------------------------------------

   """
while(1):
    try:
        
        print(" "*25 , "WELCOME TO MAIN MENU OF LOCATION TRACKER SYSTEM")
        print(menu)
        ch=int(input("ENTER YOUR CHOISE BETWEEN 0-6"))

        if ch==1:
            number=input("ENTER MOBILE NUMBER WITH COUNTRY CODE [EG:+91]:")
            if(len(number)==13 and number[0]=="+"):
                location(number)
            else:
                time.sleep(2)
                print("ENTER A VALID NUMBER WITH COUNTRY CODE ")

        elif ch==2:
            number=input("ENTER MOBILE NUMBER WITH COUNTRY CODE [EG:+91]:")
            if(len(number)==13 and number[0]=="+"):
                simcompany(number)
            else:
                time.sleep(2)
                print("ENTER A VALID NUMBER WITH COUNTRY CODE ")
        elif ch==3:
            number=input("ENTER MOBILE NUMBER WITH COUNTRY CODE [EG:+91]:")
            if(len(number)==13 and number[0]=="+"):
                timezonee(number) 
            else:
                time.sleep(2)
                print("ENTER A VALID NUMBER WITH COUNTRY CODE ")
            
            
        elif ch==4:
            number=input("ENTER MOBILE NUMBER WITH COUNTRY CODE [EG:+91]:")
            if(len(number)==13 and number[0]=="+"):
                phone = phonenumbers.parse(number)
                location = geocoder.description_for_number(phone, "en")
                query = str(location)
                mapp(number,query)
            
            else:
                time.sleep(2)
                print("ENTER A VALID NUMBER WITH COUNTRY CODE ")

        elif ch==5:
            r=["PHONE NUMBER","COUNTRY NAME","CARRIER COMPANY","TIME ZONE","LATITUDE","LONGITUDE"]
            t=pt.PrettyTable(r)
            number=input("ENTER MOBILE NUMBER WITH COUNTRY CODE [EG:+91]:")
            if(len(number)==13 and number[0]=="+"):
                
                phone = phonenumbers.parse(number)
                location = geocoder.description_for_number(phone, "en")
                query = str(location)
                print(query)
                s=simcompany(number)
                k=timezonee(number)
                o,p=mapp(number,query)
                l=[number,query,s,k,o,p]
                t.add_row(l)
                print(t)
            
            else:
                time.sleep(2)
                print("ENTER A VALID NUMBER WITH COUNTRY CODE ")
           
            
        elif ch==6:
            print("DO YOU WANT TO EXIT THE SYSYTEM->?")
            try:
                
                ch2=input("ENTER Y/N ")
                
                if ch2.lower()=="y":
                    time.sleep(3)
                    print("THANKS FOR USING OUR SERVICE")
                    break
                else:
                    pass
            except:
                time.sleep(2)
                print("SOME ERROR OCCURED")
        
        elif ch==7:
            print("WELCOME IN ABOUT US SECTION ")
            time.sleep(1)
            print("AUTHORITY - 'SHREY OMER' , 'ANUJ SONI' , 'ANJALI GUPTA' ")
            time.sleep(1)
            print("SPECIAL THANKS TO 'DR SAIFF' :")
            time.sleep(1)
                
        else:
            time.sleep(2)
            print("ENTER NUMBER BETWEEN 1-6")
    except:
        print("SORRY FOR INCONVINENCED CAUSED !!! SOME ERROR OCCURED")
        
        
            
        
        
    
    




