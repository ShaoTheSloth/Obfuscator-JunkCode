import re, random, string
from typing import List
from io import StringIO


def open_file(file_name: str) -> List[str]:
	# Read contents of a file and return contents to list
	with open(file_name, "r", encoding="utf-8") as file:
		return list(filter(None,(line.rstrip() for line in file)))


def get_nop_list() -> List[str]:
	# Return a list of valid op codes
	return open_file("valid_op.txt")

def rand_string(length: int) -> str:
	# Return a random string of ascii letters of length specified by parameter
	return "".join(random.choices(string.ascii_letters, k=length))

class Junkcode():
	def __init__(self, filename):
		self.filename = filename

		# Read Smali file
		with open(self.filename, "r") as f:
			self.content = f.read()
		

	def nopcode(self):
		# Get list of op codes that can get nop instructions
		# You can technically swap nop codes for other junk codes that do absolutely nothing
		op_codes = get_nop_list()

		pattern = re.compile(r"\s+(?P<op_code>\S+)")

		# Begin writing new file with the junk nop codes
		s = StringIO(self.content)

		# File name should be changed in the future
		with open("nop.smali", "w") as newfile:

			# Loop through each line
			for line in s:
				# Write original line to new file unless match the pattern
				newfile.write(line)
				match = pattern.match(line)

				# If match, add in random number of nop codes from 1 to 5
				if match:
					op_code = match.group("op_code")
					if op_code in op_codes:
						rand_nop = random.randint(1,5)
						newfile.write("\tnop\n" * rand_nop)

	def junkbranch(self):
		# Set some flags
		edit_flag = False
		start_label = None
		end_label = None

		# Begin writing new file with the junk branch
		s = StringIO(self.content)

		# File name should be changed in the future
		with open("branch.smali", "w") as newfile:

			# Loop through each line
			for line in s:
				# If the line is the start of a function,
				if (line.startswith(".method") and " native" not in line and " abstract" not in line and not edit_flag):
					newfile.write(line)
					# Then set edit flag to true, in preparation for end of function
					edit_flag = True

				# If the line is the end of a function
				elif line.startswith(".end method") and edit_flag:
					# Add in junk code
					if start_label and end_label:
						newfile.write("\t:{0}\n".format(end_label))
						newfile.write("\tgoto/32 :{0}\n".format(start_label))
						start_label = None
						end_label = None
					newfile.write(line)
					# Then set the edit flag back to false
					edit_flag = False

				# If the edit flag is just true
				elif edit_flag:
					newfile.write(line)
					pattern = re.compile(r"\s+\.locals\s(?P<local_count>\d+)")
					match = pattern.match(line)

					# And there are 2 registers available, add a junk branch to the beginning of the method
					if match and int(match.group("local_count")) >= 2:
						v0 = random.randint(1,32)
						v1 = random.randint(1,32)
						start_label = rand_string(16)
						end_label = rand_string (16)
						temp_label = rand_string(16)
						newfile.write("\n\tconst v0, {0}\n".format(v0))
						newfile.write("\tconst v1, {0}\n".format(v1))
						newfile.write("\tadd-int v0, v0, v1\n")
						newfile.write("\trem-int v0, v0, v1\n")
						newfile.write("\tif-gtz v0, :{0}\n".format(temp_label))
						newfile.write("\tgoto/32 :{0}\n".format(end_label))
						newfile.write("\t:{0}\n".format(temp_label))
						newfile.write("\t:{0}\n".format(start_label))

				else:
					# Else just continue writing the original line
					newfile.write(line)




def main():
	a = Junkcode("MainActivity.smali")
	a.junkbranch()
	a.nopcode()

if __name__ == '__main__':
	main()
