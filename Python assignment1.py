1)   Write a Python program to get the Fibonacci series between 0 to 50
     Note : The Fibonacci Sequence is the series of numbers :
     0, 1, 1, 2, 3, 5, 8, 13, 21, ....
     Every next number is found by adding up the two numbers before it.
     Expected Output : 1 1 2 3 5 8 13 21 34
     ANS: 
      
     x,y=0,1
     while y<50:
      print(y)
      x,y = y,x+y
      
      
      
 2)Write a Python program that accepts a word from the user and reverse it.
   WTR = input("Enter a word to reverse: ")
   for i in range(len(word) - 1, -1, -1):
      print(word[i], end="")
    
 3) Write a Python program to count the number of even and odd numbers from a series of numbers.
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
    count_odd = 0
    count_even = 0
    for x in numbers:
            if not x % 2:
               count_even+=1
            else:
               count_odd+=1
    print("Number of even numbers :",count_even)
    print("Number of odd numbers :",count_odd)
