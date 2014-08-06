#!/usr/bin/python
import re
# Specify which file to read
fname = "example2.java"

# Define a few regular expressions to match the code we don't want 
regexMultiLine = re.compile("/\*.*?\*/", re.DOTALL)
regexSingleLine = re.compile("//[^\n]*\n", re.MULTILINE)
regexWhiteSpace = re.compile("^ *\n", re.MULTILINE)

# Open our file for reading
ins = open( fname, "r" )
# Define a variable to hold our significant lines of code
codeLines = 0
# Read in all of the lines
with open(fname) as f:
	content = "".join(f.readlines())
# Add in another newline character at the end of our file
content += "\n"

# Strip out the lines that contain multiline comments
content = regexMultiLine.sub('', content)
# Strip out the lines that contain single comments
content = regexSingleLine.sub("\n", content)
# Strip out all lines that just contain whitespace
content = regexWhiteSpace.sub('', content)

# Print out our significant code to the screen
print content
# Count up the number of newlines remaining in the code
codeLines = content.count("\n")

# Let the user know what we found
print "We found", codeLines, "significant lines."
