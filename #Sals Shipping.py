#Sals Shipping
weight = 4.8
premium_ground_shipping = 125

#ground shipping

if weight >= 10:
  print ("Ground Total Cost = $" + str( (weight * 4.75) + 20))
elif weight >= 6:
  print ("Ground Total Cost = $" + str( (weight * 4) + 20)) 
elif weight >= 2:
  print ("Ground Total Cost = $" + str( (weight * 3) + 20))
elif weight >= 0:
  print ("Ground Total Cost = $" + str( (weight * 1.5) + 20))

print ("Premium Ground Shipping Option - $" + str(premium_ground_shipping) )

#drone shipping

if weight >= 10:
  print("Drone Total Cost = $" + str(14.25* weight))
elif weight >= 6:
  print("Drone Total Cost = $" + str(12* weight))
elif weight >= 2:
  print("Drone Total Cost = $" + str(9* weight))
elif weight >= 0:
  print("Drone Total Cost = $" + str(4.5* weight))

 