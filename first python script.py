#If you're from the future and#
#you're cringing, sorry. I was 14.#
import time
name = input("Enter your name punk: ")

while (not name.isalpha()):
  print ("Try again but with letters ;)")

  name = input("Enter your name punk: ")
  
age = input("How old are you, sucker?: ")
##if age.isnumeric():
##  print (age)
##else:
##   print ("Try again but with numbers ;)")
##   time.sleep(1)
##   age = input("How old are you, sucker?: ")

while (not age.isnumeric()):
    print ("Try again but with numbers ;)")

    age = input("How old are you, sucker?: ")
print (age)
time.sleep(1)
print ("OK, " + name + ", you are " + age + " years old?")
time.sleep(1)
verify = input("Is this correct? Y for yes, N for no(must be caps): ")
if verify == "Y":
    print ("Yay!")
    time.sleep(1)
    print ("Bye!")
    time.sleep(1)
elif verify == "N":
    print ("Try again")
    time.sleep(1)
    print("Sorry I couldn't loop at the time of making")
else:
    print("y tho")
    time.sleep(1)
    print("Sorry I couldn't loop at the time of making")

    




