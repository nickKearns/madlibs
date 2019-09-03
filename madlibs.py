from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def show_story():
        return render_template()

import datetime
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

current_date = datetime.today()
new__completed_story = open("" + str(current_date) + "_story.txt", 'w+')

# OPEN THE STORY TO BE PRINTED
story = open("mlstory.txt", 'r')

# DISPLAY THE STORY WITH BLANKS
print("Stairway to Heaven Madlib")
print(story.read())
story.close()

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

line1 = "There's a " + noun1 + " who's sure\n"
line2 = "All that " + verb1 + " is " + noun2 + "\n"
line3 = "And she's " + verb2 + " a stairway to " + noun3 + "\n"
line4 = "When she gets there she " + verb3 + "\n"
line5 = "If the stores are all " + adjective1 + "\n"
line6 = "With a " + noun4 + " she can get what she came for\n"
line7 = "Oh oh oh oh and she's buying a stairway to " + noun5 + "\n"

list_of_lines = [line1, line2, line3, line4, line5, line6, line7]
for i in list_of_lines:
        new__completed_story.writelines(i)

new__completed_story.close()
finished_story = open("" + str(current_date) + "_story.txt", 'r')
print(finished_story.read())