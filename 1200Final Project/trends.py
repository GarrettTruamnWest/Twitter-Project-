import sys
from state import load_states
from country import Country
from parse import load_sentiments, load_tweets
from colors import get_sentiment_color

if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
else:
    query = raw_input('Enter query: ')

sentiments = load_sentiments()    # a map from strings to float in (-1.0, +1.0) range
states = load_states()            # list of State instances
tweets = load_tweets(query)       # list of Tweet instances
usa = Country(states, 1200)       # graphical rendering of Country (feel free to change the width)

#------------ your code should follow ------------
