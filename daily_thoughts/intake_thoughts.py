# - - - context  - - -
# prompt for daily thought
# daily thought includes date and string
# append to a text file or .csv

# - - - import datetime module and date method - - - 
from datetime import date

# - - - bind empty list to variable  - - -
thoughts = list()

# - - - input a thought - - -
def input_thought():
	print("\n- - - ready for input - - -\n")
	try:
		input_thought = str(input("enter your thought for today: "))
	except ValueError:
		print("ok, this is not valid syntax. please type a string/phrase/words.")
	# --- return statement ---
	print("\n- - - input received - - -\n")
	return input_thought

# - - - collect thoughts - - -
def collect_thought():
	thoughts.append({ "date": date.today(), "thought":input_thought() })
	return thoughts

# - - - print entered thoughts - - - 
def print_thoughts(thoughts):
	print("\n", "- - - entries - - -", "\n")
	for index,  element in enumerate(thoughts):
		print(f"{index}\t{element['date']}\t{element['thought']}")
	print("\n- - - end of entries - - -", "\n")

# - - - prompt to contine entering thoughts - - -
def prompt_to_continue():
	status = str(input("would you like to continue? type y or n for [yes/no]: "))
	status = status.lower()
	return status

# - - - write content to file ---
def write_to_file(file_name, data):
	file = open("thought_log.txt", "a")
	print(f"- - - {file_name} opened - - -")
	file.write(data)
	print(f"- - - done writing to {file_name} - - -")

# - - - on run / export - - - 
if __name__ == "__main__":
	destination_file = "thought_log.txt"
	entering_thoughts = True
	# - - - begin loop - - -
	while entering_thoughts is True:
		collect_thought()
		if prompt_to_continue() == "n":
			print("\n- - - completed collecting thoughts - - -\n")
			entering_thoughts = False
			if len(thoughts) == 0:
				print(f"no thoughts have been entered.")
			else:
				print_thoughts(thoughts)		
		else:
			continue
	# - - - loop exited - - -
	for thought in thoughts:
		write_to_file(destination_file, f"{thought['date']}\t{thought['thought']}\n")



