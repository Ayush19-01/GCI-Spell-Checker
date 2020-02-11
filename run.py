#Made for the sole purpose of GCI 2019\
from spellchecker import SpellChecker
spell = SpellChecker()
list2=[]
s=""
list4=[]
list1=['question','which','pronunciation','preferred','steering','choice',
            'dictionary','wavelength','expensive','magnificent','actually','computer',
            'blistering','against','moment','curiosity','believable','frontier',
            'machine','violence']
print("Paragraph must include wrong spellings of:")
print(list1)
x=input("Enter a paragraph:")
z=x.split(" ")
a=spell.unknown(z)
cv=0
for word in a:
    list2.append(spell.correction(word))
    list4.append(word)
for i in range(len(list4)):
    l=z.index(list4[i])
    if list2[i] in list1:
        z[l]=list2[i]
        cv+=1
for j in z:
    s+=j
    s+=" "
print("Corrected Paragraph:")
print(s)
#I had a queston , that whoch of the pronounciation is preffered in steeering the choce , the words incleded in dicktionary , difficult words such as weelength expesive and magnyficent acktualy have a bad effect on the computar engineering , blistring and aginst the mement of curiocity which is indeed belieavable and fronteer mashine under violense of act
print("Number of words corrected:",cv)
