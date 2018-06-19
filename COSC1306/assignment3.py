"""
Program #3: Detecting Trends and Foul Language in Twitter
COSC 1306, Spring 2016
This program detects foul language and trendy topics in a
sample of Twitter data
"""

"""
Opens the relevant text files for reading and creates/overwrites the text file for the potentially offensive tweets
and top hashtags.
"""
tweets = open('twitter_data.txt', 'r', encoding="utf8")            # Gives encoding error if encoding isn't set
swear = open('swear_words.txt', 'r', encoding="utf8")
potential = open('potentially_offensive_tweets.txt', 'w')
top = open('top_hashtags.txt', 'w')

"""
Assigns variable tweet_line to first line of twitter_data.txt since it would use too much memory
if it made a list of strings from each line. Also creates a list of swear words from the
swear_words.txt file.
"""
tweet_line = tweets.readline()
swear_list = swear.readlines()

"""
Detecting Foul Language in Twitter
"""
# While loop that iterates through each line of the twitter_data.txt file
while tweet_line:
    # For loop that iterates through each word in swear_words.txt file
    for i in swear_list:
        # Strips newline character and checks if the line has a swear word
        if i.strip() in tweet_line:
            # Writes the line to the potentially_offensive_tweets.txt file if it has a swear word
            potential.write(tweet_line)
    # Goes to next line in the twitter_data.txt file
    tweet_line = tweets.readline()

# Outputs a statement notifying user that the file is generated
print("Twitter data processed. "
      "Please check potentially_offensive_tweets.txt for the tweets that contained swear words.")

# Closes the open files
tweets.close()
swear.close()
potential.close()

"""
Detecting Topic Trends in Twitter
"""

# Reopen twitter_data.txt to start at the top for readline
tweets = open('twitter_data.txt', 'r', encoding="utf8")

# Assigns tweet_line to the first line of twitter_data.txt
tweet_line = tweets.readline()

# Creating an empty dictionary
hashtags = {}

# While loop that iterates through each line of the twitter_data.txt file
while tweet_line:
    # Splits the string into a list of strings
    words = tweet_line.split()
    # Iterates through every string in the list of words
    for i in words:
        # Checks if hashtag is first character in each string
        if '#' in i[0]:
            # Makes entire hashtag lowercase and checks if it is contained in the dictionary or not
            # Assigns the hashtag a value of one if it is not contained in the dictionary
            if i.lower() not in hashtags:
                hashtags[i] = 1
            # Adds 1 to the value of the hashtag if it is in the dictionary
            else:
                hashtags[i.lower()] = hashtags[i.lower()] + 1
    # Goes to next line in twitter_data.txt
    tweet_line = tweets.readline()

# Creates a list from the hashtags
hashtag_list = list(hashtags.items())

# Sorts the list of hashtags in descending order
for i in range(len(hashtag_list)):
    for j in range(len(hashtag_list)):
        if hashtag_list[i][1] > hashtag_list[j][1]:
            temp = hashtag_list[i]
            hashtag_list[i] = hashtag_list[j]
            hashtag_list[j] = temp

# Asks user for number of top hashtags they want and writes it to the top_hashtags.txt file
N = int(input("Number of top hashtags: "))
for i in range(N):
    top.write(str(hashtag_list[i]) + "\n")

# Outputs a statement notifying user that the file is generated
print("Top", N, "hashtags calculated. Please check top_hashtags.txt for the hashtags and number of occurrences.")

# Closes files when done
top.close()