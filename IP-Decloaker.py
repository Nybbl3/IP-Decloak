import requests
import time
import os

print("\u001b[0m\n")

os.system("neofetch")

print("\u001b[0m\n")

f = open("ascii.txt", "r")

ascii = "".join(f.readlines())

print("\u001b[38;5;10m" + ascii)

print("\u001b[0m\n")

print("\u001b[7mCoded and Designed by Nybble\u001b[0m")

print("\u001b[0m\n")

ip = input("Enter an IP Address (IPv4 or IPv6) : ")

response = requests.get("http://ip-api.com/json/" + ip +
                        "?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,mobile,proxy,hosting,query").json()


if str(response["status"]) == "success":
    x = "Success \U0001F44D"
else:
    x = "Fail \U0001F44E"

print("\u001b[0m\n")

print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Address is : \u001b[33;1m" + str(response["query"]))

print("\u001b[38;5;86m[*] \u001b[35;1mStatus of lookup of Target IP Address is : \u001b[33;1m" + x)

if x == "Fail \U0001F44E":
    print("\n")
    print("\u001b[38;5;86m[*] \u001b[35;1mMessage : \u001b[33;1m" +
          str(response["message"]) + "\U00002757")

if str(response["city"]) == "":
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP city is : \u001b[33;1mNo data\U00002757")
else:
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP city is : \u001b[33;1m" + str(response["city"]))

if str(response["district"]) == "":
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP district is : \u001b[33;1mNo data\U00002757")
else:
    print("\u001b[38;5;86m[*] \u001b[35;1mTaget IP district is : \u001b[33;1m" +
          str(response["district"]))

if str(response["regionName"]) == "":
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Region Name is : \u001b[33;1mNo data\U00002757")
else:
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Region Name is : \u001b[33;1m" +
          str(response["regionName"]))

if str(response["region"]) == "":
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Region Code is : \u001b[33;1mNo data\U00002757")
else:
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Region Code is : \u001b[33;1m" +
          str(response["region"]))

if str(response["country"]) == "":
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Country is : \u001b[33;1mNo data\U00002757")
else:
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Country is : \u001b[33;1m" +
          str(response["country"]))

if str(response["countryCode"]) == "":
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Country Code is : \u001b[33;1mNo data\U00002757")
else:
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Country Code is : \u001b[33;1m" +
          str(response["countryCode"]))

if str(response["continent"]) == "":
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Continent is : \u001b[33;1mNo data\U00002757")
else:
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Continent is : \u001b[33;1m" +
          str(response["continent"]))

if str(response["continentCode"]) == "":
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Contient Code is: \u001b[33;1mNo data\U00002757")
else:
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Contient Code is: \u001b[33;1m" +
          str(response["continentCode"]))

if str(response["zip"]) == "":
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Zip Code is: \u001b[33;1mNo data\U00002757")
else:
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Zip Code is: \u001b[33;1m" + str(response["zip"]))

if str(response["lat"]) == "":
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Latitude is : \u001b[33;1mNo data\U00002757")
else:
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Latitude is : \u001b[33;1m" + str(response["lat"]))

if str(response["lon"]) == "":
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Longtitude is : \u001b[33;1mNo data\U00002757")
else:
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Longtitude is : \u001b[33;1m" +
          str(response["lon"]))

if str(response["timezone"]) == "":
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Timezone is : \u001b[33;1mNo data\U00002757")
else:
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Timezone is : \u001b[33;1m" +
          str(response["timezone"]))


def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(n))


n = int(response["offset"])

if int(response["offset"]) > 0:
    m = "+"
else:
    m = "-"

if str(response["offset"]) == "":
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP GMT Offset is : \u001b[33;1mNo data\U00002757")
else:
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP GMT Offset is : \u001b[33;1m" + m + convert(n))

if str(response["currency"]) == "":
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Currency is : \u001b[33;1mNo data\U00002757")
else:
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP Currency is : \u001b[33;1m" +
          str(response["currency"]))

if str(response["as"]) == "":
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP AS number is :\u001b[33;1m No data\U00002757")
else:
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP AS number is : \u001b[33;1m" + str(response["as"]))

if str(response["mobile"]) == "":
    print("\u001b[38;5;86m[*] \u001b[35;1mTarget IP using Mobile? : \u001b[33;1mNo data\U00002757")
else:
    print("\u001b[38;5;86m[*] \u001b[35;1mIs Target IP using Mobile? : \u001b[33;1m" +
          str(response["mobile"]))

if str(response["proxy"]) == "":
    print("\u001b[38;5;86m[*] \u001b[35;1mIs Target IP using Proxy? : \u001b[33;1mNo data\U00002757")
else:
    print("\u001b[38;5;86m[*] \u001b[35;1mIs Target IP using Proxy? : \u001b[33;1m" +
          str(response["proxy"]))

if str(response["hosting"]) == "":
    print("\u001b[38;5;86m[*] \u001b[35;1mIs Target IP a Hosting IP? : \u001b[33;1mNo data\U00002757")
else:
    print("\u001b[38;5;86m[*] \u001b[35;1mIs Target IP a Hosting IP? : \u001b[33;1m" +
          str(response["hosting"]))

print("\u001b[0m\n")

print("\u001b[37;1mGoogle maps link is : \u001b[36;1mhttps://www.google.com/maps/place/" +
      str(response["lat"]) + "," + str(response["lon"]))

print("\u001b[0m\n")
input("\u001b[7m\u001b[42;1mPress ENTER to exit\u001b[0m")
print("\u001b[0m\n")
