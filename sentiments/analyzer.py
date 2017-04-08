import time

import nltk 
from nltk.tokenize import TweetTokenizer


class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        
        start_time = time.time()
        # initializes sets for positve and negative words
        self.positive, self.negative = set(), set()
        
        # loads positive words and closes file
        with open(positives) as lines:
            for line in (line for line in lines if not line.startswith(";")):
                self.positive.add(line.strip())
                    
        # loads negative words and closes file
        with open(negatives) as lines:
            for line in (line for line in lines if not line.startswith(";")):
                    self.negative.add(line.strip())
        
        end_time = time.time()
        total_time = end_time - start_time
        print("Words Parsed/Imported, Positive: ", len(self.positive))
        print("Words Parsed/Imported, Negative: ", len(self.negative))
        print("Total run time: %.5s seconds." %total_time)
        
        rel_time = (143091 / (len(self.positive)+len(self.negative))*total_time)
        
        print("Time comparison: %.5s vs. .06 seconds" %rel_time)
                    
        

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        
        # defaults to neutral sentiment
        total = 0
        
        # sets up tokenized list of text
        tkn = TweetTokenizer()
        token = tkn.tokenize(text)
        
        # checks sentiment of each word and adjusts score accordingly
        for word in token:
            if word in self.positive:
                total += 1
            if word in self.negative:
                total -= 1
        
        return total
        
Analyzer("positive-words.txt", "negative-words.txt")