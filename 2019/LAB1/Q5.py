# a is day number , b is month
a = int(input())
b = input().upper()
if(b=="JANUARY"):
    if(a>=20 and a<=31):
        print("Aquarius")
    else:
        print("capricon")

elif(b=="FEBUARY"):
    if (a >= 19 and a <= 30):
        print("Aquarius")
    else:
        print("Aquarius")

elif (b == "MARCH"):
    if (a >= 21 and a <= 31):
        print("Aries")
    else:
        print("Pisces")

elif (b == "APRIL"):
    if (a >= 20 and a <= 30):
        print("Taurus")
    else:
        print("Aries")

elif (b == "MAY"):
    if (a >= 21 and a <= 31):
        print("Gemini")
    else:
        print("Taurus")

elif (b == "JUNE"):
    if (a >= 21 and a <= 30):
        print("Cancer")
    else:
        print("Gemini")

elif (b == "JULY"):
    if (a >= 23 and a <= 31):
        print("Leo")
    else:
        print("cancer")

elif (b == "AUGUST"):
    if (a >= 23 and a <= 31):
        print("Virgo")
    else:
        print("Leo")

elif (b == "SEPTEMBER"):
    if (a >= 23 and a <= 30):
        print("Libra")
    else:
        print("Virgo")

elif (b == "OCTOBER"):
    if (a >= 23 and a <= 31):
        print("Scorpio")
    else:
        print("Libra")

elif (b == "NOVEMBER"):
    if (a >= 22 and a <= 30):
        print("Sagittarius")
    else:
        print("Scorpio")

elif (b == "DECEMBER"):
    if (a >= 22 and a <= 31):
        print("Capricon")
    else:
        print("Sagittarius")

