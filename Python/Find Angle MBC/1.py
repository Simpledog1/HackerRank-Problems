# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB = int(input())
BC = int(input())
result = math.degrees(math.atan(AB/BC))
result = round(result)
print(str(result) + "\u00b0")
