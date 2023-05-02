label d2classroom:

    scene classroom with dissolve15

    "It's Miss Baker's class again."
    
    show teacher neutral with dissolve1

    t "Good morning class!"

    show teacher explain

    t "Everyone, get into your project groups right away! Chop chop!"

    hide teacher explain with dissolve1

    "The class quickly shuffles around..."

    "...except the student that's still sleeping!"

    "You sit with Annie and Tyler."

    show annie neutral at slightleft
    show tyler neutral at slightright
    with dissolve1

    "The interaction in the hallway was quite awkward."

    "You quickly glance at Tyler to check how he's doing."

    hide annie neutral with dissolve1
    show tyler neutral at center with move

    if bullyNerdInteraction == "help":

        show tyler smile

        b "Kinda nice Miss Baker didn't give us detention or anything."

        "Random Student" "Shhhh!!!"

        hide tyler smile with dissolve1

    elif bullyNerdInteraction == "hurt":
        
        show tyler bruh

        "He gives you the side eye."

        b "Hmph."

        hide tyler bruh with dissolve1
    
    show teacher neutral with dissolve1

    t "Good morning class! Happy Tuesday!"
    
    show teacher explain

    t "I hope you all weren't up playing Minecraft or talking to your friends and started on your work!"

    if nightAction == "research":

        n "Our group should be pleased that I found that [president] is the [presidentNum] president of America!"
    
    else:

        n "Wow, is she a psychic?"

        n "It's okay though, I still got a little bit of research done."

    show teacher neutral

    "Miss Baker stands at the front of the room, handing out a sheet of paper to each student."

    show teacher explain

    t "Alright, class. I want to emphasize that this assignment is a teamwork project..."

    t "...which means that every one of you has to participate and do something in the group work."

    show teacher happy

    t "It's not just about individual performance, but also how well you work together as a team."

    show teacher explain

    t "Here are some tips for successful collaboration."

    hide teacher explain with dissolve

    "Miss Baker hands out the paper on your desk."

    me "Thank you, Miss Baker."

    "After Miss Baker hands out the paper to everyone, she goes back to the front of the class."

    show teacher explain with dissolve

    t "Everyone, please read the tips silently as I read them out loud."

    t "1. Listen to others: It's important to listen to your team members and consider their ideas and suggestions."

    t "2. Communicate effectively: Communicate your ideas clearly and ask questions to make sure you understand what your team members are saying."

    t "3. Set goals: Set clear goals and expectations for the project so everyone knows what they are working towards."

    t "4. Respect others: Show respect to your team members and be open to different perspectives and opinions."

    t "5. Take responsibility: Take responsibility for your part in the project and make sure you are meeting deadlines and contributing to the team effort."

    t "6. Be flexible: Be open to changes in the project and be willing to adjust your approach if needed."

    t "7. Stay positive: Encourage your team members and stay positive, even if things get difficult."

    "As Dr. Shah explains this, you hope that Tyler is paying attention."

    show teacher happy

    t "Okay everyone! Start working with your groups!"

    hide teacher happy with dissolve1
    show tyler neutral with dissolve1

    "You glance at Tyler and see a very noticeable blemish on his face!"

    n "What happened to his face. Should I ask about it?"

    menu:
        "Ask about Tyler's face?"

        "Ignore it":
            
            n "Why should I care about it? Just ignore it."

            n "Besides, we should probably focus on the project."

        "Ask":

            $ blemishAsk = True

            me "Hey Tyler, what happened to your face?"

            show tyler embarrassed

            b "What do you mean what happened? Nothing happened."

            "Hmm, he's pretty resilient about telling you what happened."

            "Since he threatened Harold for his homework today, perhaps he was unsuccessful previously and got in a fight?"

            "It could have been from earlier today or even from yesterday."

            "Will you pry on it further?"

            menu:

                "Yes":

                    $ blemishPush = True

                    me "Did you get beat up or something?"

                    show tyler mad

                    b "Shut up, [name]. Mind your own business."

                "No":

                    me "Are you sure it's nothing? I hope you're okay."

                    show tyler smile

                    b "Uh, thanks, I guess. Why do you care?"
            
            "Before either of you continue, Annie jumps in the conversation."
    
    show tyler neutral at slightright with move
    show annie neutral at slightleft with dissolve1

    a "Hey, guys, what progress did you make in your research?"

    me "I did some research."

    if nightAction == "research":

        me "I also found that [president] is the [presidentNum] president of America!"

        if research(1):

            show annie happy

            a "Great work [name]!"
        
        else:

            show annie think

            a "Is that true? That seems kind of off..."
    
    show tyler think

    b "Hmmm... We were supposed to do the research?"

    show annie surprised

    n "What the heck! Did Tyler actually forget or did he purposefully not do it?"

    n "Should I confront him about it?"

    show annie neutral

    menu:

        "Ignore it":

            "You're not really the confrontational type."

            show annie neutral

            a "That's alright. Can you remember to work on it today?"

            show tyler neutral

            b "Ok."

            "You're quite skeptical about that short ‘Ok'."

            play sound bell volume 0.8

            "After a pretty short meeting, everyone departs for their next class."

        "Inquire about why Tyler didn't work":

            me "Tyler, did you really forget to work on the research?"

            if not blemishPush:

                show tyler embarrassed

                b "Uhhh..."

                me "Hey, Tyler, you need to contribute to this project. You need to take responsibility like Dr. Shah said."

                me "It's a team effort, and we're all in this together."

                show tyler neutral

                b "Alright, alright. I'll try to do the research tonight."

                play sound bell volume 0.8

                "As the meeting is about to end, Tyler quickly interrupts."

                show tyler kindasad

                b "Sorry, I didn't forget. Something just happened... that prevented me from doing my work..."

                "Something happened? You're quite surprised."

                show tyler hehe

                b "But anyway, see you all tomorrow!"

                hide tyler hehe with moveoutright

                "You hope that Tyler can do his part tonight."

                "Something that happened in his life... what does that mean?"

                "Since everyone is departing for their next class, you quickly do the same."
            
            else:

                show tyler mad

                b "Why do you have to pry on my life so much? Can't you just leave me alone?"

                me "Aren't you being a hypocrite? You wouldn't leave Harold alone."

                show tyler bruh

                b "Well that's different..."

                show tyler neutral

                b "Ugh ok fine. I'll do my part."

                show annie happy

                a "Alright guys, let's just do our parts tonight, okay?"

                play sound bell volume 0.8

                "After a shaky meeting, everyone departs for their next class."
        
        "Yell at Tyler":

            me "Tyler! You can't be doing this! This is a group project! You need to contribute just like we do!"

            show teacher mad at right with moveinright

            t "Students, please no yelling at your classmates! Remember rule 7 is to stay positive!"

            hide teacher mad with moveoutright

            show tyler bruh

            b "Yea [name]. No yelling at your classmates."

            me "Well you should remember that rule 5 is to take responsibility, which you clearly aren't doing."

            show tyler mad

            b "Clearly, you're not following rule 4, which is to respect others."
            
            b "You have no idea what's going on in my life so shut it."

            "Something going on with his life? You're quite dumbfounded."

            "He needs to stop picking on others."

            "Also, did he actually listen to Dr. Shah's rules?"

            show annie embarrassed

            a "Alright guys, let's just do our parts tonight, okay?"

            play sound bell volume 0.8

            "After a shaky meeting, everyone departs for their next class."

    stop music fadeout 1.0

    jump d2bedroom

label d2bedroom:

    scene bedroom with dissolve15

    play music bedroom

    queue sound [opendoor, closedoor]

    "You come back to your room after a long day at school and a tasty dinner."

    "You sit down at your desk, when suddenly you hear your phone buzz."

    n "Hmm, must be a text message, let’s see who it’s from."

    a "yo [name], i just heard some tea about Tyler!! wanna hear?"

    n "Tea about Tyler? Did he get in trouble with the principal again?"

    "Hmmm sounds very tempting, and you wonder what the tea could be."

    "What should you do?"

    menu:

        "What should you do?"

        "Spill the tea":

            $ gossipListen = True

            me "YES fill me in!"

            a "OMG ok"

            a "sooo I heard... that Tyler's dad is having an affair with the principal!!"

            me "WHAT?? are you for real?"

            a "YESSS people in our class were saying they were seeing his dad go into the principal's office multiple times this week!"

            me "omg... that does seem a little suspicious..."

            a "yea for sure! and it makes so much sense..."

            a "...because why do you think Tyler never really got a lot of consequences?"

            a "probably gets the principal's favoritism"

            me "i cant believe it... thats so crazy!"

            a "i know right?? its also probably why Tyler never does his work since he knows he can just get away with it."
            
            a "like even today, he legit showed up without doing his part on the research!"

            me "hmmm... im not sure but it could be a possibility?"

            "You put your phone down after reading the gossip Annie shared."

            "That was a lot to take in."

            n "Could everything Annie said be true??"

            "You're quite exhausted and don't want to think about Tyler."
            
            "The idea that he might not do any work tonight bothers you."

        "Ignore the gossip":

            me "nah, i think im ok"

            me "its probably just some rumors the other kids are talking about anyway"

            me "ill see you tomorrow in class though!"

            "With that, you place your phone down."
    
    "Now, time to figure out how you want to spend the rest of your night!"

    menu:

        "Do you want to..."

        "Do more research":

            $ nightAction = "research"

            n "I should probably spend some more time doing my part of the research so that our group is a bit ahead."

            scene computer with pixellate

            "You do some more research on [president]."

            n "Let me check wikipedia again."
            
            "The box on the right gives a lot of general information about [president]."

            if president == "Washington":

                menu:
                    "It says that [president] started his presidency in _."

                    "1777":
                        $ presidentYear = "1777"
                    "1781":
                        $ presidentYear = "1781"
                    "1789":
                        $ presidentYear = "1789"
            
            elif president == "Lincoln":

                menu:
                    "It says that [president] started his presidency in _."

                    "1861":
                        $ presidentYear = "1861"
                    "1863":
                        $ presidentYear = "1863"
                    "1865":
                        $ presidentYear = "1865"

            elif president == "Hoover":

                menu:
                    "It says that [president] started his presidency in _."

                    "1921":
                        $ presidentYear = "1921"
                    "1929":
                        $ presidentYear = "1929"
                    "1933":
                        $ presidentYear = "1933"
            
            n "That's quite a lot of years ago!"

            n "Looks like we'll be a bit ahead of our game!"

        "Play video games":

            $ nightAction = "games"

            scene computer with pixellate

            stop music fadeout 1.0

            "Thinking back on your session on Minecraft yesterday, you decide to give it another go."
            
            "That $29 wasn't spent for nothing."

            play music subwoofer

            "As you start up the game again, you are once again greeted by a new world of trees and grasslands."

            play sound mc_walking loop volume 0.7

            "This time, you'll make sure that you don't die to whatever killed you last night."

            "It is still day time, so you devise a plan to gather dirt and wood to build a makeshift house."

            queue sound pig loop volume 0.7

            show pig at left with moveinright
            hide pig with moveoutleft

            "Every here and there as you're working, you still hear the sounds of animals nearby."

            stop sound

            "As the sun begins to set, you face your dirt and wooden house with accomplishment."

            play sound zombie loop volume 0.7

            "Finally as it is night time, you begin to hear growls and slow creeping of some sort of monster."

            "Luckily, you are in the safety of your home."

            "For now, you decide to remain inside until it is day time."

            "..."

            "..."

            stop sound

            "..."

            n "Looks like the sun is rising. The monsters are slowly dying."

            "You're relieved to have survived a night of Minecraft!"

            "With your first accomplishment, you decide that this is a good time to stop for the night."

            "And with that, you log off Minecraft."

            stop music fadeout 1.0
    
    scene bedroom
    play music bedroom if_changed

    "You feel that you accomplished quite a bit today."

    if gossipListen:

        "You're also quite curious about the gossip that you heard today."

        n "What is really up with Tyler?"

        n "I guess I'll find out tomorrow."

    else:

        "You start thinking about what you'll accomplish tomorrow."

    "And with that, you quickly drift to sleep."

    stop music fadeout 1.0
    scene black
    with dissolve2