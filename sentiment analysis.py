import string

from collections import Counter

import matplotlib.pyplot as plt

#opening the txt file
text=open('read.txt',encoding="utf-8").read()

#encode to make word difference in samaller case
lower_case=text.lower()

# removing punctuations
cleaned_text=lower_case.translate(str.maketrans('', '', string.punctuation))

# we are breaking sentences to small words
tokenized_words=cleaned_text.split()

# here we are removing words from the input list and then we are simply
# seperating the simple words with no meaning and removing them as they are of no use.
# creating a list for other words as well
# we are doing this to save time

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words=[]
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)



emotion_list=[]

#opening the file emotionns.txt and looping through each line and clear it
#extracting the word and emotions using split

with open('emotions.txt','r') as file:
    for line in file:
#replacing extra line and extra space behind by strip and removing quotation marks
        clear_line=line.replace('\n','').replace(',','').replace("'",'').strip()
        word, emotion = clear_line.split(':')
# here we are simply taking the words  of emotion and making them to a new list
        if word in final_words:
            emotion_list.append(emotion)


#here we are using counter function to count the number of emotions.
print(emotion_list)
w = Counter(emotion_list)
print(w)

# creating the bar graph from the counter values
fig, ax1 = plt.subplots()
 # adjusting x axis for seeing words clearly
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.show()


