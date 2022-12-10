from questions import Question

Questions = [
    "In the UK, the abbreviation NHS stands for National what Service?\n(a) Humanity\n(b) Health\n(c) Honour\n(d) Household\n\n:",
    "\nWhich Disney character famously leaves a glass slipper behind at a royal ball?\n(a) Pocahontas\n(b) Sleeping Beauty\n(c) Cinderella\n(d) Elsa\n\n:",
    "\nWhat name is given to the revolving belt machinery in an airport that delivers checked luggage from the plane to baggage reclaim?\n(a) Hangar\n(b) Terminal\n(c) Concourse\n(d) Carousel\n\n:",
    "\nWhich of these brands was chiefly associated with the manufacture of household locks?\n(a) Phillips\n(b) Flymo\n(c) Chubb\n(d) Ronseal\n\n:",
    "\nThe hammer and sickle is one of the most recognisable symbols of which political ideology?\n(a) Republicanism\n(b) Communism\n(c) Conservatism\n(d) Liberalism\n\n:",
    "\nWhich toys have been marketed with the phrase “robots in disguise”?\n(a) Bratz Dolls\n(b) Sylvanian Families\n(c) Hatchimals\n(d) Transformers\n\n:",
    "\nWhat does the word loquacious mean?\n(a) Angry\n(b) Chatty\n(c) Beautiful\n(d) Shy\n\n:",
    "\nObstetrics is a branch of medicine particularly concerned with what?\n(a) Childbirth\n(b) Broken bones\n(c) Heart conditions\n(d) Old age\n\n:",
    "\nIn Doctor Who, what was the signature look of the fourth Doctor, as portrayed by Tom Baker?\n(a) Bow-tie, braces and tweed jacket\n(b) Wide-brimmed hat and extra long scarf\n(c) Pinstripe suit and trainers\n(d) Cape, velvet jacket and frilly shirt\n\n:",
    "\nWhich of these religious observances lasts for the shortest period of time during the calendar year?\n(a) Ramadan\n(b) Diwali\n(c) Lent\n(d) Hanukkah\n\n:"
    ]

questions = [
    Question(Questions[0], "b"),
    Question(Questions[1], "c"),
    Question(Questions[2], "d"),
    Question(Questions[3], "c"),
    Question(Questions[4], "b"),
    Question(Questions[5], "d"),
    Question(Questions[6], "b"),
    Question(Questions[7], "a"),
    Question(Questions[8], "b"),
    Question(Questions[9], "b"),
]

money = 0
question_count = 0
for question in questions:
    answer = input(question.questions)
    if answer == question.answers:
        question_count += 1
        money += 100000
    if question == questions[3]  or question == questions[7]:
        print("If you get next question wrong you lose $200,000")
    elif ((question == questions[4]) and (answer != question.answers)) or ((question == questions[8]) and (answer != question.answers)):
        money -= 200000
        print(money)
print("You got {} question right\nYou walk away with ${}".format(question_count, money))
