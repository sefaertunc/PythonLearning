import re

# Define the file paths
input_file_path = 'word_list.txt'  # Update this with your input file path
output_file_path = 'cleaned_word_list.txt'  # Update this with your desired output file path

# Words to put in brackets
words_to_bracket = {'noun', 'adjective', 'adverb', 'verb', 'preposition', 'conjunction'}

# Open the input file, process the lines, and write to the output file
try:
	with open(input_file_path, 'r', encoding='utf-8') as infile:
		lines = infile.readlines()

	cleaned_lines = []
	for line in lines:
		# Remove the number at the beginning and C2 (or similar tags) at the end
		cleaned_line = ' '.join(line.split(' ')[1:]).strip()
		cleaned_line = ' '.join(cleaned_line.split()[:-1]).strip()


		# Use regex to find and bracket words (with or without punctuation attached)
		def bracket_word(match):
			word = match.group(1)  # Extract the word without punctuation
			return f"[{word}]{match.group(2)}"  # Reconstruct with brackets and punctuation


		# Regex pattern to match target words with optional punctuation
		pattern = r'\b(' + '|'.join(words_to_bracket) + r')\b([,;.]?)'
		cleaned_line = re.sub(pattern, bracket_word, cleaned_line)

		# Add a comma at the end of each cleaned line
		cleaned_lines.append(f'"{cleaned_line}",')

	# Write the cleaned lines to the output file
	with open(output_file_path, 'w', encoding='utf-8') as outfile:
		outfile.write('\n'.join(cleaned_lines))

	print(f"File processed successfully! Cleaned data saved to {output_file_path}")
except FileNotFoundError:
	print(f"Error: The file {input_file_path} does not exist.")
except Exception as e:
	print(f"An error occurred: {e}")
