#PSET 1

# 1. Exercise
count = 0
v = ['a','e','i','o','u']
for i in s:
    if i in v:
        count +=1
print('Number of vowels:', count)
# 2. Exercise
count = 0
v = ['a','e','i','o','u']
for i in s:
    if i in v:
        count +=1
print('Number of vowels:', count)

# 3. Exercise
string1 = ''
otro1 = ''
otro2 = ''

for i in range(len(s)):
    try:
        if s[i] <= s[i+1]:
            if string1 == '':
                string1 = s[i:i+2]
            else:
                string1 = string1 + s[i+1]
        else:
            if otro2 == '':
                otro2 = string1
                string1 = ''
            else:
                if len(otro1)> len(string1):
                    otro1 = otro1
                    string1 = ''
                elif len(otro1) == len(string1):
                    otro1 = otro1
                    string1 =  ''
                else:
                    otro1 = string1
                    string1 =  ''
    except:
        if len(string1) > len(otro2) and len(string1) > len(otro1):
            print('Longest substring in alphabetical order is:', string1)
        elif otro1 == '' and otro2 == '':
            print('Longest substring in alphabetical order is:', 'z')
        elif len(otro2) == len(otro1):
            print('Longest substring in alphabetical order is:', otro2)
        elif len(otro2) > len(otro1): 
            print('Longest substring in alphabetical order is:', otro2)
        else: 
            print('Longest substring in alphabetical order is:', otro1)

#PSET 2
# Exercise 1
for i in range(0,12):
    minimum_monthly_payment = monthlyPaymentRate * balance
    monthly_unpaid_balance = balance - minimum_monthly_payment
    interest = (annualInterestRate/12) * monthly_unpaid_balance
    balance = monthly_unpaid_balance + interest
print('Remaining balance: ',round(balance,2))

# Exercise 2
original = balance
month = 0
minimum_monthly_payment = 0
while balance > 0:
    minimum_monthly_payment += 10
    balance = original
    month = 0
    while month < 12:
        monthly_unpaid_balance = balance - minimum_monthly_payment
        interest = (annualInterestRate/12) * monthly_unpaid_balance
        balance = monthly_unpaid_balance + interest
        month += 1

     
print('Lowest Payment: ',minimum_monthly_payment)


# Exercise 3
monthInterest = annualInterestRate / 12
lowerBound = balance / 12
higherBound = (balance *(1+monthInterest)**12)/12.0

ans = (higherBound + lowerBound)/2.0

month = 0
original = balance
while abs(balance) >=0.01:
    ans = (higherBound + lowerBound)/2.0
    balance = original
    while month < 12:
        month +=1
        balance = balance - ans
        interest = balance * monthInterest
        balance = balance + interest
    month = 0
    if balance >0:
        lowerBound = ans
    else:
        higherBound = ans
print('Lowest payment: ', round(ans,2))


#PSET 3

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    finded_list = [i for i in secretWord if i in lettersGuessed]
    
    if not finded_list:
        return False

    boolean_list = []
    for find_letter in finded_list:
        if find_letter in lettersGuessed:
            lettersGuessed.remove(find_letter)
            boolean_list.append(True)
        else:
            boolean_list.append(False)
    ans = all(boolean_list)
    return ans


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    finded_list = [i for i in secretWord if i in lettersGuessed]
    final_string = ''
    if not finded_list:
        for i in range(len(secretWord)):
            final_string += "_ "
        return final_string
    for i in range(len(secretWord)):
        if secretWord[i] in finded_list:
            final_string += secretWord[i]
        else:
            final_string += "_"
            
    return final_string


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    strings = ''
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            strings += i 
    return strings


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    guesses = 8
    word_len = len(secretWord)
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(word_len))
    print('-------------')
    while guesses > 0:
        print('You have {} guesses left.'.format(guesses))
        print('Available letters:{}'.format(getAvailableLetters(lettersGuessed))) #La primera ronda va vacio
        guess = input('Please guess a letter:')
        guessInLowerCase = guess.lower()
        if guessInLowerCase not in lettersGuessed:
            lettersGuessed.append(guessInLowerCase)
            # print(lettersGuessed)
            # if isWordGuessed(secretWord, lettersGuessed):
            if guessInLowerCase in secretWord:
                print('Good guess: {}'.format(getGuessedWord(secretWord, lettersGuessed))) # Si es verdadero tiene que mostrar lo que tiene
                print('-------------')
                # print(lettersGuessed)
                if  set(secretWord) <= (set(lettersGuessed)):
                    print('Congratulations, you won!')
                    break
                if guesses <1:
                    print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))
            else:
                print("Oops! That letter is not in my word: {}".format(getGuessedWord(secretWord, lettersGuessed)))
                print('-------------')
                guesses -= 1
                if guesses <1:
                    print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))
        else:
            print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed)))
            print('-------------')
            continue


# PSET 4
def getWordScore(word, n:int =7):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    
    letter_points = []
    if word == '':
        return 0
    for i in word:
        letter_points.append(SCRABBLE_LETTER_VALUES[i])
        partial_score = sum(letter_points)*len(word)
    if len(word) == n:
        final_score = partial_score +50
        return final_score
    else:
        return partial_score
    

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    updated_hand = {}
    for letter in hand.keys():
        if letter in word:
            new_value = 0
            value_to_delete = hand[letter]
            if word.count(letter) > 1:
                new_value = value_to_delete-word.count(letter)
            else:
                new_value = value_to_delete-1
            updated_hand[letter] = new_value
        else:
            value_to_delete = hand[letter]
            updated_hand[letter] = value_to_delete
    return updated_hand


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if word not in wordList:
        return False
    string = ''
    for letter in hand.keys():
        valor = hand[letter]
        if valor >1:
            string += str(letter)*valor
        else:
            string += str(letter)
    # print(string)
    boolean_list = []
    for lett in word:
        if lett in string:
            boolean_list.append(True)
            string = string.replace(lett,'',1)
            # print('segundo print',string)
        else:
            boolean_list.append(False)
    # print(boolean_list)
    if all(boolean_list):
        return True
    else:
        return False
    
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    number = sum(hand.values())
    return number

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    total_score = 0 # Keep track of the total score
    
     
    while calculateHandlen(hand) > 0:# if all(hand.values()) == 0: # As long as there are still letters left in the hand:
    
        print('Current hand:', end=' '), displayHand(hand)
        
        input_word = input('Enter word, or a "." to indicate that you are finished: ' ) # Ask user for input
        
        if input_word == '.': # If the input is a single period:
        
            break # End the game (break out of the loop)

            
        else: # Otherwise (the input is not a single period):
        
            if not isValidWord(input_word, hand, wordList): # If the word is not valid:
            
                print('Invalid word, please try again. \n') # Reject invalid word (print a message followed by a blank line)

            else: # Otherwise (the word is valid):
                partial_score = getWordScore(input_word, n)
                total_score += partial_score

                print('" {0} " earned {1} points. Total: {2} points.\n'.format(input_word, partial_score, total_score)) # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                
                hand = updateHand(hand, input_word) # Update the hand 
                
    if calculateHandlen(hand) == 0:
        print("Run out of letters. Total score: {} points.".format(total_score)) # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    else:
        print('Goodbye! Total score: {} points.'.format(total_score))

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    #wordList = loadWords()
    played_games = 0
    while True:
        word = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        if word == 'r' and played_games == 0:
            print('You have not played a hand yet. Please play a new hand first!')
        elif word == 'r' and played_games > 0:
            #jugar la mano anterior coja el dealhand almacenado
            playHand(hand, wordList, HAND_SIZE)
        elif word == 'n':
            hand = dealHand(HAND_SIZE)
            # Aca va play hand
            playHand(hand, wordList, HAND_SIZE)
            # Pensar donde va dealHand
            played_games += 1
        elif word == 'e':
            # End Game
            break
        else:
            print('Invalid command.')

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    played_games = 0
    validation = True
    while validation:
        word = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        if word == 'r' and played_games == 0:
            print('You have not played a hand yet. Please play a new hand first!')
        elif word == 'r' and played_games > 0:
            menu_2 = input('Enter u to have yourself play, c to have the computer play:')
            if menu_2 == 'u':
                playHand(hand, wordList, HAND_SIZE)
            elif menu_2 == 'c':
                compPlayHand(hand, wordList, HAND_SIZE)
            else:
                print('Invalid command.')
        elif word == 'n':
            loop = True
            while loop:
                menu_2 = input('Enter u to have yourself play, c to have the computer play:')
                if menu_2 == 'u':
                    hand = dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
                    loop = False
                elif menu_2 == 'c':
                    hand = dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList, HAND_SIZE)
                    loop = False
                else:
                    print('Invalid command.')
            played_games += 1
        elif word == 'e':
            # End Game
            validation = False
            break
        else:
            print('Invalid command.')

# PSET 5
class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        import string
        lower = string.ascii_lowercase * 2 
        upper = string.ascii_uppercase * 2
        alphabet = lower + upper
        return {
            letter:
            (alphabet[alphabet.find(letter) + shift])
            for letter in alphabet
        }
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        d = self.build_shift_dict(shift)
        return "".join(d.get(letter, letter) for letter in self.get_message_text())
    
    class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self,shift=shift)
        self.message_text_encrypted = Message.apply_shift(self, shift=shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self,shift=shift)
        self.message_text_encrypted = Message.apply_shift(self, shift=shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        self.message_text = text
        
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        dictio = {}
        val = 0
        for k in range(0,25):
            val = 0
            decoded_msg = self.apply_shift(26-k)
            decoded_list = decoded_msg.split(' ')
            for word in decoded_list:
                if is_word(self.get_valid_words(),word):
                    val +=1
            dictio[k] = val
        valor_maximo = max(dictio.items(), key=lambda x: x[1])
        return (valor_maximo[0], self.apply_shift( 26 - valor_maximo[0]))
    

def decrypt_story():
    instancia = CiphertextMessage(get_story_string())
    return instancia.decrypt_message()