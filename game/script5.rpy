label d5classroom:

    scene classroom with dissolve15

    play music classroom

    "It’s the day for the presentation!"

    show teacher neutral with dissolve15

    t "Class! It’s time for the presentation now!"

    show teacher happy

    t "I can’t wait to hear your wonderful presentations."

    show teacher explain

    t "Harold, your group will be the first. And [name], get ready! Your group will be the next!"

    me "Okay Dr. Shah!"

    hide teacher
    show harold neutral with moveinright

    "Harold stands at the front of the class with his group, giving a presentation about President Franklin."

    h "And so, as you can see, Franklin's leadership during the Great Depression and World War II had a profound impact on our country's history."

    "As you watch Harold’s presentation about Franklin D. Roosevelt, you’re really impressed by how thorough the research is and how confidently he presents the points in each slide."

    "Strangely enough, none of Harold’s other groupmates seem to be taking turns in helping him present."

    "For a moment, you wonder what it would have been like if Harold joined you and Annie’s group instead..."

    "Harold and his group finished their presentation to a smattering of polite applause."

    show harold neutral at slightleft with move
    show teacher happy at slightright with dissolve15

    t "Well done, Harold's group! That was an excellent presentation."

    show harold happy

    h "Thank you, Dr. Shah."

    t "Now, let's hear from the rest of the group."

    hide harold with dissolve15
    hide teacher with dissolve15

    "You and Annie exchange nervous glances before beginning your presentation."

    n "Oh! Now it’s our turn!"

    show annie embarrassed at slightleft
    show tyler hehe at slightright with dissolve15

    "Ahh! You feel very nervous even though you’ve practiced multiple times."

    "You take a deep breath, and hope that you don’t stutter on your words."

    show annie happy
    show tyler smile

    if projectPoints >= 4:

        "Annie goes first presenting Section A on [president]."
    
        n "Nice work Annie! I knew I could rely on you!"

        "You go next, presenting Section B. You started off a little shaky, but you ended up pulling through till the end."

        if nightAction1 == "research":

            me "I found that [president] is the [presidentNum] president of America!"

            if nightAction2 == "research":
                
                me "I also found that [president] entered office in [presidentYear]!"

        elif nightAction2 == "research":

            me "I found that [president] entered office in [presidentYear]!"
        
        show annie embarrassed
        show tyler hehe

        "Next, is Tyler’s turn to present Section C."

        "You hold your breath for a moment as he presents."

        "It’s not terrible, at the very least he remembered what he was supposed to say, but it’s not like Harold’s either."

        "Perhaps even Tyler did not want to look bad in front of everyone else."

        show tyler smile
        show annie neutral

        if d4action == 3:

            "Regardless of what everyone else thinks, the presentation is finally finished."

            n "Yessss!! This is finally done!!"

            show teacher happy at right with moveinright

            t "Good Job! [name], I just wanna say I really appreciate your effort and your dedication to the project."

            t "You did a fantastic job with the work you completed. It's clear that you put a lot of time and thought into it."

            show teacher neutral

            me "Thank you, Dr. Shah. It was a lot of work, but I wanted to make sure we did a good job on the project."

            show teacher explain

            t "I can definitely appreciate that, but I also want to stress the importance of collaboration in group work."

            t "It's important to work together and support each other in order to achieve success."

            show teacher embarrassed

            t "I can tell that the distribution of work was… uneven."

            me "I’m sooo sorry for this, Dr. Shah. I was just thinking that it would probably be more effective if I could just finish this on my own."

            me "Also, our group didn’t have much time left, but there were still so many things that haven’t been done…"

            me "In fact, Annie also helped me with this. But definitely we'll make sure to do better in teamwork next time."

            show teacher neutral

            t "I totally understand your situation, [name]. Thank you for your honesty and willingness to take responsibility."

            show teacher explain

            t "Next time, if you are in a similar situation, remember, you can always reach out to me at any time. I will be very willing to give you tips for teamwork!"

            show teacher neutral

            me "Thank you Dr. Shah. I will."

            show tyler hehe

            "You glanced at Tyler, he definitely also heard Dr. Shah’s comments."

            t "And Tyler, I know you struggled with your part of the project, but I have faith that you'll improve with more practice."

            show tyler smile

            b "Thanks, Dr. Shah."

            show teacher happy

            t "Overall, good job. Keep up the good work, everyone."

        elif d4action == 2:

            "Regardless of what everyone else thinks, the presentation is finally finished."

            n "It’s finally finished!!"

            n "I had been worried sick!!!! But fortunately Tyler successfully completed his part for the presentation."

            show teacher happy at right with moveinright
            show annie happy
            show tyler happy

            t "Good job group! I love how you analyze the President’s motivation for making the reform."

            show annie neutral
            show tyler smile
            show teacher neutral

            t "However, I have to say that I think it could have done better in presenting the president’s reform policy."

            show teacher happy

            t "Well, nonetheless, I did want to acknowledge that I noticed your group had an equal share in the work and that you worked very well for your teamwork!"
            
            t "That's definitely something to be proud of."

            show teacher neutral

            me "Thank you Dr. Shah! I appreciate that."

            me "I did try my best to make sure everyone had a role in the project and that we were all working together effectively."

            me "But I do agree that there were some areas where we could have improved."

            show teacher happy

            t "Absolutely. And I don't want to discount the hard work you put in. It's clear that you take group work seriously and want to make sure everyone is involved."
            
            show teacher explain

            t "Moving forward, I think it would be helpful to focus on improving communication within the group and making sure that everyone is on the same page."

            show teacher neutral

            me "Okay, that makes sense. we'll definitely keep that in mind."

            show annie happy
            show tyler happy

            t "Great! I'm glad to hear that. Remember, group work can be challenging, but it's also a great opportunity to learn from each other and grow as a team."

            show annie neutral
            show tyler smile

            me "Thank you Dr. Shah for the advice and encouragement."

        elif d4action == 1:

            "Regardless of what everyone else thinks, the presentation is finally finished."

            show teacher happy at right with moveinright
            show annie happy

            t "I just wanted to take a moment to say how impressed I am with the work you and Annie did on your part of the project."

            t "Your effort really paid off and it shows in the quality of your work."

            show annie neutral
            show tyler hehe
            show teacher neutral

            t "However, I did notice that Tyler struggled with his part and his work wasn't up to the same standard."

            show teacher explain

            t "As a group, I think it would be beneficial to work on collaborating more effectively and learn how to work with different types of people."
            
            show teacher neutral
            show tyler neutral

            me "Thank you, Dr. Shah! We really appreciate the recognition."

            me "We tried our best to complete our part of the project to the best of our abilities."

            me "As for Tyler, we did try to help him out as much as we could."

            t "I understand, and I appreciate your efforts to help Tyler."
            
            t "However, it's important to remember that group work is all about collaboration and working together towards a common goal."

            t "I think as a group, there may have been some room for improvement in supporting each other and ensuring that everyone understood their roles and responsibilities."
            
            a "I see your point, and I agree. We could have done better in communicating with each other and making sure everyone was on the same page."

            show annie think

            a "Do you have any advice on how we can improve group work for the future?"

            show annie neutral
            show teacher explain

            t "Yes, I think it would be helpful to establish clear expectations for everyone in the group, and to make sure that everyone has a say in how the project is completed."
            
            t "It's important to learn how to work with different types of people and to collaborate effectively in order to achieve success."

            t "I believe you all have the potential to do great things together if you work on these skills."

            me "Thank you for the advice, we will definitely keep that in mind for this!"

            show teacher happy

            t "That's great to hear. I have no doubt that you will continue to improve! Keep up the good work!"
    
    else:

        "Annie goes first presenting Section A on [president]."
    
        n "Ok not bad Annie. You said a couple of things that sounded funny but that’s alright."

        "You go next, presenting Section B. You started off a little shaky, but you ended up pulling through till the end."

        if nightAction1 == "research":

            me "I found that [president] is the [presidentNum] president of America!"

            if nightAction2 == "research":
                
                me "I also found that [president] entered office in [presidentYear]!"

        elif nightAction2 == "research":

            me "I found that [president] entered office in [presidentYear]!"
        
        "However, when you look at Dr. Shah from across the classroom, she looks quite puzzled."
        
        show annie embarrassed
        show tyler hehe

        "Next, is Tyler’s turn to present Section C."

        "You hold your breath for a moment as he presents."

        "Wait, was he supposed to say that? You realize that he’s trying his best to say what he was supposed to say but it didn’t quite sound like what you all rehearsed."

        "Now you feel really embarrassed. Even Harold is judging you."

        show harold idk at right with moveinright
        hide harold with moveoutright
        show tyler embarrassed

        "But regardless of what everyone else thinks, the presentation is finally finished."

        # TODO
        show teacher sad at right with moveinright

        t "I'm sorry to say that I'm not very impressed with your presentation, group."

        show annie sad

        a "Oh no..."

        if d4action == 3:

            show teacher explain

            t "[name], I can tell you did all the work on this project, but unfortunately, it didn't show in your presentation."

            t "There are many aspects of the project that could be improved."

            me "I understand, Dr. Shah. We'll try to do better next time."

            t "And Tyler, I know you struggled with your part of the project, but I have faith that you'll improve with more practice."

            show tyler hehe

            b "Yeah, I'll try harder next time."

            show teacher happy

            t "Overall, it's clear that your group needs to work on collaborating more effectively and learning how to leverage your strengths and weaknesses to achieve a goal."

        elif d4action == 2:

            show teacher explain

            t "However, as much as I think your presentation could be improved, I’m glad to see how you all worked together to make sure you had finished it."

            t "While being accurate in your facts is one thing, being able to work as a team is another thing. The latter is what will get you far in life."

            show teacher neutral

            me "I understand, Dr. Shah. We'll try to do better next time."

            show teacher explain

            t "And Tyler, I know you struggled with your part of the project, but I have faith that you'll improve with more practice."

            show teacher neutral
            show tyler hehe

            b "Yeah, I'll try harder next time."

            show teacher happy
            show tyler smile
            show annie neutral

            t "Overall, all groups could always use more practice on collaborating more effectively and learning how to leverage your strengths and weaknesses to achieve a goal."

        elif d4action == 1:

            show teacher explain

            t "I can tell that the work completed for this presentation was not distributed evenly. There are many aspects of the project that could be improved."

            show teacher neutral

            me "I understand, Dr. Shah. We'll try to do better next time."

            show teacher explain

            t "And Tyler, I know you struggled with your part of the project, but I have faith that you'll improve with more practice."

            show teacher neutral
            show tyler hehe

            b "Yeah, I'll try harder next time."

            show teacher happy
            show tyler smile
            show annie neutral

            t "Overall, it's clear that your group needs to work on collaborating more effectively and learning how to leverage your strengths and weaknesses to achieve a goal."
    
    if tylerPoints >= 3:

        scene hallway with dissolve15

        "After the class, you and Annie just pack up your stuff and wanna get to the next class. Suddenly, Tyler calls you out."

        show annie neutral at slightleft
        show tyler neutral at slightright with dissolve15

        t "[name] and Annie…"
        
        show tyler kindasad

        t "I just really want to say sorry for the way I've been acting in our group."

        t "But.. I've realized something."

        show tyler smile

        t "You guys actually care about me and have been doing a lot to help me out. And I appreciate it, I really do."

        t "So, I'm sorry for being a pain and not pulling my weight."

        t "From now on, I'm gonna work with you all and do better. Thanks for having my back."

        show annie surprised

        a "Oh! Uhh you’re welcome."

        show annie embarrassed

        a "Yeah it’s not like we doubted you or anything ahahah..."

        me "Yeah, no problem man. Just let us know if you need anything! See you tomorrow!"

        scene outside with dissolve15

        "As you begin to leave the school, you see your mom’s car pull up to the pickup zone."

        "You smile to yourself."

        if projectPoints >= 4:

            "Your presentation went well, and you made a new unexpected friend."

            "You are glad because you wonder how things could have turned out poorly if you made different decisions, and a part of you wonders what it would have been like to have Harold in your group."

            "But regardless, this was the best outcome you could have hoped for."
        
        else:

            "Although your presentation could have gone better, you made a new unexpected friend."

            "You are glad because you wonder how things could have turned out poorly if you made different decisions, and a part of you wonders what it would have been like to have Harold in your group."
    
    else:

        scene outside with dissolve15

        "After school, as you begin to leave the school, you see your mom’s car pull up to the pickup zone."

        if projectPoints >= 4:

            "You smile to yourself."

            "Your presentation went well."

            "However, Tyler didn’t look like a happy camper."

            "You wonder if things would have turned out differently if you made different decisions, and a part of you wonders what it would have been like to have Harold in your group instead."

        else:

            "You are feeling a little dejected."

            "Your presentation didn’t go as well as you had hoped, and Tyler seems to still hate your guts."

            "You wonder if things would have turned out differently if you made different decisions, and a part of you wonders what it would have been like to have Harold in your group instead."

        n "Huh?"

        "You hear running coming up from behind you?"

        "You turn around and see two students shouting and chasing each other."

        n "Oh no."

        "They’re coming your way."

        "You try to maneuver so you dodge them but you’re too slow and one of them collides with you, sending you sprawling to the ground."

        "You’re okay, though you have some scrapes on your hand."

        "However, you realize that your backpack wasn’t zipped all the way and all of its contents spilled out onto the concrete."

        "The two students run off to continue chasing each other, not even apologizing to you."

        "As you quickly try to scoop everything back into the backpack, you see Tyler walk by."

        show tyler neutral with dissolve15

        "You and Tyler make eye contact, and a part of you hopes he stops to help you."

        "After all, you were in a group project together right?"

        show tyler bruh

        "Tyler rolls his eyes, and then leaves you to pick up after yourself without saying a word."
    
    stop music fadeout 1.0

    scene black with dissolve2

    "Thank you for playing Middle School Journey! If you want to know what would have happened if you picked other dialogue options, then feel free to play again!"