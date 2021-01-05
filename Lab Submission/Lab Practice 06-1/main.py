from datetime import datetime
import json

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
locations = {
    "1": "กรุงเทพมหานคร",
    "2": "จังหวัดกาญจนบุรี",
    "3": "จังหวัดจันทบุรี",
    "4": "จังหวัดฉะเชิงเทรา",
    "5": "จังหวัดชุมพร",
    "6": "จังหวัดชลบุรี",
    "7": "จังหวัดตราด",
    "8": "จังหวัดตาก",
    "9": "จังหวัดนครนายก",
    "10": "จังหวัดนครปฐม",
    "11": "จังหวัดนนทบุรี",
    "12": "จังหวัดปทุมธานี",
    "13": "จังหวัดประจวบคีรีขันธ์",
    "14": "จังหวัดปราจีนบุรี",
    "15": "จังหวัดพระนครศรีอยุธยา",
    "16": "จังหวัดเพชรบุรี",
    "17": "จังหวัดราชบุรี",
    "18": "จังหวัดระนอง",
    "19": "จังหวัดระยอง",
    "20": "จังหวัดลพบุรี",
    "21": "จังหวัดสิงห์บุรี",
    "22": "จังหวัดสมุทรปราการ",
    "23": "จังหวัดสมุทรสงคราม",
    "24": "จังหวัดสมุทรสาคร",
    "25": "จังหวัดสุพรรณบุรี",
    "26": "จังหวัดสระแก้ว",
    "27": "จังหวัดสระบุรี",
    "28": "จังหวัดอ่างทอง",
    "0": "อื่นๆ"
}

persondict = {
    "datatime": dt_string,
    "fname": str(input("Enter first name: ")),
    "lname": str(input("Enter last name: ")),
    "age": int(input("Enter age: ")),
    "body_temp": float(input("Enter body temperature: ")),
    "location": "",
    "risk": False,
    "covid": False
}

print("Location")
for x, y in locations.items():
    print("{0}. {1}".format(x, y))
persondict.update({"location": int(input("Enter location number: "))})
if persondict.get("location") == 0:
    persondict.update({"risk": False})
elif persondict.get("body_temp") > 37.5 and str(persondict.get("location")) in locations.keys():
    persondict.update({"covid": True})
elif str(persondict.get("location")) in locations.keys():
    persondict.update({"risk": True})
if persondict.get("body_temp") > 37.5:
    persondict.update({"risk": True})
print("JSON={0}".format(json.dumps(persondict)))