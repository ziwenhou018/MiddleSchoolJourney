# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Me (thinking)", color="D3D3D3")
define me = Character("[name]", color="#28f35b")
define t = Character("Dr. Shah", color="#ff1eb4")
define a = Character("Annie", color="#ebaa1e")
define b = Character("Tyler", color="#5f1616")
define h = Character("Harold", color="#3d78cf")

define dissolve1 = Dissolve(1)
define dissolve15 = Dissolve(1.5)
define dissolve2 = Dissolve(2)
define move1 = MoveTransition(1)
define move15 = MoveTransition(1.5)
define moveinright1 = MoveTransition(1, enter=_moveright)
define moveinleft1 = MoveTransition(1, enter=_moveleft)
define moveoutright1 = MoveTransition(1, leave=_moveright)
define moveoutleft1 = MoveTransition(1, leave=_moveleft)

define audio.classroom = "audio/classroom.mp3"
define audio.bedroom = "audio/bedroom.mp3"
define audio.alarm = "audio/alarm.mp3"
define audio.alarmy = "audio/alarmy.mp3"
define audio.bell = "audio/bell.mp3"
define audio.wethands = "audio/wethands.mp3"
define audio.mc_walking = "audio/mc_walking.mp3"
define audio.opendoor = "audio/opendoor.mp3"
define audio.closedoor = "audio/closedoor.mp3"
define audio.pig = "audio/pig.mp3"
define audio.cow = "audio/cow.mp3"
define audio.sheep = "audio/sheep.mp3"
define audio.zombie = "audio/zombie.mp3"
define audio.creeper = "audio/creeper.mp3"
define audio.subwoofer = "audio/subwoofer.mp3"

transform slightleft:
    xalign 0.3 yalign 1.0

transform slightright:
    xalign 0.7 yalign 1.0

init python:
    def research(night):
        if night == 1:
            return (president == "Washington" and presidentNum == "1st") or (president == "Lincoln" and presidentNum == "16th") or (president == "Hoover" and presidentNum == "31st")
        if night == 2:
            return (president == "Washington" and presidentYear == "1789") or (president == "Lincoln" and presidentYear == "1861") or (president == "Hoover" and presidentYear == "1929") 
        return False


label start:

    default name = "John"
    default president = "Washington"
    default feeling = "worried"
    default bullyNerdInteraction = "hurt"
    default nightAction1 = "chat"
    default nightAction2 = "games"
    default blemishAsk = False
    default blemishPush = False
    default gossipListen = False
    default tylerWillDoWork = False
    default tylerStory = False
    default d4action = 1

    default tylerPoints = 0
    default projectPoints = 0

    play sound alarm volume 0.8

    "RING!!! RING!!! RINGGGGGGGGGGGGGGG!!!!!"
    
    stop sound

    "------SNOOZE------"

    "zzz..."

    "zzzzz....."

    "zzzzzzzzzzzzz.............."

    play sound alarmy volume 0.8

    n "..."

    n "OH MY GODDDDDD!!!"

    "You sprint to your alarm and slam the off button!"

    stop sound

    n "Ughhhh what time is it..."

    scene bedroom with dissolve15

    "You look at the clock. It says 7:30 am."

    n "Monday... ughhghh... when will it be the weekend again..."

    "You quickly get out of bed and get dressed."

    n "As a middle school student, it's always a pain to wake up this early. Why can't school start when normal people wake up, at like 9?"

    "You hear your mom downstairs calling you to hurry up. What name is she calling you?"

    python:
        name = renpy.input("You hear your mom downstairs calling you to hurry up. What name is she calling you?", length=32)
        name = name.strip() or "John"
    
    menu:
        "How will you respond?"

        "Be nice about it":

            me "Ok ok! I'm coming!"

        "Yell back":

            me "Stop yelling!! I'll be there soon!!"

    "You go downstairs, eat breakfast, then get driven to school by your mom."

    jump d1hallway

label d1hallway:

    scene hallway with dissolve15

    play music classroom

    "Finally arriving at school, you hear the sound of chit chat in the hallway."

    play sound bell volume 0.8

    "DING DONG!"

    n "Oh the bell! I should probably hurry to class!"

    jump d1classroom


label d1classroom:

    scene classroom with dissolve15

    "As you scurry to class, everyone starts to pile into the classroom. Dr. Shah stands at the front of the room, greeting each student as they enter."

    show teacher neutral with dissolve1

    t "Good morning!"

    "Everyone greets Dr. Shah and quickly gets seated."

    t "Today we will be starting our research project."

    n "Wh..wha...what!!! Research??"

    show teacher explain

    t "For this week, you will be researching American presidents."
    
    t "At the end of the week, you will be presenting your topic."
    
    t "You can choose to work in groups of 3, but I would like to remind you that this project will be a significant part of your final grade!"

    hide teacher with dissolve

    "Everyone looks around in the classroom, eager to form groups. Some students have already made eye contact."

    "Others... you're not sure if they even listened to the teacher's instructions."

    show annie neutral at right with dissolve15

    n "Annie! Please be in my group, bestie!"

    show annie happy
    
    "Lucky enough, you glance at Annie who is also looking back at you smiling."

    show teacher neutral with dissolve
    show annie neutral

    t "Alright now, feel free to start forming groups!"

    t "Good luck!"

    hide teacher with dissolve15
    
    "With that, you quickly get up and convene with Annie. She does the same with you."

    show annie neutral at center with move1

    a "Hey [name]!"

    me "Hey Annie! Glad we coordinated!"

    a "So we are definitely partnering up together but now we need a third person in our group."

    show annie think

    a "Hmmmm... who should we ask to join our group?"

    "Unfortunately, some students have already formed their groups of 3s."

    "You're also smart enough to not pair with the guy that's sleeping in class..."

    show annie think at left with move
    show harold neutral with dissolve

    a "There's Harold. He's pretty hard working, but does he even want to work with anyone?"

    hide harold with dissolve
    show tyler neutral with dissolve

    a "There's also Tyler, I guess? I heard he's mean to some people, but I also heard he's also nice to a couple others! Maybe we should give him a chance."

    hide tyler with dissolve
    show annie neutral at center with move

    a "I'll leave it to you to choose who we should work with!"

    "Who do you want to work with?"

    menu partner:
        "Who do you want to work with?"

        "Harold":

            show teacher embarrassed at right with moveinright

            t "Sorry, but Harold isn't ready to work with you yet! Maybe try again when the 'team' allows it!"

            hide teacher with moveoutright

            me "What... what 'team'?"

            me "???"

            jump partner

        "Tyler":

            me "Let's go work with Tyler!"

            python:
                partner = "tyler"
            
    a "Sounds good!"

    "You and Annie walk up to Tyler."

    show annie neutral at slightleft with move
    show tyler neutral at slightright with dissolve1

    me "Hey Tyler, wanna work togther?"

    show tyler smile

    b "You want to work with me? Sure, why not?"

    hide annie
    hide tyler
    with dissolve

    "Your group spends some time brainstorming a historical president."

    "Which one did you have in mind?"

    menu:
        "George Washington":

            $ president = "Washington"

        "Abraham Lincoln":

            $ president = "Lincoln"

        "Herbert Hoover":

            $ president = "Hoover"

    show annie neutral at slightleft
    show tyler neutral at slightright
    with dissolve

    me "I was thinking of doing [president]. What do you guys think?"

    show annie happy

    a "That sounds great, let's do that topic!"

    show annie neutral

    a "How should we split the work?"

    show tyler think

    me "..."

    show annie bruh

    me "Hey Tyler, do you have a preference on what part of the project you want to work on?"

    show tyler smile

    b "Nah."

    "Hmm, you have a feeling that Tyler won't be very cooperative. Should you say something about that?"

    menu:
        "Hmm, you have a feeling that Tyler won't be very cooperative. Should you say something about that?"

        "No, don't say anything. I'm sure it'll be fine.":

            pass

        "Yes, I should say something!":

            me "That's alright if you have no preference! Would you be ok if we just split the work randomly then? Since we should have equal contribution to the research."
        
            show tyler think

            b "Whatever, you guys can figure that out"

    show annie neutral
    show tyler neutral

    a "Ok. How about I handle section A, [name] can take section B, and Tyler, you take section C. Simple as that!"

    show annie happy

    me "Ok that works! And we can bring our research to class tomorrow"

    show annie neutral
    show tyler think

    b "Ok, whatever you guys say."

    play sound bell volume 0.8

    "And with that, the team meeting concluded."

    stop music fadeout 1.0

    jump d1bedroom

label d1bedroom:

    scene black
    with dissolve15

    "Finally, after a long day at school, you are welcomed back into your cozy home."

    "After dinner, you help with washing the dishes and then you go back to your bedroom."

    scene bedroom with dissolve15

    play music bedroom

    queue sound [opendoor, closedoor]

    "You remember that you were assigned to so some research for the group project for Dr. Shah's class."

    scene computer with pixellate
    
    "You spend some time doing a little bit of research."

    me "Hmm... [president]... who was he again?"

    "After some time using Google, you learned a little bit about [president] and how to do research!"

    me "Wikipedia is probably okay for general knowledge... right?"

    scene bedroom with pixellate

    me "Ok, I probably did enough research for now."

    "What do you want to do now?"

    menu:
        "What do you want to do now?"

        "Do a bit more research":

            $ nightAction1 = "research"

            n "I should probably spend some more time doing my part of the research so that our group is a bit ahead."

            scene computer with pixellate

            "You do some more research on [president]."

            "Apparently on wikipedia the box on the right gives a lot of general information about [president]."

            if president == "Washington":

                menu:
                    "It says that [president] was America's _ president."

                    "1st":
                        $ presidentNum = "1st"
                        $ projectPoints = projectPoints + 1
                    "2nd":
                        $ presidentNum = "2nd"
                        $ projectPoints = projectPoints - 1
                    "3rd":
                        $ presidentNum = "3rd"
                        $ projectPoints = projectPoints - 1
            
            elif president == "Lincoln":

                menu:
                    "It says that [president] was America's _ president."

                    "5th":
                        $ presidentNum = "5th"
                        $ projectPoints = projectPoints - 1
                    "16th":
                        $ presidentNum = "16th"
                        $ projectPoints = projectPoints + 1
                    "31st":
                        $ presidentNum = "31st"
                        $ projectPoints = projectPoints - 1

            elif president == "Hoover":

                menu:
                    "It says that [president] was America's _ president."

                    "17th":
                        $ presidentNum = "17th"
                        $ projectPoints = projectPoints - 1
                    "20th":
                        $ presidentNum = "20th"
                        $ projectPoints = projectPoints - 1
                    "31st":
                        $ presidentNum = "31st"
                        $ projectPoints = projectPoints + 1
            
            n "Wow, I didn't know that! Looks like we'll be a bit ahead of our game!"

        "Play the video games that you just bought":

            $ nightAction1 = "games"

            scene computer with pixellate

            stop music fadeout 1.0

            "You just bought Minecraft! Everyone has been talking about it for ages! You can finally see what all the hype is about."

            play music wethands

            "As you start up the game, you are fascinated by the simple graphics!"

            play sound mc_walking loop volume 0.7

            "Because you've played 1st person 3d games in the past, the movement is no issue to you."

            "Unfortunately, you have no idea what to do! There are no instructions."

            queue sound pig loop volume 0.7
            queue sound cow loop volume 0.4
            queue sound sheep loop volume 0.7

            show pig at left with moveinright1
            show cow at center with moveinright1
            show sheep at right with moveinright1
            pause 0.5
            hide pig with moveoutleft1
            hide cow with moveoutleft1
            hide sheep with moveoutleft1

            "You see sheep, pigs and cows here and there."

            stop sound

            "As the sun is setting, you've done nothing but explore the wilderness. That should be fine right?"

            play sound zombie loop volume 0.7

            "Finally as it is night time, you begin to hear growls and slow creeping of some sort of monster."

            stop sound
            show creeper at truecenter with zoomin

            "What's that?"

            play sound creeper volume 0.7

            "..."

            hide creeper
            stop music

            n "What just happened?"

            "You see a 'You Died' screen. After continuing, it brings you back to the main menu."

            n "Man, I don't even know what happened. Exploring was fun, but I have no idea what happened. I guess I'll try again tomorrow."

            "And with that, you log off Minecraft."

        "Hang out with Annie":

            $ nightAction1 = "chat"

            "You text Annie."

            me "hey Annie! watcha up to?"

            a "nothing much lol"

            a "did u hear about the kid that leaked all the government documents?"

            me "no.. why would anyone do that?"

            a "idk, what a great way to ruin your life while ur still 22"

            "You quickly look up what Annie was talking about."

            me "oh wow, google says that the kid was chased by like the whole military! With helicopters and stuff!"

            a "oh dang, that's kinda cool! but also bad lol"

            me "yea well, lesson learned. don't leak secret information!!"

            "You chat about other stuff with Annie..."
            
            "like whether she's the orphan in a musical..."
            
            "or if she could shoot fire from her teddy bear."
    
    scene bedroom
    play music bedroom if_changed

    "You had an interesting night!"

    "It's 10:30 pm now. After showering and brushing your teeth, you lie on your bed and start to reflect on what happened today."

    "Tyler seemed pretty nonchalant about the project and you're not sure if he will actually do work."

    menu:
        "How do you feel about this right now?"

        "Worried":

            $ feeling = "worried"

            me "Maybe I made the wrong choice."

            me "Maybe I shouldn't have chosen to work with Tyler."

            me "What if he does no work?"

            me "What if he does bad work that we will have to redo?"

            me "These concerns are fine, right??"

            "You are overwhelmed by your worriedness that it wears you out."

            "As if counting sheep, you count your countless worries until you finally fall asleep..."

        "Excited":

            $ feeling = "excited"

            me "I got a chance to really talk to Tyler. He wasn't as bad as people said!"

            me "Maybe we'll get to know him more tomorrow!"

            "You're excited to see what everyone has found from their research."

            if nightAction1 == "research":

                "Doing that extra bit definitely helps your group in the long run."

            "With a smile on your face, you close your eyes and get ready for the next day."

        "Calm":

            $ feeling = "calm"

            "You're still somewhat skeptical about Tyler, but you also might be overthinking things."

            me "We can just find out what everyone did tomorrow when we meet up."

            "You're quite calm and cleanse your mind about your worries."

            "Tomorrow will be a new day and you look forward to it."
            
    stop music fadeout 1.0
    scene black
    with dissolve2

    jump d2start