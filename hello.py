
# Print test message
import emoji

###########################################################################################
# Variables
audience = 'People'
greeting = 'Hello '
message_for_all = f'''{greeting}{audience}! You are reading the first official python program I a have created! This text is actually 
written in lowercase but converted to \"upper\". I want for any feedback that you may have. Check out the source code
and you will see that I used replace, len, and find functions. Additionally, I utilized f-strings. I imported 
the emojis package and set \'use_aliases\' to \'true\' which gave me much more emojies to choose from. Tkinter
is giving me trouble even though it's already installed here on my Py 3.7.'''
message_for_all = message_for_all.replace('want','wish')
message_length = len(message_for_all)
first_letter = audience[0]
letter_count = message_for_all.count("a")
find_wish = message_for_all.find('wish')
name_count = len(audience)
###########################################################################################

print(message_for_all.upper()),print(emoji.emojize(':smirk:', use_aliases=True))


# Metrics to be added at bottom and repeated across future projects
print('##########################################################################')
print('Coding Metrics')
print('Name\'s first letter = ',first_letter)
print('Name length = ',name_count)
print('Message length = ',message_length)
print('Letter \"A\" Character count = ',letter_count)
print('The word \"wish\" is found',find_wish,'times?')
print('##########################################################################')
