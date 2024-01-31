import json # jason derulo
import requests

url = "https://api.datamuse.com/words?ml=skiing"

req = requests.get(url)

print(req.text)

dct1 = json.loads(req.text)

print(dct1)

score_key = "score"
word_key = "word"

total_score = 0.0

for d in dct1:
    # print(d[word_key], d[score_key])
    if "snowboard" in d[word_key]:
        print(d[word_key], d[score_key])
        total_score += d[score_key]
        
print("all snowboards total score: ", total_score)
    
    
        
        
