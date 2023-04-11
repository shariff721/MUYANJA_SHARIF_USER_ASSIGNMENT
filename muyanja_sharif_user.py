
class User:
    def __init__(self, first_name, last_name, email, age, is_reward_member = False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = is_reward_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(f"First Name: {self.first_name}\n Last Name: {self.last_name}\n Email: {self.email}\n Age: {self.age}\n Gold Points: {self.gold_card_points}\n Is Reward Member: {self.is_reward_member}")
    
    def enroll(self):
        if self.is_reward_member == False:
            self.is_reward_member = True
            self.gold_card_points = 200
        else:
            print("Your are  already A rewards Memmer")
    
    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points = self.gold_card_points - amount
        else:
            print("You Have No More Points To Spend")
        return self.gold_card_points


sharif = User("Sharif", "Muyanja", "smuyanja11@gmail.com", 33)
ayah = User("maryam", "Ayah", "mayah01@gmail.com", 13)
dino = User("imran", "dino", "imrandinio100@gmail.com",8)


sharif.enroll()

sharif.spend_points(50)

ayah.enroll()

ayah.spend_points(80)


sharif.display_info()
ayah.display_info()
dino.display_info()

sharif.enroll()