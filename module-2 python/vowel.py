l = input("Input a letter of the alphabet: ")
2	
3	if l in ('a', 'e', 'i', 'o', 'u'):
4	    print("%s is a vowel." % l)
5	elif l == 'y':
6	    print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
7	else:
8	    print("%s is a consonant." % l)