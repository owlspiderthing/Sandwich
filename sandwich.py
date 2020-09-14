from time import *
print("Remember to only input the number of the answer.")
sleep(1)
print("It's time to make a sandwich. First, the carbs.")
carb = input("1) Bun or 2) Bread?")
print("")

if carb == "1":
  
  carb = "bun"
  sleep(1)
  
  print("What kind of bun?")
  carbs = input("1) Brioche, 2) White, 3) Seeded, or 4) Wholegrain?")
  print("")
  
  if carbs == "1":
    carbs = "a brioche"
  elif carbs == "2":
    carbs = "a white"
  elif carbs == "3":
    carbs = "a seeded"
  elif carbs == "4":
    carbs = "a wholegrain"
  
  
elif carb == "2":
  carb = "bread"
  sleep(1)
  
  print("What kind of bread?")
  carbs = input("1) White, 2) Wholegrain, 3) 50/50, 4) Sourdough, or 5) Crusty?")
  print("")
  
  if carbs == "1":
    carbs = "white"
  elif carbs == "2":
    carbs = "wholegrain"
  elif carbs == "3":
    carbs = "50/50"
  elif carbs == "5":
    carbs = "crusty"
  elif carbs == "4":
    carbs = "sourdough"
sleep(1)  
  
print("OK, next, the filling.")
filling = input("1) Meat, 2) Cheese, 3) Egg, 4) Meat and Cheese, 5) Egg and Cheese, 6) Meat and Egg,  or 7) All Three")
print("")
if filling == "1":
  sleep(1)
  print("What kind of meat?")
  meat = input("1) Bacon, 2) Ham, 3) Burger, or 4) Sausages?")
  if meat == "1":
    meat = "bacon"
  elif meat == "2":
    meat = "ham"
  elif meat == "3":
    meat = "burger"
  elif meat == "4":
    meat = "sausage"
    
  filling = meat
  
if filling == "2":
  sleep(1)
  print("What kind of cheese?")
  cheese = input("1) Cheddar, 2) Red Leicester, 3) Halloumi, or 4) Stilton?")
  print("")
  if cheese == "1":
    cheese = "cheddar"
  elif cheese == "2":
    cheese = "red leicester"
  elif cheese == "3":
    cheese = "halloumi"
  elif cheese == "4":
    cheese = "stilton"
    
  filling = cheese
  
if filling == "3":
  sleep(1)
  print("What kind of egg?")
  egg = input("1) Fried Egg, 2) Poached Egg, 3) Omelette, or 4) Scrambled Egg?")
  print("")
  if egg == "1":
    egg = "fried egg"
  elif egg == "2":
    egg = "poached egg"
  elif egg == "3":
    egg = "omelette"
  elif egg == "4":
    egg = "scrambled egg"
  filling = egg
  
if filling == "4":
  sleep(1)
    
  print("What kind of meat?")
  sleep(1)
  meat = input("1) Bacon, 2) Ham, 3) Burger, or 4) Sausages?")
  print("")
  if meat == "1":
    meat = "bacon"
  elif meat == "2":
    meat = "ham"
  elif meat == "3":
    meat = "fish finger"
  elif meat == "4":
    meat = "sausage"
    
    print("What kind of cheese?")
  cheese = input("1) Cheddar, 2) Wensleydale, 3) Halloumi, or 4) Stilton?")
  print("")
  if cheese == "1":
    cheese = "cheddar"
  elif cheese == "2":
    cheese = "wensleydale"
  elif cheese == "3":
    cheese = "halloumi"
  elif cheese == "4":
    cheese = "stilton"
  
  filling = str(meat) + ", " + str(egg)
  
if filling == "5":
  print("What kind of egg?")
  egg = input("1) Fried Egg, 2) Poached Egg, 3) Omelette, or 4) Scrambled Egg?")
  sleep(1)
  print("")
  if egg == "1":
    egg = "fried egg"
  elif egg == "2":
    egg = "poached egg"
  elif egg == "3":
    egg = "omelette"
  elif egg == "4":
    egg = "scrambled egg"
  
  print("What kind of cheese?")
  cheese = input("1) Cheddar, 2) Wensleydale, 3) Halloumi, or 4) Stilton?")
  print("")
  if cheese == "1":
    cheese = "cheddar"
  elif cheese == "2":
    cheese = "wensleydale"
  elif cheese == "3":
    cheese = "halloumi"
  elif cheese == "4":
    cheese = "stilton"
  
  filling = str(egg) + ", " + str(cheese)
    
if filling == "6":
  sleep(1)
  print("What kind of meat?")
  meat = input("1) Bacon, 2) Ham, 3) Burger, or 4) Sausages?")
  if meat == "1":
    meat = "bacon"
  elif meat == "2":
    meat = "ham"
  elif meat == "3":
    meat = "burger"
  elif meat == "4":
    meat = "sausage"
    
  print("What kind of egg?")
  egg = input("1) Fried Egg, 2) Poached Egg, 3) Omelette, or 4) Scrambled Egg?")
  sleep(1)
  print("")
  if egg == "1":
    egg = "fried egg"
  elif egg == "2":
    egg = "poached egg"
  elif egg == "3":
    egg = "omelette"
  elif egg == "4":
    egg = "scrambled egg"
    
  filling = str(meat) + ", " + str(egg)
  
if filling =="7":
  print("What kind of meat?")
  sleep(1)
  meat = input("1) Bacon, 2) Ham, 3) Burger, or 4) Sausages?")
  print("")
  if meat == "1":
    meat = "bacon"
  elif meat == "2":
    meat = "ham"
  elif meat == "3":
    meat = "fish finger"
  elif meat == "4":
    meat = "sausage"
    
    print("What kind of cheese?")
  cheese = input("1) Cheddar, 2) Wensleydale, 3) Halloumi, or 4) Stilton?")
  print("")
  if cheese == "1":
    cheese = "cheddar"
  elif cheese == "2":
    cheese = "wensleydale"
  elif cheese == "3":
    cheese = "halloumi"
  elif cheese == "4":
    cheese = "stilton"
    
    print("What kind of egg?")
  egg = input("1) Fried Egg, 2) Poached Egg, 3) Omelette, or 4) Scrambled Egg?")
  sleep(1)
  print("")
  if egg == "1":
    egg = "fried egg"
  elif egg == "2":
    egg = "poached egg"
  elif egg == "3":
    egg = "omelette"
  elif egg == "4":
    egg = "scrambled egg"
  
  filling = str(meat) + ", " + str(cheese) + ", " + str(egg)
  

  
print("Almost done, now for the salad.")
salad = input("1) Lettuce, 2) Cucumber, 3), Tomato, 4) Red Pepper?, 5) All of the above, or 6) None of the above")
sleep(1)
print("")
if salad == "1":
  salad = "lettuce"
elif salad == "2":
  salad = "cucumber"
elif salad == "3":
  salad = "tomato"
elif salad == "4":
  salad = "red pepper"
elif salad == "5":
  salad = "a lettuce, cucumber, tomato, and red pepper salad"
elif salad == "6":
  salad = "none"
  
print("And finally, the sauce.")
sauce = input("1) Mayonnaise, 2) Ketchup, 3) Peri Peri, 4) Mustard?, or 5) None of the above")
print("")
if sauce == "1":
  sauce = "mayonnaise"
elif sauce == "2":
  sauce = "ketchup"
elif sauce == "3":
  sauce = "peri peri"
elif sauce == "4":
  sauce = "mustard"
elif sauce == "5":
  sauce = "none"

sleep(1)
if salad == "none":
  print("Your sandwich is a " + filling + " sandwich on " + carbs + " " + carb + " with a " + sauce + " sauce. Enjoy!")
elif sauce == "none":
  print("Your sandwich is a " + filling + " and " + salad + " sandwich on " + carbs + " " + carb + ". Enjoy!")
else:
  print("Your sandwich is a " + filling + " and " + salad + " sandwich on " + carbs + " " + carb + " with a " + sauce + " sauce. Enjoy!")

