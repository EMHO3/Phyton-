with open("./text.txt","r+") as file:
  for line in file:
   print(line)    #\n para hacer salto de linea 
  file.write("Hello World \n")  
  file.write("Hello World3 \n")
  file.write("Hello World3343 \n")  

    