from sys import argv

script, user_name, last_name = argv
prompt = '-> '

print "Hi %s %s, I'm the %s script." % (user_name, last_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s %s?" % (user_name, last_name)
likes = raw_input(prompt)

print "Where do you like %s %s?" % (user_name, last_name)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %s about liking me.
You live in %s. Not sure where that is.
And you have a %s computer. Nice.
""" % (likes, lives, computer)
