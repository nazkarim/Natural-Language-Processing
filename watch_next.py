#Import module and english language model --------------------------
import spacy
nlp = spacy.load('en_core_web_md')

def reccomend_movie(description):
    description = nlp(description)  #convert description into spacy object
    #create empty variable for most similar description and highest similarity variable
    most_similar = ''               
    highest_similarity = 0
    #open the movies.txt file
    with open ("movies.txt", 'r') as f:
        for line in f:
            line = nlp(line)        #convert each line to spacy object
            similarity = description.similarity(line)   #get the similarity of the line compared to the description 
            if similarity > highest_similarity:
                highest_similarity = similarity         #assign similarity to highest similarity
                most_similar = line                     #save current line as most similar line

    print(most_similar)     #print out most similar description saved in 'most_similar'

#call function with descrition from Hulk movie
reccomend_movie("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.")