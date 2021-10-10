# https://www.youtube.com/watch?v=s8XjEuplx_U&t=3245s
import spacy

nlp = spacy.load("en_core_web_sm")

text = ("Google was initially funded by an August 1998 investment of $100,000 from Andy Bechtolsheim, co-founder of Sun Microsystems, a few weeks prior to September 7, 1998, the day Google was officially incorporated. Google received money from three other angel investors in 1998: Amazon.com founder Jeff Bezos, Stanford University computer science professor David Cheriton, and entrepreneur Ram Shriram. Between these initial investors, friends, and family Google raised around $1,000,000, which is what allowed them to open up their original shop in Menlo Park, California.")

print ("text = " + text)

doc = nlp(text)

"""
print ('---------------\nTokens: ')
for token in doc:
    print(token)
print ('---------------')
"""

"""
print ('---------------\nNouns: ')
for token in doc:
    if token.pos_ == 'NOUN':
        print(token)
print ('---------------')
"""

"""
print ('---------------\nAdjectives: ')
for token in doc:
    if token.pos_ == 'ADJ':
        print(token)
print ('---------------')
"""

"""
print ('---------------\nEntities: ')
for entity in doc.ents:
    print(entity.text, entity.label_)
print ('---------------')
"""
