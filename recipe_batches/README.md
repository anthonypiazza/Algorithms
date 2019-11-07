# Recipe Batches

Write a function that receives a recipe in the form of a dictionary, as well as all of the ingredients you have available to you, also in the form of a dictionary. Both of these dictionaries will have the same form, and might look something like this:

```python
{
  'eggs': 5,
  'butter': 10,
  'sugar': 8,
  'flour': 15
}
```

The keys will be the ingredient names, with their associated values being the amounts. In the case of the recipe dictionary, these amounts will represent the amount of each ingredient needed for the recipe, while in the case of the ingredients dictionary, the amounts represent the amounts available to you. 

Your function should output the maximum number of whole batches that can be made for the supplied recipe using the ingredients available to you, as indicated by the second dictionary. 

For example

```python
# should return 0 since we don't have enough butter!
recipe_batches(
  { 'milk': 100, 'butter': 50, 'flour': 5 },
  { 'milk': 138, 'butter': 48, 'flour': 51 }
)
```

## Testing 

Run the test file by executing `python test_recipe_batches.py`.

You can also test your implementation manually by executing `python recipe_batches.py`.

## Hints

 * If there's a dictionary operation you aren't sure of how to perform in Python, look it up!
 * What's the _minimum_ number of loops we need to perform in order to write a working implementation?

POLYA Process

 1. Ask Q's:
    - Only whole integers or fractions too?
    - All measurement units will be equal for both keys?
  
  2. Planning
    -two arguments passed in 
        1) ingredients needed with values
        2) ingredients available with values
    
    - Instantiate a counter 
    - While all available_ingredients are > 0:

      - Loop over the available ingredients dictionary and subtract each value by the required value in the needed ingredients dictionary

        If all values are positive than increment counter by 1
        Else return counter

  3. Implementation - see code

  4. Optimization 
      - Nested for loops - time complexity is quadratic and could be improved
