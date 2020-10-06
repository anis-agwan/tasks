# Task 6

# Write the Task 5 titles to the text file.

# Extras:
# Ask the user to specify the name of the output file that will be saved.
from task_5 import scrape_url, result

file_name = input('What would you like to name the file? ')

with open(file_name+'.txt', 'a') as f:
    for title in result:
        f.write('\n'+title)