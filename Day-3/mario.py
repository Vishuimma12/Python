
def main():
  square(3);

def square(x):

  for row in range(x):
    # for each row, we print x number of columns
  
    for col in range(x): # here we are using a for loop to print the columns
      print("#", end="")
    print()  

#  print("#" * x) # this will print x number of columns in each row
    # for i in range(x):
    #   print("#" * x)
      
main()




# Output:


###
###
###
