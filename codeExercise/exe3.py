pangram = "The quick Brown fox jumps over the lazy dog"


# This is an example method call.
#example_pangram = pangram.some_method_here()

# This needs to be all in uppercase.
shouty_pangram = pangram.upper()
#print(shouty_pangram)


# This needs to have the first 'T' of the pangram in uppercase, keep the rest the same.
first_only_pangram = pangram.capitalize()
#print(first_only_pangram)


# This needs to have the first letter of each word in uppercase.
all_words_pangram = pangram.title();
#print(all_words_pangram)


# This needs to be all in lowercase.
quiet_pangram = pangram.casefold();
#print(quiet_pangram)


# Break the sentence apart into a list of individual words.
list_of_pangram_words= ((pangram.split(" ")));
print(list_of_pangram_words)





