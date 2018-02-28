import json
import markovify

class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = [w for w in words if len(w) > 0]
        words = ["::".join(tag) for tag in nltk.pos_tag(words)]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

with open('cyber.json') as c:
    text_model = POSifiedText.from_json(json.load(c))

for i in range(10000):
    with open('cyber_snippets', 'a') as o:
        o.write(text_model.make_sentence()+'\n')

