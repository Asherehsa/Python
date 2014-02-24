user_name = "Asher"
prompt = '> '

print "I'd like to ask you a few questions."

print "Do you like me %s?" %user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What is your favorite color?"
color = raw_input(prompt)

print """
Alright, so you said %r about liking me.
you live in %r. Not sure where that is.
And you like %r. Nice.
""" % (likes, lives, color)
