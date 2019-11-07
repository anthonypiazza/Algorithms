# Stock Prices

You want to write a bot that will automate the task of day-trading for you while you're going through Lambda. You decide to have your bot just focus on buying and selling Amazon stock. 

Write a function `find_max_profit` that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here.

For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices. 

## Testing

Run the test file by executing `python test_stock_prices.py`.

You can also test your implementation manually by executing `python stock_prices.py [integers_separated_by_a_single_space]`

## Hints

 For this problem, we essentially want to find the maximum difference between the smallest and largest prices in the list of prices, but we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it; it can't come after it in the list of prices. 

 So what if we kept track of the `current_min_price_so_far` and the `max_profit_so_far`? 


1. Ask Q's:
    - What type of number? Integers only or floats as well 
    - What if there are two of the same max profit? 
    - What type of data do you want to return?

2. Planning

 current_min_price_so_far = track lowest price
 max_profit_so_far = track max profit so far

 start at 0 index and subtract 0 index from each of the other indexes
 log the highest return

 start at 1 index and subtract that index from its neighbor and so on
 log each return and compare to max_profit

 continue to loop once you have reached the last index

 return max_profit

 3. Implement - see code

 4. Optimize 
     - Used a nested for loop so speed could definitely be optimized
     - Could abstract away from stated variables more to free up space complexity