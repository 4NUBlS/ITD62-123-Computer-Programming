# program description
# Basic functions

# import function definition
import function_def as fn

# print author information and date-time when executed
from datetime import datetime # datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S
print("Executed time: ", dt_string)
name = 'xxxxxxxxxxxxxxxxxxxxx'
std_id = 'xxxxxxxx'
lab = 'LP04-1'
print(lab +' Name: '+name+' Student ID: '+ std_id)
print('-----------------------------------------')

# variables declaration

# command scripts
fn.calculate_circle_area(5)
fn.calculate_circle_area(8)

fn.calculate_circle_circumference(9)
fn.calculate_circle_circumference(4)

fn.calculate_retangle_area(3,5)
fn.calculate_retangle_area(3,9)

fn.calculate_triangle_area(2,5)
fn.calculate_triangle_area(5,9)