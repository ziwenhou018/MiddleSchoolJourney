label d4start:

    play sound alarmy volume 0.8

    "RING!!! RING!!! RINGGGGGGGGGGGGGGG!!!!!"

    stop sound

    n "Time to go to school!"

    jump d4classroom

label d4classroom:

    scene hallway with dissolve15

    play music classroom

    "You walk to Dr. Shah's class as usual."

    play sound bell volume 0.8

    scene classroom with dissolve15

    show teacher neutral with dissolve15

    t "Alright, class, today is the last day to work on your projects."

    show teacher happy

    t "Presentations will be tomorrow and I hope you've all made some progress. I can't wait to see your amazing projects!"

    show teacher neutral

    t "So now, I will leave some time for you guys to spend with your group and finalize your project and presentation."

    t "Please make sure your work is up to par."

    n "Ahhhh!! Tomorrow?!! Are we really ready for this?"

    hide teacher

    "Everyone shuffles once again to get into their group."

    show annie neutral at slightleft
    show tyler kindasad at slightright
    with dissolve15

    a "Okay, group. Let's each share our progress. I can go first."

    a "So, I have done all the research for section A and I can be responsible for this part for the presentation."

    show annie happy

    me "Good job Annie!! Perfect."

    me "I'm almost done with section B, and I can be responsible for section B in the presentation too."

    show annie neutral

    me "So how is your part Tyler? You are responsible for section C right?"

    show tyler smile

    b "Uh, yeah, I've been working on it."

    show tyler kindasad

    "You quickly skim through Tyler's part and find that only some of the questions are answered!"

    "Besides, the answered parts are just a mess of scribbles and half-finished ideas."

    n "Is this the only work Tyler has done?!! The presentation will just be tomorrow!"

    "Annie also notices the messy work that Tyler did. She seems to be very angry about this."

    show annie bruh

    a "We should never have let him join our team in the first place."

    a "He's just free loading. Maybe we should have worked with Harold."

    show harold surprised at left with moveinleft1
    pause 0.5
    hide harold with moveoutright1

    "Weirdly enough, Tyler did not respond to Annie's comments."

    "He kept his head down and didn't say a word."

    play sound bell volume 0.8

    "Ringgggg."

    n "Class is over already?"

    hide tyler with dissolve15

    "Tyler gets up and goes to his desk."

    show annie mad at center with move

    a "I can't believe that was all that Tyler did."

    a "We shouldn't have expected anything from him."

    a "I can't stand him anymore!!!"

    a "We are a group but look at what he has done. Tomorrow is the presentation!!!"

    show annie bruh

    me "Yeah, I know. It's been tough."

    show annie sad

    a "What are we going to do?"

    "You're not sure what the next best step is, but you have a few options."

    "What would you like to do next?"

    menu:

        "What would you like to do next?"

        "Tell Dr. Shah":

            $ tylerPoints = tylerPoints - 1

            $ d4action = 1

            me "Maybe we should tell Dr.Shah about Tyler's behaviors. We tried to work as a team, but Tyler just isn't willing to collaborate."

            show annie neutral

            a "I agree! Let's go talk to Dr.Shah right now!"

            "You walk up to Dr. Shah's desk."

            show annie neutral at slightleft with move
            show teacher neutral at slightright with dissolve

            t "Hey Annie and [name], anything happened to your group? I'm so looking forward to your group's presentation tomorrow."

            me "Actually, we wanna share with you the current situation in our group."

            show teacher happy

            t "Oh! How is it?"

            me "Annie and I have almost finished all of our work, but Tyler... his part is still a mess."

            show teacher neutral

            me "I know we are supposed to be a group and help each other, but we just can't figure out how to get along with him. He never wants to collaborate."

            show teacher embarrassed

            t "Ohhhh! I am so sorry to hear what happened in your group."

            t "Don't worry about tomorrow's presentation. Just be prepared for the parts that both of you are responsible with. I will talk to Tyler later."

            me "Thank you Dr. Shah."

            hide teacher with dissolve
            show annie neutral at center with move

            "Dr. Shah leaves to speak with Tyler."

            a "Finally! We should have told Dr. Shah earlier about this!"

            show tyler kindasad at right with move

            "Suddenly, you see Tyler just standing next to the corner!"

            "He must have heard what you and Annie just talked about. You hurried, lower your head and quickly leave."

        "Invite Tyler To Work Tonight":

            $ tylerPoints = tylerPoints + 1
            $ projectPoints = projectPoints + 1

            $ d4action = 2

            "Maybe Tyler just needs more help to work on his work!"

            me "I'll talk to him during lunch."

            scene lunchroom with dissolve15

            "You spot Tyler sitting alone by the table. You walk and sit across from him."

            show tyler neutral

            me "Hey Tyler. Do you want to work together tonight?"

            me "Annie and I have already finished our part, so I think we should help you and let's try to finish up our project tonight!"

            show tyler surprised

            b "Really? You want to work with me?"

            me "Yeah, we are a team. We are supposed to collaborate to finish the work."

            me "We could get a lot done if we work together, and I'd be open to help you out with figuring out some of the material."

            "Tyler hesitates for a moment and finally nods his head."

            show tyler smile

            b "Alright, let's do it."

            me "Great! We can work together through a video call later at home. I'll talk with you then!"

            "Tyler sat there and nodded his head. Hopefully this can help Tyler to be more productive with the project..."

        "Do Tyler's Work Yourself":

            $ projectPoints = projectPoints + 1

            $ d4action = 3

            me "I don't think telling the teacher will help."

            me "And I don't want to work with Tyler, either."

            show annie sad

            a "I know, but we can't just let him ruin our project."

            me "Right... I'll just have to work extra hard to make up for it."

            show annie neutral

            a "I can help you, too."

            me "Thanks, Annie! I appreciate it. I know you are always the best!"

    stop music fadeout 1.0

    jump d4bedroom

label d4bedroom:

    scene bedroom with dissolve15

    play music bedroom

    queue sound [opendoor, closedoor]

    if d4action == 1:

        "You return home and enter your room."

        "Tomorrow's finally the day of the presentation, so you want to make sure you have everything ready."

        n "I feel kind of bad about telling Dr. Shah about Tyler but... it had to be done."

        n "Annie and I are so fed up with Tyler that we have to take a stand on the situation."

        n "Hopefully Dr. Shah's talk with Tyler helps him to prepare for the presentation tomorrow..."

        n "Speaking of which, I should probably prepare as well."

        scene computer with pixellate

        "You finish up your part and research a little bit."

        scene bedroom with pixellate

        "After you feel that you are comfortable with your part of the presentation, you go to sleep."
    
    elif d4action == 2:

        "You return home and enter your room."

        "You remember that you and Tyler agreed to work through the presentation through video call, so you set up your computer to get the call ready."

        scene computer with pixellate

        "Ring ring!!!"

        "Your computer rang."

        "You are getting a call from Tyler."

        "You pick up."

        me "Hey Tyler! Ready to get started on the work?"

        b "Yeah... let's start"

        me "Ok, so I think first we should take a look at your notes so we can see how to structure it onto the presentation slides."

        b "Sure, here I can show you my notes."

        "Suddenly, you hear a loud crash, as if a glass cup had shattered."

        "You look up to see what might've fallen in your room, but see that nothing shattered."

        "Then, you hear some shouting, and you realize the sounds are coming from Tyler's screen."

        me "Hey... is everything ok? Is there something happening?"

        b "Uh... no... it's nothing, just mind your own business."

        "But unfortunately, you hear more shouting going on in the back... potentially a man and woman's voice, and you hear it getting gradually louder and louder."

        b "Ok, actually, my parents are arguing right now again, I think my dad came home drunk."

        me "Oh... do you want to work on this later then?"

        b "No, it's ok. I don't want this to let me be behind on my work anymore."

        b "I'll change my location in my house so we can get some work done."

        n "Tyler must be going through a lot with his family right now, especially between the family dynamic."

        n "I'm glad that he was able to be transparent with me though, since it helps me to understand his circumstances a bit better."

        "Tyler returns to the call sitting in a different room."

        "Thankfully, the background noise isn't as present anymore, so you and Tyler continue to work together."

        "As you work, you slowly hear the yelling and noises calm down..."

        "Hopefully everything on Tyler's end is ok... but good news is that you and Tyler were able to get a lot of work done and feel pretty good about tomorrow's presentation."

        b "Okay, thanks for working with me once again!"

        "You say your goodnights and both get a good night's rest."

    elif d4action == 3:

        "You return home and enter your room."

        "Tomorrow's finally the day of the presentation, so you want to make sure you have everything ready."

        n "UGH, I can't believe Annie and I have to cover Tyler's portion of the project."

        n "He's just going to get the grade without having done any helpful work."

        "BUZZ BUZZ"

        "It's a text from Annie!"

        a "Hey, are you free now to hop on a call to finish Tyler's part of the presentation?"

        me "Yeah, I'm really discouraged that we got stuck with doing his work."

        me "It's so unfair and it makes me so frustrated."

        a "Yeah, it truly does suck that we have to be in this position."

        a "I understand that we are both very angry and frustrated with the situation, but let's just try to get what we can do to the best of our abilities!"

        me "I agree, I'm going to take some deep breaths. Thanks for always letting me process my emotions through you."

        "You take some deep breaths."

        me "Ok, I'm ready to get on a video call now."

        scene computer with pixellate

        "You and Annie go into a video call to prepare for the presentation and finish Tyler's portion of the presentation."

        "You and Annie work diligently on the project for the rest of the day, but it's clear that Tyler isn't putting in any effort."

        "You can't help but feel frustrated."

        "Let's just hope the presentation goes well tomorrow..."

        "You finish up, say your goodnights, then go to bed."

    stop music fadeout 1.0
    scene black
    with dissolve2

    jump d5classroom