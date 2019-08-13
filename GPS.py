#!/usr/bin/python
import os
import urllib2
import json

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"

while True:
    print("            "+Blue+"   $$$$$$   $$$$$$$    $$$$$$    ")
    print("            "+Blue+"  $$    $$  $$    $$  $$    $$	")
    print("            "+Blue+"  $$        $$    $$  $$  		")
    print("            "+Blue+"  $$  $$$$  $$$$$$$    $$$$$$ 	")
    print("            "+Blue+"  $$    $$  $$              $$	")
    print("            "+Blue+"  $$    $$  $$        $$    $$	")
    print("            "+Blue+"   $$$$$$   $$         $$$$$$	")
    print("            "+Reset+"\n")

    ip1 = raw_input("  IP Address: ")
    url = "http://ip-api.com/json/"
    response = urllib2.urlopen(url + ip1)
    data = response.read()
    values = json.loads(data)
	
    print("            "+Green+" Status: " + values['status'])
    print("            "+Green+" Region Name: " + values['regionName'])
    print("            "+Green+" Region Code: " + values['region'])
    print("            "+Green+" Country Code: " + values['countryCode'])
    print("            "+Green+" City: " + values['city'])
    print("            "+Green+" ISP: " + values['isp'])
    print("            "+Green+" Lat,Lon: " + str(values['lat']) + "," + str(values['lon']))
    print("            "+Green+" ZIPCODE: " + values['zip'])
    print("            "+Green+" TimeZone: " + values['timezone'])
    print("            "+Green+" AS: " + values['as'] + "\n")

    print("Thanks 4 Using This Tool ^_^ !! \n")

    break
