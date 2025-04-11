import os
import re

file_path = "/AI_Policy_deepseek/"
myStates = ['NY', 'CA', 'SD', 'AZ', 'WA', 'FL', 'TX']
fileName = "_AI_Policy_deepseek.md"

patterns = [r'### \*\*\d+\. \w+\*\*\n\w+', r'\n---\n', r'\]\n\n---\n\n']

match_locs = {}
cur_file = myStates[0]+fileName
with open(cur_file, 'r') as file:
	content = file.read()
	for p in patterns:
		matches = list(re.finditer(p, content))
		if matches:
			match_locs[p] = [match.start() for match in matches]

print(f"matchs found \n{match_locs}")

