def main():
    text = input("Please enter a string: ")
    word = input("Please enter a word: ")
    dist = calcDistribution(text, word)
    print(f"'{word}' makes up {dist}% of the words in '{text}'") # output results of distribution

def calcDistribution(text, word):
    ''' Calculates the percentage of how many times word appears in text
        Percentage = number of times word appears / total amount of words

        Input: "cat cat cat dog", "dog"
        Output: 25.0 (Since it is 25%)

        Input: "tomato tomatoes tomato", "tomato"
        Output: 66.66666666666666
    '''
    counts, total = wordCounter(text) # extract data from other functions
    if word not in counts: # account for special case when word appears 0 times in text
        dist = 0
    else: # return the final percentage (Ex. 25 for 25%, 17.7 for 17.7%)
        dist = counts[word] / total * 100
    return dist

def stringToWords(text):
    ''' Splits text into a list of tokens using whitespace '''
    token_lst = text.split()
    return token_lst

def wordCounter(text):
    ''' Counts the number of words in text
        Returns a list containing two elements:
            a dictionary of words and their frequencies
            the total amount of words

        Input: "cat cat cat dog"
        Output: [ {("cat" : 3), ("dog" : 1)}, 4 ]
    '''
    # Format raw string into a list of words
    token_lst = stringToWords(text)

    # Calculate frequency of each word and total word count
    total = len(token_lst)
    counts = {}
    for word in token_lst: # iterating over each item in token_lst
        if word not in counts: # testing for existence of word key in counts
            word_count = token_lst.count(word)  # count number of times word occurs in token_lst
            counts[word] = word_count # create key-value pair for word and word_count
    return [counts, total]

if __name__ == '__main__':
    main()