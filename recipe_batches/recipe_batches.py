#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  print(recipe)
  print(recipe['milk'])

  specific_ingredient_makes_batches = 0
  list_of_ingredient_batches = []
  key_match = False
  
  for j in recipe:
    for k in ingredients:
      if j == k:
        key_match = True   
    
    print(f"Key Match: {key_match}")
    if key_match == False:
      return 0

    for i in ingredients:
      print(i)

      specific_ingredient_makes_batches = 0
      while ingredients[i] > 0:
        print(f"Ingredient: {i}, Quantity Remaining: {ingredients[i]}")
        if ingredients[i] - recipe[i] >= 0:
          ingredients[i] = ingredients[i] - recipe[i]
          specific_ingredient_makes_batches += 1
        else:
          ingredients[i] = ingredients[i] - recipe[i]

      list_of_ingredient_batches.append(specific_ingredient_makes_batches)
    
    print(list_of_ingredient_batches)
    for i in range(0, len(list_of_ingredient_batches)-1):
      if list_of_ingredient_batches[i] > list_of_ingredient_batches[i+1]:
        list_of_ingredient_batches[i], list_of_ingredient_batches[i+1] = list_of_ingredient_batches[i+1], list_of_ingredient_batches[i]
    
    print(list_of_ingredient_batches)

  
  return list_of_ingredient_batches[0]



  # for i in ingredients:
  #   print(i)

  #   specific_ingredient_makes_batches = 0
  #   while ingredients[i] > 0:
  #     print(f"Ingredient: {i}, Quantity Remaining: {ingredients[i]}")
  #     if ingredients[i] - recipe[i] >= 0:
  #       ingredients[i] = ingredients[i] - recipe[i]
  #       specific_ingredient_makes_batches += 1
  #     else:
  #       ingredients[i] = ingredients[i] - recipe[i]

  #   list_of_ingredient_batches.append(specific_ingredient_makes_batches)
  
  # print(list_of_ingredient_batches)
  # for i in range(0, len(list_of_ingredient_batches)-1):
  #   if list_of_ingredient_batches[i] > list_of_ingredient_batches[i+1]:
  #     list_of_ingredient_batches[i], list_of_ingredient_batches[i+1] = list_of_ingredient_batches[i+1], list_of_ingredient_batches[i]
  
  # print(list_of_ingredient_batches)

  # return list_of_ingredient_batches[0]

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))