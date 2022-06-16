# Write your code below: 
from contextlib import contextmanager 

@contextmanager
def generic(card_type,sender_name,recipient):
  open_card =open(card_type,'r')
  new_card = open(f"{sender_name}_generic.txt","w")
  try:
    new_card.write(f'Dear {recipient},\n')
    new_card.write(open_card.read())
    new_card.write(f"\n Sincerely, {sender_name}")
    yield new_card
  finally:
    new_card.close()
    open_card.close()

with generic('thankyou_card.txt',"Mwenda","Amanda") as card:
  print('Card Generated!')
  
with open('Mwenda_generic.txt','r') as first_order:
  print(first_order.read())

class personalized:
  def __init__(self, sender,recipient):
    self.sender = sender
    self.recipient = recipient
    self.open_card = open(f'{sender}_personalized.txt','w')
  def __enter__(self):
    self.open_card.write(f'Dear {self.recipient},\n')
    return self.open_card
  def __exit__(self,*exc):
    self.open_card.write(f'\n Sincerely, {self.sender}')
    self.open_card.close()


with personalized('John','Michael') as second_order:
  second_order.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don't say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")

with generic('happy_bday.txt','Josiah','Remy') as third_order:
  with personalized('Josiah','Esther') as forth_order:
    forth_order.write("Happy Birthday!! I love you to the moon and back. Even though you're a pain sometimes, you're a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You're getting old!")

with open('Josiah_personalized.txt','r') as personal, open('Josiah_generic.txt','r') as generic:
  print(personal.read())
  print(generic.read())
