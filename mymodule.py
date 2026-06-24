import random
import string

def random_user_id():
   characters = string.ascii_lowercase + string.digits
   return random.choice(characters)
