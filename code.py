file = open(r"C:\Users\Chiranjeev\OneDrive\Desktop\FunctionsPy\text3.txt","r")

no_words=0
no_lines=0

for line in file:
          words=line.split()
          no_words=no_words+len(words)
          line=line.strip()
          no_lines=no_lines+1

file.close()

print("no. of words",no_words)
print("no. of lines",no_lines)