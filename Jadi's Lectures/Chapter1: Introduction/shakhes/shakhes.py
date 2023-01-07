def IndexText(text):
    Text = text.split('. ') # here we created a list so we can call ots items later.
    # print(Text) # a list of sentences.
    count = 1
    Count = 0
    for sent in Text:
        # print(sent)
        Word = sent.split()[1:]
        # print(Word) # a list of words in a sentence.
        for word in Word:
            word=word.translate({ord(','): None})
            word=word.translate({ord('.'): None})
            count +=1
            CapCheck = word[0].isupper()
            if CapCheck == True:
                print('{0}:{1}'.format(count,word))
                Count +=1
        count +=1
    if Count == 0:
        print('None')

                
IndexText(input())