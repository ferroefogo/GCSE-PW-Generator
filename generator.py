import random




WORDS=['elephant','wisteria','cranberry','christmas','rudolph']
CHARS =['*','&','$','%']

def generate_password(min_length, num_words, caps, nums, chars):
    '''Generates a password'''
    password = '' #password starts as empty string
    wordsToChoose = random.sample(WORDS, num_words) #pick a set amount of words (between 1-3) randomly from the list WORDS 
    for word in wordsToChoose: #for every word that is chosen check for the following.
        if caps == True:       #does the user want caps?
            word = word.capitalize()    #if so capitalize
        password = password + word      #add this to the empty string
    if nums == True:            #does the user want numbers?
        password = password + str(random.randint(1,9))  #if so add a random digit between 1-9 to the password
    checkLength = False     #setting up validation loop.
    while checkLength == False: #repeat this until checkLength is True
        if chars == True:       #if the user wants chars (symbols)
            password = password + (random.choice(CHARS))    #add the symbols to the password
        if len(password) >= int(min_length):        #if the length of the password is bigger than the minimum length
            checkLength = True                      #make checkLength True, because this loop doesn't need to continue.
    return password     #return the password as the value for generate_password

'''test portion of the code'''
def test():
    '''code to test the password generator'''
    min_length = 10
    num_words = 3
    caps = False
    nums = True
    chars = False
    password = generate_password(min_length, num_words, caps, nums, chars)
    print(password)

if __name__ == '__main__':
    test()
    
# could be improved by adding every letter to the WORDS list and make it print a random string of letters, numbers, caps, symbols and numbers, though it would make for a hard password to remember.
    
