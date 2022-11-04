# REQUIRED IMPORTS:
import json
import random
import os

# GET(): SELECTS A RANDOM OBJECT FROM THE JSON DATABASE USING A RANDOM TYPE (HAVING A 5% CHANCE OF GETTING A JOKE, 95% CHANCE OF GETTING A QUOTE). PARSES IT. IF IT'S A QUOTE FORMATS IT IN A 'QUOTE (AUTHOR)' STYLE (IF THE AUTHOR IS NULL IT DOESN'T GET PRINTED); IF IT'S A JOKE, FORMATS IT IN A 'SETUP PUNCHLINE' STYLE. THEN PRINTS IT.
def GET():
    # OPENS THE JSON DATABASE AT PATH '/DATABASE.json' IF IT'S RUNNING ON DOCKER.
    if os.path.exists('/DATABASE.json'):
        with open('/DATABASE.json', 'r') as DATA:
            DATABASE = json.load(DATA)
    # OPENS THE JSON DATABASE AT PATH 'DATABASE.json' IF IT'S RUNNING LOCALLY.
    else:
        with open('DATABASE.json', 'r') as DATA:
            DATABASE = json.load(DATA)
    # GETTING A RANDOM TYPE (HAVING A 5% CHANCE OF GETTING A JOKE, 95% CHANCE OF GETTING A QUOTE):
    TYPE = 'JOKE' if random.randint(0, 100) <= 5 else 'QUOTE'
    # GETTING A RANDOM OBJECT:
    OBJECT = random.choice(DATABASE[TYPE])
    # PARSING THE OBJECT AND FORMATTING IT:
    if TYPE == 'QUOTE':
        # IF IT'S A QUOTE:
        if OBJECT.keys().__contains__('AUTHOR'):
            # IF THE AUTHOR IS NOT NULL:
            print(f'{OBJECT["QUOTE"]} ({OBJECT["AUTHOR"]})')
        else:
            # IF THE AUTHOR IS NULL:
            print(f'{OBJECT["QUOTE"]}')
    else:
        # IF IT'S A JOKE:
        print(f'{OBJECT["SETUP"]} {OBJECT["PUNCHLINE"]}')

# MAIN(): CALLS GET() AND PRINTS THE RESULTS.
if __name__ == "__main__":
    # RUNS THE GET() FUNCTION AND PRINTS THE RESULTS.
    GET()