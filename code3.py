from os import read


with open(r"C:/Users/Chiranjeev/OneDrive/Desktop/FunctionsPy/text3.txt","r") as a:
          data_a=a.read()

with open(r"C:/Users/Chiranjeev/OneDrive/Desktop/FunctionsPy/text2.txt","r") as b:
          data_b=b.read()

with open(r"C:/Users/Chiranjeev/OneDrive/Desktop/FunctionsPy/text2.txt","w") as b:
          b.write(data_a)    
with open(r"C:/Users/Chiranjeev/OneDrive/Desktop/FunctionsPy/text3.txt","w") as a:
          a.write(data_b)                   
