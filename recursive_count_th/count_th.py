'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# Given 1 string of word, the task is to count the number of times "th" occurs in `word` using recursion.
# Suppose the problem has n parts, divide the problem in such a way that considers n-1 parts already done after which the operation to be performed is limited to only one part. 
# Thereby, dividing the recursion approach into two cases i.e. base case and the recursive case. 
# Recursive fn for counting number of "th" occur within a string of `word` with "th"
def count_th(word):
    # set the variable count to 0 to keep track
    count = 0
    
    # if length of the `word` only has 1 or less letter, it can't have "th" in it
    if len(word) <= 1:
        return count
    
    # if the word has a "t" and is followed by an "h", add it to the count
    elif word[0] == 't' and word[1] == 'h':
        count += 1
        
    # use recursion to check adjacent letters
    # remove the first position and check the next until they match
    return count + count_th(word[1: ])

# Driver code
if __name__ == '__main__':
    
    word = ""
    count = count_th(word)
    print(count_th(word))
    
    word = "thank you"
    count = count_th(word)
    print(count_th(word))
    
    word = "thank you but no thank you"
    count = count_th(word)
    print(count_th(word))
    
    
