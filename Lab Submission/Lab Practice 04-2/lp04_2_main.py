# program description
# User – defined functions

# print author information and date-time when executed
import lp04_2_utilityfunc as lp04
from datetime import datetime # datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S
print("Executed time: ", dt_string)
name = 'xxxxxxxxxxxxxxxxxxxxx'
std_id = 'xxxxxxxx'
lab = 'LP04-2'
print(lab +' Name: '+name+' Student ID: '+ std_id)
print('-----------------------------------------')

# variables declaration

line = "-----------------------------------------"
id_1 = "1234567890121"
id_2 = "1234567890122"

# command scripts

print("The person id '{0}' is {1}.\n{2}".format(id_1,lp04.validate_person_id(id_1),line))
print("The person id '{0}' is {1}.\n{2}".format(id_2,lp04.validate_person_id(id_2),line))