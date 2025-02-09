#My second basic practice with notes. Promotion checker

def calculate_rating (score):
  if score >= 90:
     return "Excellent"
  elif score >= 70:
     return "Good"
  elif score >= 50:
     return "Average"
  elif score >= 40:
     return "Medyo Average" #Tried branch testing 2 here to see what happens
   #Tried another merge here
  else:
     return "Poor"

def check_promotion(rating):
   if rating == "Excellent" or rating == "Good":
      return "Eligible for Promotion"
   else:
      return "Not Eligible for Promotion"
   
def main():
    score = float(input("Enter the employee's performance score (out of 100): "))
    
    if score < 0 or score > 100:
      print ("Invalid numbers, It should be 0 to 100 only please!")
      return

    rating = calculate_rating(score)

    promotion_status = check_promotion (rating)

    print (f"Performance rating: {rating}")
    print (f"Promotion Eligibility: {promotion_status}")

if __name__ == "__main__":
    main()