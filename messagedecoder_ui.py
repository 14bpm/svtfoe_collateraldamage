#defining coded texts
#tb stands for Timothy Bonner, all texts start with tb
#TEXT means string (BY CHARACTERS)
#LIST means list (BY WORDS)
tbTEXT_JUSTLETTERS = 'DearestRebeccaIHatethepossumsIhatethepossumssomuchMyrageforthemisallIcanthinkaboutTheyscratchandbitelikethedemonsinfairytalesIcannolongerloveyouIcanonlyhatethepossumsSincerelyTimothyBonner'
tbTEXT_NOSPACE = 'DearestRebecca,IHatethepossums.Ihatethepossumssomuch.MyrageforthemisallIcanthinkabout.Theyscratchandbitelikethedemonsinfairytales.Icannolongerloveyou.Icanonlyhate......thepossums.Sincerely,TimothyBonner'
tbTEXT_NOCAPS = 'earestebeccaatethepossumshatethepossumssomuchyrageforthemisallcanthinkaboutheyscratchandbitelikethedemonsinfairytalescannolongerloveyoucanonlyhatethepossumsincerelyimothyonner'
tbTEXT_ONLYCAPS = 'DRIHIMITIISTB'
tbTEXT_FULLTEXT = '''
Dearest Rebecca,

I Hate the possums.
I hate the possums so much.
My rage for them is all
I can think about.
They scratch and bite like the
demons in fairy tales.
I can no longer love you.
I can only hate...

...the possums.

Sincerely,
Timothy Bonner
'''
tbLIST_ALLWORDS = ['Dearest', 'Rebecca', 'I', 'Hate', 'the', 'possums', 'I', 'hate', 'the', 'possums', 'so', 'much', 'My', 'rage', 'for', 'them', 'is', 'all', 'I', 'can', 'think', 'about', 'They', 'scratch', 'and', 'bite', 'like', 'the', 'demons', 'in', 'fairy', 'tales', 'I', 'can', 'no', 'longer', 'love', 'you', 'I', 'can', 'only', 'hate', 'the', 'possums', 'Sincerely', 'Timothy', 'Bonner']
tbLIST_ONEHATE = ['Dearest', 'Rebecca', 'I', 'Hate', 'the', 'possums', 'I', 'the', 'possums', 'so', 'much', 'My', 'rage', 'for', 'them', 'is', 'all', 'I', 'can', 'think', 'about', 'They', 'scratch', 'and', 'bite', 'like', 'the', 'demons', 'in', 'fairy', 'tales', 'I', 'can', 'no', 'longer', 'love', 'you', 'I', 'can', 'only', 'the', 'possums', 'Sincerely', 'Timothy', 'Bonner']
tbLIST_NOHATE = ['Dearest', 'Rebecca', 'I', 'the', 'possums', 'I', 'the', 'possums', 'so', 'much', 'My', 'rage', 'for', 'them', 'is', 'all', 'I', 'can', 'think', 'about', 'They', 'scratch', 'and', 'bite', 'like', 'the', 'demons', 'in', 'fairy', 'tales', 'I', 'can', 'no', 'longer', 'love', 'you', 'I', 'can', 'only', 'the', 'possums', 'Sincerely', 'Timothy', 'Bonner']
tbLIST_NOPOSSUMS = ['Dearest', 'Rebecca', 'I', 'Hate', 'the', 'I', 'hate', 'the', 'so', 'much', 'My', 'rage', 'for', 'them', 'is', 'all', 'I', 'can', 'think', 'about', 'They', 'scratch', 'and', 'bite', 'like', 'the', 'demons', 'in', 'fairy', 'tales', 'I', 'can', 'no', 'longer', 'love', 'you', 'I', 'can', 'only', 'hate', 'the', 'Sincerely', 'Timothy', 'Bonner']
tbLIST_NOI = ['Dearest', 'Rebecca', 'Hate', 'the', 'possums', 'hate', 'the', 'possums', 'so', 'much', 'My', 'rage', 'for', 'them', 'is', 'all', 'can', 'think', 'about', 'They', 'scratch', 'and', 'bite', 'like', 'the', 'demons', 'in', 'fairy', 'tales', 'can', 'no', 'longer', 'love', 'you', 'can', 'only', 'hate', 'the', 'possums', 'Sincerely', 'Timothy', 'Bonner']
tbLIST_NOCAPS = ['the', 'possums', 'hate', 'the', 'possums', 'so', 'much', 'rage', 'for', 'them', 'is', 'all', 'can', 'think', 'about', 'They', 'scratch', 'and', 'bite', 'like', 'the', 'demons', 'in', 'fairy', 'tales', 'can', 'no', 'longer', 'love', 'you', 'can', 'only', 'hate', 'the', 'possums']

#text = select which text to slice
#sliced = specify data type
#this part of the code is antequated but whatever. like you could delete this block and nothing would happen
text = tbTEXT_JUSTLETTERS
length = len(text)
sliced = ''

#big loop go round
loop = 'OH YEAH BABY'
while loop:
    #select text, assign variable to slice
    validchoice = 0
    while not validchoice == 1:
        print('Welcome to the secret message slicer\n\n')
        text_choice = input(
            '''
How do you wish to slice?
1 - with formatting | BY CHARACTERS
2 - without spaces or line breaks | BY CHARACTERS
3 - letters only | BY CHARACTERS
4 - words only | BY WORDS
5 - words only sans lowercase "hate" | BY WORDS
6 - words only sans both "Hate" and "hate" | BY WORDS
7 - words only sans "possums" | BY WORDS
8 - words only sans "I" | BY WORDS

''')
        text_choice = int(text_choice)
        if text_choice == 1:
            text = tbTEXT_FULLTEXT
            length = len(text)
            sliced = ''
            choicetype = 'string'
            validchoice = 1
        elif text_choice == 2:
            text = tbTEXT_NOSPACE
            length = len(text)
            sliced = ''
            choicetype = 'string'
            validchoice = 1
        elif text_choice == 3:
            text = tbTEXT_JUSTLETTERS
            length = len(text)
            sliced = ''
            choicetype = 'string'
            validchoice = 1
        elif text_choice == 4:
            text = tbLIST_ALLWORDS
            length = len(text)
            sliced = []
            choicetype = 'list'
            validchoice = 1
        elif text_choice == 5:
            text = tbLIST_ONEHATE
            length = len(text)
            choicetype = 'list'
            sliced = []
            validchoice = 1
        elif text_choice == 6:
            text = tbLIST_NOHATE
            length = len(text)
            choicetype = 'list'
            sliced = []
            validchoice = 1
        elif text_choice == 7:
            text = tbLIST_NOPOSSUMS
            length = len(text)
            choicetype = 'list'
            sliced = []
            validchoice = 1
        elif text_choice == 8:
            text = tbLIST_NOI
            length = len(text)
            choicetype = 'list'
            sliced = []
            validchoice = 1
        else:
            print('\aInvalid choice. Pick again.\n')
    
    
    slice_num = input('\n\nSlice by? (Enter a counting number or this shit gonna crash.)\n\n')
    slice_num = int(slice_num)
    position = slice_num
    position -= 1
    
    while position <= length:
        positionn = position
        positionn += 1
        sliced += text[position:positionn]
        position += slice_num
    
    if choicetype == 'string':
        print('\n\nHere is your original text:\n' + text)
        print('\n\nAnd here is the sliced secret message:\n' + sliced)
    elif choicetype == 'list':
        print('\n\nHere is your original text:', text)
        print('\n\nAnd here is the sliced secret message:', sliced)
    choice = None
    while choice != 'N' and choice != 'Y':
        choice = input('\n\nSlice again (Y/N)?: ')
        choice = choice.upper()
        if choice == 'Y':
            print('\nYou\'re one dedicated code-breaker!', end='\n\n')
        elif choice == 'N':
            print('\nUntil next time!')
            loop = None #exit big loop
        else:
            print('\n\aInvalid choice!')

input('\n\nPress the enter key to exit.')
