#!/usr/bin/python

import argparse

def find_max_profit(prices):

  print(prices)
  max_profit_so_far = prices[1] - prices[0]
  
  for i in range(0, len(prices)-1):
    
    current_buy_value = prices[i]
    current_high_value_in_loop = 0
    
    print(f"Current Buy Value: {current_buy_value}")

    for j in range(i+1, len(prices)):
      if prices[j] > current_high_value_in_loop:
        current_high_value_in_loop = prices[j]
      
    current_loop_max_profit = current_high_value_in_loop - current_buy_value

    if max_profit_so_far < current_loop_max_profit:
      max_profit_so_far = current_loop_max_profit
  
  return max_profit_so_far



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))