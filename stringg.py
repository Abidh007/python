string=input("enter a string")
str_len=len(string)
if(str_len>2):
  if(string[-3]=="ing"):
    newText=string,replace("ing","Iy",1);

    print("the new string:",mewText)
else:
    print("the new string:",string+'ing')
