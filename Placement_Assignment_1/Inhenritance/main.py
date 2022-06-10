class Dad:
    def good_height(self):
        print('Good height')

class Mom:
    def good_features(self):
        print('Great features')

class Kid(Dad, Mom):
    def quick_learer_skill(self):
        print('Quick learner') 


# Here we can see that kid inherited mom and dad booth good_features and good_height this is
# an example of inheritance in action 

kid = Kid()
kid.good_features()
kid.good_height()



