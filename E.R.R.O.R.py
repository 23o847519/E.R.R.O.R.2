#config
#plese enter your name here
name = ("Bearry")

#config

import os
import random
from rich.console import Console
console = Console()

print("\t*************************************************")
console.print("\t**[bold red]Emergency Relapse Reaction Organised Response[/]**")
print("\t*************************************************")

print("Welcome to E.R.R.O.R " + name + "!")

print("Select A Emergency Response" + name + ":")
print("Drugs")
print("PMO")
print("Anxiety")
print("Paranoia")
print("other")

tim222 = ("Flee the evil desires of youth and pursue righteousness, faith, love and peace, along with those who call on the Lord out of a pure heart.")

list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6]
list4 = [1, 2]


Emergency1 = input("Enter emergency here: ")
if Emergency1 =="Drugs":
	print(random.choice(list1)) 
elif Emergency1 == "PMO":
	print(random.choice(list2))
elif Emergency1 == "Anxiety":
	print(random.choice(list3))
elif Emergency1 == "Other":
	print(random.choice(list4))
exit = input("Press any key to exit: ")


os.system('clear')

