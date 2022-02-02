import readchar
import MakeSortedWordList

wordList = MakeSortedWordList.MakeSortedWordList("./RawWordList.txt")
answer = [0,'','','','','']
otherLetters = []
notLetters = []

#While there is more than one answer in the list
while len(wordList)>1 and answer[0] < 5:
    guessIndex = 0
    #Tell the user how many words are left in the list
    print(f"There are {len(wordList)} guesses left in my list.")
    #Suggest the first word and see if the user likes it
    userLikeTheWord = False
    while userLikeTheWord == False:
    #ask the user if they want to try this word.
        guess = ""
        for l in wordList[guessIndex][1:]:
            guess += l
        print(f"Do you want to try {guess}?", end='')
        like = readchar.readkey()
        print(like)
        if like == 'y' or like == 'Y':
            userLikeTheWord = True
        #While the don't find the next word.
        if like == 'n' or like == 'N':
            guessIndex += 1
            if guessIndex >= len(wordList):
                guessIndex = 0
    goodInputFromUser = False
    resultList = []
    while goodInputFromUser == False:
        #ask the user for the results
        result = input("Enter the word into the game and tell me the results.  Use Y for yellow, G for green, and N for letters not in the word:")
        if len(result) != 5:
            print("invalid lenght")
            continue
        inputGood = True
        for letter in result:
            if letter not in ['g','y','n','G','Y','N']:
                inputGood = False
        if inputGood == False:
            print("input is invalid.  Try again.")
            continue
        goodInputFromUser = True
    resultList = [0] + [char for char in result]
    i = 0
    #update the answer list and the other letters list
    while i < len(resultList):
        if resultList[i] == 'g' or resultList[i] == 'G':
            if answer[i] == '':
                answer[0] += 1
            answer[i] = wordList[guessIndex][i]
        if resultList[i] == 'y' or resultList[i] == 'Y':
            if wordList[guessIndex][i] not in otherLetters:
                otherLetters.append(wordList[guessIndex][i])
        i += 1
    #Now make a list of letters not in the answer
    i = 0
    while i < len(resultList):
        if resultList[i] == 'n' or  resultList[i] == 'N':
            #first make sure the letter is not in the other letters
            if wordList[guessIndex][i] not in otherLetters and wordList[guessIndex][i] not in answer:
                notLetters.append(wordList[guessIndex][i])
        i += 1
    #Build a new word list
    newWordList = []
    #Examine each word
    for word in wordList:
        #first make sure it doesn't contain any non present letters
        if len([letter for letter in notLetters if letter in word]) == 0:
            #then make sure it does contain all of the letters in other letters
            containsAllTheLetters = True #assume the word contains all the "Other Letters"
            for letter in otherLetters:
                if letter not in word:
                    containsAllTheLetters = False
                    break
            if containsAllTheLetters:
                #if it contains all the words move on to matching the answer pattern
                matchesAnswerPattern = True
                i = 1 #starting at the first letter in the result/answer
                while i < len(resultList):
                    #if the result was green, it must have that letter in this space
                    if resultList[i] == 'g' or resultList[i] == 'G':
                        if word[i] != wordList[guessIndex][i]:
                            matchesAnswerPattern = False
                    #if the result was yellow, the word MUST NOT have that letter in this place
                    if resultList[i] == 'y' or resultList[i] == 'Y':
                        if word[i] == wordList[guessIndex][i]:
                            matchesAnswerPattern = False
                    i += 1
                #If all these things are correct then the word is still a good candidate.
                if matchesAnswerPattern:
                    newWordList.append(word)
    wordList = newWordList
guess = ""
for l in wordList[0][1:]:
    guess += l
print(f"The answer is {guess}!!")