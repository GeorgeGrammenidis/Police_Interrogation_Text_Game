def PlayCase (info , questions , answers , correct):
    print ('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print ("Before interrogating the suspects here is all the available information about this case:")
    asked_questions = []
    asked_numbers = []
    for i in range (len(info)):
        print (info[i])
    help = input ("Type anything to move on once you study these facts ")
    print ('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    while True:
        print ("Questions you can ask the suspects:")
        for i in range (len(questions)):
            if (questions[i] not in asked_questions):
                print (questions[i])
        key = input ("Type the digit corresponding to the question you want to ask ")
        while (key!='1' and key!="2" and key!="3" and key!="4" and key!="5" or key in asked_numbers):
               key = input("Please type one of the available digits ")
        if key == "5":
               break
        key = int(key)
        asked_questions.append(questions[key-1])
        asked_numbers.append(key)
        print ('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print (questions[key-1])
        for i in range (3):
            print ("Subject ", i+1, ":")
            print ( answers[key-1][i])
        print ('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        q = input ("Type anything to proceed ")
    print ('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print ("Now we enter the accusatory phase")
    guess = input  ("One of the three suspects is a lier. Type the number (1,2 or 3) of your guess ")
    while guess!='1' and guess!='2' and guess!='3':
        guess = input("The acceptable answers are 1, 2 or 3 ")
    if guess==correct[0]:
        print ("You guessed correctly!")
        print ("The gotcha moment that proves the suspect was lying was: ")
        print (correct[1])
        return True
    else:
        print ("Your guess was incorrect you dumbass")
        return False
    print ('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

case_1_info = ['I) A bar near the coast was blown up at 2:43' , 'II) The investigators found pieces of an exploding mechanism near the bar' ,'III) Every person working there died except from the owner who was out of town and the barwoman who left earlier (this information has not been public yet)' , 'IV)  The 3 suspects that are about to be interrogated were spotted between 1:00 and 2:00 near  the bar by nearby security cameras']
case_1_questions = ['1) Have you ever been to the bar and do you know anyone that worked there?' , '2) How often do you visit this area?' , '3) What were you doing this late near the coast?' , '4) The barwoman left earlier than normal that day. Why do you suspect she would do that? ' , '5) (stop the questions and accuse one of them of lying)' ]
case_1_answers = [ ["No, I've never been there and I don't know anyone that has ever worked there" , "I was going there that night but I don't personally know anyone working there" , 'I used to go there regularly last year and I have seen the owner on TV'] , ["I live there so all the time" , "Once or twice a month" , "When I feel like crushing some poon, am I right officer?"] , ["Going home from work" , "Returning home from the bar" , "I was on a date at the beach that ended badly"] , ["Why on earth would I know what Amanda was doing?" , "How could I possibly know that? Is this some kind of trick question so I would accidentaly confess?" , "Why am I being asked this? Are you suspecting me? I do not know this woman!" ]]
case_1_correct = ['1' , 'When asked question 1, that suspect claims that they do not know anyone from the bar yet when asked question 3 they reveal that they know the name of the barwoman (Amanda) despite that not being public information']
case_1 = [ case_1_info , case_1_questions , case_1_answers , case_1_correct]

case_2_info = ['I) A woman was found murdered on a warehouse in Tallinn' , 'II) Only the 3 suspects had a key and therefore access to the warehouse' , 'III) Suspects 2&3 work as janitors in the warehouse and reportedly live a quite life, have low income and have never left Estonia according to the records of the authorities' , 'IV) Suspect 1 owns the warehouse and makes frequent business travels to Belarus' , 'V) Suspects 1&3 are reportedly native Estonians while 2 is from Latvia']
case_2_questions = ['1) Did you know this woman?' ,  '2) Where were you at the night of the murder, approximately 3 days before the body was found?' , '3) How often are you alone in the warehouse? ' , '4) What was your opinion of this person?' , '5) (stop the questions and accuse one of them of lying)' ]
case_2_answers = [ ["No I have no idea who she is" , "Yes she is in my book club" , "Yes we in fact used to date"] , ["I was at a basketball game that I had reserved tickets for for 3 weeks" , "I was at my girlfriend's birthday party" , "I was staying with a couple of friends in Vilnius"] , ["I go there once a week when people are working so rarely" , "I work there part time on Mondays, Tuesdays and Wednesdays" , "I work there only on Thursdays and Fridays"] , [" I did not know this person" ,  "She was a manipulative, dishonest, shady and immoral individual" , "I am not happy that she died but she did cheat on me and I had been angry for a long time, but I still really cried about her death"] ]
case_2_correct = ['3', 'According to the Estonian authorities suspect 3 has never left the country yet he claims that he was in Vilnius on the night of the murder, which is located in Lithuania']
case_2 = [case_2_info , case_2_questions , case_2_answers , case_2_correct]

case_3_info = ['I) Vehicular homicide, hit and run (aka someone was ran over by a car) , by unknown car outside of a small village in Armenia at around 13:40' , 'II) There is another village 40km away, a mountain range 90km away and a forest 70km away' , 'III) The 3 suspects were spotted in the village where the hit and run happened one hour before the murder (12:50)' , 'IV) Their cars have tires matching those on the body']
case_3_questions = ['1) Describe the properties of your car' , '2) What was your relationship with this person?' , '3) You were spotted in the village one hour before the murder. What were you doing there?' , '4) Where were you when the murder happened, aka 13:40?' , '5) (stop the questions and accuse one of them of lying)']
case_3_answers =  [ [ "My car is a bulky jeep that can run up to 80km per hour" , "My car is an old piece of shit but it can still reach 50km in an hour" , "My car is 30 years old and it can reach 55km per hour max"] , ["We used to go to school together, haven't talked ever since" , "Used to work together, never really talked" ,  "Haven't heard of this person"] , ["Visited family" , "Went to buy gasoline because it is cheaper there" , "Stopped to get water on my way to the mountains"] , ["I was at the nearest forest to collect wood" , "I went to the nearest village to visit a friend" , "I was at the mountain range for hiking"] ]
case_3_correct = ['3' , 'Suspect 3 claims his car can reach at best 55km in an hour, yet he also claims that 50 minutes after he was spotted in the village he was at the mountain range which is impossible because it is 90 km away']
case_3 = [case_3_info , case_3_questions , case_3_answers , case_3_correct]
levels = [ case_1 , case_2 , case_3 ]
score=0
cases= ["1" , "2" , "3"]
completed_cases=[]
print ("Welcome to this detective text game. The rules are simple: When you select a case you get to read all the available information about it and then select what questions to ask the 3 suspects. One of them is always lying, so when you are comfortable with the information you have you can proceed and accuse them. Good luck!")
while (len(completed_cases) < len(levels)):
    print ('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    for i in range (3):
        if (cases[i] not in completed_cases):
            print ("Case " , cases[i])
    stage = input ("Type the corresponding number to select that case ")
    while (stage not in cases) or (stage in completed_cases):
        stage = input("Type a valid number ")
    completed_cases.append(stage)
    stage = int(stage)
    if (PlayCase(levels[stage-1][0] , levels[stage-1][1] , levels[stage-1][2],levels[stage-1][3])):
        score = score + 1
print ("Your score is " , score, " out of 3")
if (score== len(levels)):
    print ("You got everything correctly")
elif (score==0):
    print ("You did not get anything correctly, you are abysmally terrible")
        
    
                                                                                                                                                                                                                             

