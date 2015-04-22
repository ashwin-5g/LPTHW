from sys import exit

def gold_room():
	print "This room is full of gold.  How much do you take?"
  
	choice = int(raw_input("> "))
	if choice < 0:
		dead("Man, learn to type a number.")
	elif 0 <= choice < 50:
		print "Nice, you're not greedy. You win!"
		exit(0)
	else:
		dead("You greedy bastard!")
		   
i = 0 
while (i < 8):
	gold_room()
	i = i + 1

