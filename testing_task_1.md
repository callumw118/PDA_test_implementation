### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.
# There are 6 errors in total. 

```python

class CardGame:
  
  def checkforAce(self, card):
    if card.value = 1: # Should be ==
      return true # true requires capitalisation
    else  # Missing :
      return false # false requires capitalisation

  dif highest_card(self, card1 card2) # dif should be def and missing comma between card1 and card2. Also missing : at end of function
    if card1.value > card2.value # Missing :
      return card # card not defined, should probably be card1
    else  # Missing :
      return card2
 

 def cards_total(cards): # Requires self in function parameters and needs to be tabbed in
   total # total not set to a value
   for card in cards:
     total += card.value # Remove card.value and replace with 1
     return "You have a total of" + total # Should be outside of for loop and be string formatted


```
