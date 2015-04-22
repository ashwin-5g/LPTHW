from sys import argv 

script, filename = argv

txt = open(filename)

print "Here's your file: %s" % filename
print txt.read()

file_again = raw_input("File to be opened: ")

txt_again = open(file_again)

print txt_again.readline()

file_t = raw_input("File to be truncated: ")

trunc_file = open(file_t, 'w')

trunc_file.truncate()

print "%s has been truncated" % file_t



