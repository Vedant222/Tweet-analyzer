import re

def calculate_profanity(tweet, slurs):
    words = tweet.lower().split()
    num_slurs = 0
    for word in words:
        if word in slurs:
            num_slurs += 1
    
    degree_of_profanity = (num_slurs / len(words)) * 100
    
    return degree_of_profanity

def main():
    with open('tweets.txt', 'r') as f:
        tweets = f.read().splitlines()
        
    slurs = {'slur1', 'slur2', 'slur3'}
    
    for tweet in tweets:
        degree_of_profanity = calculate_profanity(tweet, slurs)
        print(f'{tweet}: {degree_of_profanity}%')

if __name__ == '__main__':
    main()
