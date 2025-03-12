import os
import inquirer

def show_question(question, options):
    questions = [
        inquirer.List('response', message=question, choices=options)
    ]
    answer = inquirer.prompt(questions)
    return answer['response']


all_dirs = os.listdir('.')
only_modules = [i for i in all_dirs if '.' not in i]

res = show_question("Which module do you want to see?", only_modules)
res1 = show_question("...and now?", ['<-- Back']+os.listdir(res))
print(res1)






