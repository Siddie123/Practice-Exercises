import statistics
def calculate():
   
   lst = []
   elements = int(input("Enter the no. of elements: "))
   for elements in range (0,elements):
      ele = int(input())
      lst.append(ele)
      
   #Mean 
   length = len(lst)
   addition = sum(lst)
   mean = addition/length
   
   
   #Max 
   maximum = max(lst)
   minimum = min(lst)
   
   print(f"mean: {mean}")
   print(f"maximum: {maximum}")
   print(f"Minimum: {minimum}")

calculate()
      
      
      
      
      
      
   
