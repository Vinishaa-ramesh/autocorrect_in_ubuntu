import nltk
from nltk.metrics.distance import edit_distance
from nltk.util import ngrams
import pandas
import subprocess
import sys

with open("/home/bharathi/command_list.txt") as f:
    content_list = [line.rstrip() for line in f]

correct_spellings = content_list
spellings_series = pandas.Series(correct_spellings)
spellings_series

#user_list = list(input('Enter command: ').split(" "))
user_list = sys.argv[1:]
command_new = []
c = ""

def editreco(x=user_list[0]):
    outcomes = ""
    distances = ((edit_distance(x, word), word)
                        for word in correct_spellings)
    closest = min(distances)
    outcomes = closest[1]
    return outcomes
if(user_list[0][0]=='c' and len(user_list[0])==2):
	c="cd"
else:
	c = editreco()
command_new.append(c)

for string in user_list:
	if string==user_list[0]:
		continue;
	else:
		c+=" " + string
		command_new.append(string)

#subprocess.run(command_new)

sys.exit(c)

