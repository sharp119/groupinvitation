import random
import sys
import jsons


# Parse the JSON data from the file
with open('groups.json', encoding="utf-8") as json_file:
	data = jsons.loads(json_file.read())

# Select a random group
group = random.choice(data['groups'])

# Check if the group link was passed as a command-line argument
if len(sys.argv) > 1:
	# Use the provided link
	group_link = sys.argv[1]
else:
	# Prompt the user for the link
	group_link = input('Enter the group link: ')

# Generate the WhatsApp message
message = f"Join the {group['name']}\n\n{group['description']}\nLink: {group_link}"

# Print the message
print(message)
