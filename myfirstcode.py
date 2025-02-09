#First Code with Notes for now

def calculate_perimeter(length, width):
  perimeter = 2 * (length + width)
  return perimeter

length = float(input("Enter the length of the rectangle:"))
width = float(input("Enter the width of the rectangle:"))

result = calculate_perimeter(length, width)

print (f"The perimeter of the rectangle is: {result}")

