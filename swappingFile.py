def swapFileData():
  var1= input("enter files name:- ")
  var2 = input("enter files name:- ")


  with open(var1, 'r') as a: 
    data_a = a.read()

  with open(var2, 'r') as b: 
   data_b = b.read()

  with open(var1, 'w') as a: 
    a.write(data_b)

  with open(var2, 'w') as b: 
    b.write(data_a)

swapFileData()