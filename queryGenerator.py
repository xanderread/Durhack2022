"""

This program takes a string which is roughly a paragraph in length.

It returns three arguments, 
    - an array of keywords
    - a theme or NONE
    - a sound or NONE

"""

from rake_nltk import Rake
import spacy
from nrclex import NRCLex
nlp = spacy.load("en_core_web_sm")


#text = "Nearly ten years had passed since the Dursleys had woken up to find their nephew on the front step, but Privet Drive had hardly changed at all. The sun rose on the same tidy front gardens and lit up the brass number four on the Dursleys' front door; it crept into their living room, which was almost exactly the same as it had been on the night when Mr. Dursley had seen that fateful news report about the owls"

# this function finds the keywords
def extractKeywords(text):

    rake_nltk_var = Rake()
    rake_nltk_var.extract_keywords_from_text(text)
    keyword_extracted = rake_nltk_var.get_ranked_phrases()
    correctPhrases = []
    for phrase in keyword_extracted:
        flag = False
        for token in nlp(phrase):
            if(token.pos_ == "NOUN" or token.pos_=="ADJ"):
                flag=True
                break
            elif(token.pos_ == "NUM" or token.pos_ == "VERB"):
                flag=False
        if(flag and (phrase not in correctPhrases)):
            correctPhrases.append(phrase)
    sorted_list = list(sorted(correctPhrases, key = len))
    return sorted_list[:7]

# this function generates a theme
def getSentiment(text):
    text_object = NRCLex(text)
    data = text_object.raw_emotion_scores
    max = 0
    maxEmotion = ""
    for keys in data:
        if(data[keys]>max and (keys != "positive" and keys != "negative")):
            maxEmotion = keys
    return maxEmotion

# this function finds the first sound and returns it

def searchSounds(text):
    if "birds" in text:
        return "birds.mp3"
    elif "rain" in text:
        return "rain.mp3"
    return ""

# this function calls them all and returns the input
def queryGenerator(text):
    soundLink = searchSounds(text)
    keywords = ', '.join(extractKeywords(text))
    sentiment = getSentiment(text)
    keywords = keywords + ', '+sentiment
    return keywords,soundLink

#extractKeywords(text)