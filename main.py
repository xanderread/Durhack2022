from makeImage import *
from queryGenerator import *
#from speechtotext import *

#This function should be called by joel's back end
text = "he house stood on a slight rise just on the edge of the village. It stood on its own and looked out over a broad spread of West Country farmland. Not a remarkable house by any means—it was about thirty years old, squattish, squarish, made of brick, and had four windows set in the front of a size and proportion which more or less exactly failed to please the eye."
def main(inputText, style):
    #params = audio,style
    prompt,soundLink = queryGenerator(inputText) #Awaiting next push
    prompt += ", "+style
    #sounds can be returned as an array of URLs for sounds
    imageURL=makeImage(prompt)
    print(imageURL)
    #Should then be returned to alex's flask function
    return imageURL,soundLink