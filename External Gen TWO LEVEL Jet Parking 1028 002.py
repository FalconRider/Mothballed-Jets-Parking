# P. Gitschner   October 2020 

#External PAIRS GENERATOR  TWO LEVELS  mit Graph


# make Pairs for a -  w  x 2 matrix
# starting at   -   a  , total nodes z = w  . 2
#zone of interference 1  r

import datetime
timestamp = datetime.datetime.now()


####### Enter ####
w = 8
#################

z = w *2 
a = 1
i = a
#adding variable spacing  wip
r = 1
#adding offset  wip
offset = 0

#TopRow -----------------------------------


myString = "(["

while i <= w-r:
  j = str(i)
  #adding variable spacing
  k = str(i+r)
  
  myString = myString +"("+ j + ", " + k +" )"
  i += 1
  # comma between pairs
  myString = myString + "," 
  

#last pair of row
#myString = myString +"("+ str(z-w) + "," + str(a) +")" +"])"

# Second row ----------------------------------
i += 1


while i < w+w:
  j = str(i)
  #adding variable spacing
  k = str(i+r)
  
  myString = myString +"("+ j + ", " + k +" )"
  i += 1
  # comma between pairs
  myString = myString + ","

#--below------------------------------
i = a
while i <= w:
  j = str(i)
  #adding variable spacing
  k = str(i+r+w-1)
  
  myString = myString +"("+ j + ", " + k +" )"
  i += 1
  # comma between pairs
  myString = myString + ","
   

#--slant right-------------------------  
i = 1
while i < w:
  j = str(i)
  #adding variable spacing
  k = str(i+r+w)
  
  myString = myString +"("+ j + ", " + k +" )"
  i += 1
  # comma between pairs
  myString = myString + ","
  
 #--slant left-------------------------

i = 2
while i <= w:
  j = str(i)
  #adding variable spacing
  k = str(i+r+w-1-1)
  
  myString = myString +"("+ j + ", " + k +" )"
  i += 1
  # comma between pairs
  myString = myString + ","
  
 


 # endcap ---------------------------------

myString = myString + "])"







#   adjust your  printout requirments ---------------REPORT---------***
print(" ")
print("--------------------------------------------------------------")
print("Visual Run test ")
print("Run                             ",timestamp)
print("--------------------------------------------------------------")


print("Start             ", a)
print("Length of row     ", w)
print("Spacing   ", r)
print ("END   ",z)


print("---------------------------------------------------------")
print("cut AND PASTE THIS")
print("")
print (myString)



