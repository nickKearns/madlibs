#FUNCTIONS TO GET EACH TYPE OF SPEECH
def get_a_noun():
    print("Please enter a noun.")
    given_noun = str(input())
    return given_noun 

def get_a_verb():
        print("Please enter a verb.")
        given_verb = str(input())
        return given_verb

def get_an_adjective():
    print("Please enter an adjective.")
    given_adjective = str(input())
    return given_adjective

def get_verb_ing():
    print("Please enter a verb ending in ing.")
    given_verb_ing = str(input())
    return given_verb_ing

# DISPLAY THE STORY WITH BLANKS
print("Stairway to Heaven Madlib")
print('''There's a (NOUN) who's sure
All that (VERB) is (NOUN)
And she's (VERB ending in ING) a stairway to (NOUN)
When she gets there she (VERB)
If the stores are all (ADJECTIVE)
With a (NOUN) she can get what she came for
Oh oh oh oh and she's buying a stairway to (NOUN)''')

#COLLECT INPUTS
noun1 = get_a_noun()
verb1 = get_a_verb()
noun2 = get_a_noun()
verb2 = get_verb_ing()
noun3 = get_a_noun()
verb3 = get_a_verb()
adjective1 = get_an_adjective()
noun4 = get_a_noun()
noun5 = get_a_noun()

print("There's a " + noun1 + " who's sure")
print("All that " + verb1 + " is " + noun2)
print("And she's " + verb2 + " a stairway to " + noun3)
print("When she gets there she " + verb3)
print("If the stores are all " + adjective1)
print("With a " + noun4 + " she can get what she came for")
print("Oh oh oh oh and she's buying a stairway to " + noun5)



