"""Word Count Function
Select Files to run 
Create and Empty dictionary
Iterate(Loop) through the file 
    use line split rstrip() f(x) to seperate data
    Iterate over each word in line 
    
    use line split rstrip() f(x) to seperate data
    Iterate over each word in line 
    Check if the word is already there 
    Count words by 1
    add to the dictionary 
print or call function"""

def word_count():

    input_file = open("twain.txt")
    wordcount_dict = {}

    for line in input_file:
        line = line.rstrip()
        words = line.split (" ")

        for word in words:
            if word in wordcount_dict:
                wordcount_dict[word] = wordcount_dict[word] + 1
            else:
                wordcount_dict[word] = 1
    for key in list(wordcount_dict.keys()):
        print(key, wordcount_dict[key])

word_count()