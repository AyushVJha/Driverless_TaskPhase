my_string= ''' Hello People, This is Ayush Jha
          I am a taskphase member of driverless subsytem in The Formula Manipal.
          This is our first Python task.
          It was a pleasure meeting You
          Thank You :) '''
# The String is defined above          
          

def word_occurence(str): # function named word_occurence of string data type
    occurence = dict() # dictionary defined
    words = str.split() # This splits all the words of a string to a list

    for word in words:
        if word in occurence:
            occurence[word] += 1
        else:
            occurence[word] = 1

    return occurence

print( word_occurence(my_string))
total_words= len(my_string.split())
print("Total number of words in the string are:" + str(total_words))


