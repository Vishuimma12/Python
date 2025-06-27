i=3
# while condition:    
print("While loop example")
while i != 0: # here the condition is i != 0
    print("meow")
    i=i-1 # this will make the condition false eventually


# for variable in iterable:for i in range(3): # here the iterable is range(3) which generates 0, 1, 2

print("\nFor loop example")
for i in [0,1,2]: # here the iterable is a list [0, 1, 2]
    print("meow")


print("\nFor loop with range example")
for _ in range(3): # here the iterable is range(3) which generates 0, 1, 2.  _ is used to indicate that we don't need the loop variable
    print("meow") 

print("\nUsing print with multiplication")
print("meow \n" * 3, end="") # this will print "meow" 3 times, equivalent to the for loop above end="" prevents adding a new line at the end

print("\nUsing input with for loop") 
a=int(input("Enter a number: "))
for a in range(a): # here the iterable is range(a) which generates 0 to a-1
    print("meow") # this will print "meow" a times


print("\nUsing input with while loop till infinite loop")
while True: # this will create an infinite loop
    n= int(input("Enter a number: "))
    if n > 0:
        break
    
for _ in range(n): 
    print("meow") 


print("\nUsing functions with loops")
def main():
    number = get_number()
    meow(number) 
    
def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main() 
