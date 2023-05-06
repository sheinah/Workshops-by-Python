#Example
#name = input('Waht\'s your name?')
#if name == 'Michael':
#	print("OH, I LOVE YOU " + name)
#else:
#	print("I DO NOT LOVE YOU.")

###############################

# e.g. "What is your age?"    50
# PROGRAM ANSWERS:
# Hello, I am 24 years old.  You are 26 years older than me.

# e.g. "What is your age?"    12
# PROGRAM ANSWERS:
# Hello, I am 24 years old.  You are 12 years younger than me.


# Ask someone their age
age = int(input('What\'s your age? :'))
a1 = int(input("And...How old are you? :"))

# Then say that Sheenah's age is 24
print('Sheenah\'s age is', age)


# Then tell them how much younger or older they are than you.
if age == 24:
	print("I am", a1, "years old.")
else:
	print("I am", a1, "years old.")

if a1 == 24:
	print("you are same age as me")
elif a1 > 24:
	print("You are", int(a1-24), "years younger than me.")
elif a1 < 24:
	print("you are", int(24-a1), "years older than me.")
else:
	print('')

if a1 ==100:
	print('you are toooo old!')