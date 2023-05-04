label d3start:

    play sound alarmy volume 0.8

    "RING!!! RING!!! RINGGGGGGGGGGGGGGG!!!!!"

    n "I'm not snoozing! This is annoying!"

    "You sprint to your alarm and slam the off button!"

    stop sound

    n "But at least it's waking me up!"

    scene bedroom with dissolve15

    n "Hump day!!!"

    "You hear your mom yell at you to hurry up."

    me "Ok ok!!! I'm coming!"

    "And so your day begins."

    jump d3classroom

label d3classroom:

    scene hallway with dissolve15

    play music classroom

    n "There's no signs of bullying today..."

    play sound bell volume 0.8

    n "Time to head to class!"

    scene classroom with dissolve15

    "You're greeted by Dr. Shah's friendly face."

    show teacher neutral with dissolve15

    t "Hello class!"

    show teacher explain

    t "Today we will be continuing our research in our groups."

    t "Before we get into groups today, I want to be handing out more tips for positive team building."

    show teacher neutral

    "Dr. Shah begins walking around handing everyone a piece of paper once again."

    hide teacher with moveoutleft1

    "Dr. Shah hands out the paper on your desk."

    me "Thank you, Dr. Shah."

    "After Dr. Shah hands out the paper to everyone, she goes back to the front of the class."

    show teacher explain with moveinright1

    t "Everyone, please read the tips silently as I read them out loud."

    t "1. Establish clear goals: Set clear, measurable goals that everyone on the team understands and is committed to achieving."

    t "2. Encourage open communication: Encourage open and honest communication among team members."

    t "This can include regular team meetings, one-on-one check-ins, and opportunities for feedback."

    t "3. Foster trust: Build trust among team members by being reliable, transparent, and demonstrating a willingness to listen and understand others' perspectives."

    t "4. Promote collaboration: Encourage collaboration by creating opportunities for team members to work together on projects and share their expertise and ideas."

    t "5. Provide feedback: Provide constructive feedback to team members, both positive and negative. This can help improve individual and team performance and build trust."

    show teacher neutral

    "As Dr. Shah explains this, you hope that Tyler is paying attention."

    "You also hope that he did his work..."

    t "Alright class, feel free to gather in your research groups."

    hide teacher with dissolve15

    n "Alright, time to get back into this group... the moment of truth..."

    "The class shuffled into their groups. You head to your group as well."

    show annie neutral at slightleft
    show tyler neutralb2 at slightright

    me "Hey guys, so what new research have you guys found?"

    show annie happy

    a "I researched about the [president]'s childhood."

    show annie neutral

    me "Awesome Annie!"

    me "I did some research about [president]'s inauguration."

    if nightAction2 == "research":

        show annie surprised

        me "I also found that [president] entered office in [presidentYear]!"
    
        show annie neutral

    me "What about you, Tyler?"

    if not tylerWillDoWork:

        show tyler heheb2
        show annie bruh

        b "I didn't do the research."

        n "Oh dear, not this again."

        n "He didn't do his research for the second day in a row???"

        n "This is getting ridiculous. What should I do??"

        menu:

            "What should I do??"

            "Accept it and let it slide":

                me "Ummm... ok... I see... well, I guess maybe that should be fine then since Annie and I did some research for now..."

                me "I guess for now we can maybe start the presentation slides?"

                show annie think

                a "Sure... I can start by creating a document."

                "You and Annie make eye contact fully knowing this is so unfair, but you don't want to escalate things and decide it might just be for the better and let it slide."

                "Maybe Tyler will do his work for tomorrow..."

            "Lash out":

                $ tylerPoints = tylerPoints - 1

                show tyler surprisedb2
                show annie surprised

                me "Tyler, you didn't do your work yesterday and then you show up today in class without your work AGAIN??"

                me "As if one time wasn't enough, you really didn't bother to do your work again??"

                show tyler madb2

                b "Hey, watch what you're saying."

                me "Annie and I have been consistently doing our work, so why can't you put in the same effort, especially when this is a group project??"

                show annie embarrassed

                a "Hey [name], I think you should tone it down a bit. I understand you are angry but maybe we should take some deep breaths first."

                b "Yeah, what's the matter with you anyway!? You better not talk to me like that again or else who knows what I'll do to you."

                n "Oh man... maybe I took it too far... I lashed out based on my emotions too fast. My anger took over but I should try to at least talk it out."

                me "Ok, my bad for reacting too fast."

                me "I was feeling a bit angry and frustrated that you didn't do your share of work..."
                
                me "...but would really appreciate it if you can put in some effort for our group project as well."

                show tyler bruhb2

                b "Whatever."

                a "How about we start trying to create the powerpoint slides?"

                me "Sure, let's do that."

            "Ask why he hasn't done his work":

                $ tylerPoints = tylerPoints + 1

                show tyler neutralb2
                show annie neutral

                me "Hmm... Tyler, is there a reason that you weren't able to complete your research?"

                b "Uh... I just wasn't able to get to it, ok..."

                me "Ok, just wanted to check in since we are a team and we should be working together on this section."

                me "I want to make sure you are able to have the resources to complete your part of the research."

                show tyler thinkb2

                b "... I mean, just some stuff happening at home that distracted me but it's whatever."

                b "I guess I'll try to get some research done tomorrow or something..."

                me "No worries, and you definitely don't have to talk more about it if you don't want to but thanks for being honest with us! We appreciate that."

                b "Yeah whatever..."

                show annie happy

                a "Hey [name], that was a really nice approach you took for this situation!"

                n "I'm glad I got to hear more about Tyler's side."

                n "Seems like there's some stuff going on and maybe I should try to be more understanding of his situation."

                show annie neutral
                show tyler neutralb2

                me "Alright, well how about for tomorrow we each take another section to do some research on?"

                show annie happy

                a "That sounds great, will do!"

                show annie neutral
                
                "Sure..."
            
    else:

        b "Yeah, here's my research."

        b "Tyler hands over a crumpled piece of paper with a couple sentences written on it."

        me "Great, thanks for doing the research Tyler! Do you mind if I take a quick look at it?"

        show tyler thinkb2

        b "Sure, I don't care."

        "You take the paper Tyler handed to you and read through his notes."

        "You notice that some of the information seems to be wrong and not as detailed."

        n "Hmm... he definitely did do some work but seems pretty low effort."

        n "What should I do about this?"

        menu:

            "What should I do about this?"

            "Offer constructive feedback":

                $ tylerPoints = tylerPoints - 1
                $ projectPoints = projectPoints + 1

                me "What you have seems to be great so far! I'm noticing here that you wrote that [president] was the 10th president..."

                if nightAction1 == "research":

                    me "... but I found that he was the [presidentNum] president."
                
                else:

                    show annie think

                    a "Yea, I don't think that's what we learned from History class..."

                    show annie neutral

                me "Also, you wrote about [president]'s legacy, but some more details would be helpful."

                show tyler bruhb2
                show annie surprised

                b "Did I ask for your opinion?!"

                me "Uhh... I mean I was just trying to give you some helpful feedback..."

                show tyler thinkb2

                b "Whatever, I didn't ask for you to help me anyway."

                me "Uh oh... seems like my feedback irritated Tyler..."

                me "...but hopefully he can take what I said into consideration for the next part of the project..."

                show annie embarrassed
                show tyler neutralb2

                a "How about we get started on the presentation with the research we all brought today?"

                show annie neutral
                show tyler bruhb2

                me "Sure, that works!"

            "Give honest feedback":

                $ tylerPoints = tylerPoints - 1

                me "What you have seems to be great so far! But I'm kind of noticing that the structure of your notes is kind of ugly..."

                show tyler madb2
                show annie surprised

                b "What did you just say about my work?!"

                me "Well I mean... it's pretty messy to look at and hard to follow. Maybe you should try rewriting it?"

                b "Hey why don't you just shut up if you're not even going to be helpful."

                n "Yikes... maybe I should have provided him with more helpful feedback but it seems like he's pretty mad right now..."

                n "...maybe I'll stop here..."

                show annie embarrassed

                a "Hey guys, how about we get started on the presentation with the research we all brought today?"

                show tyler bruhb2

                me "Sure, that works!"

            "Just accept it as it is":

                $ tylerPoints = tylerPoints + 1

                n "Even though it doesn't seem that great of a job, maybe I'll just accept it as it is because at least he did some work unlike yesterday."

                show annie embarrassed

                a "(whispering to you) Hey, Tyler's research is so messy and pretty sure he's got inaccurate information..."

                me "(whispering to Annie) Yeah I agree... but at least he did research today? Maybe this means it will get better from now on?"

                a "(whispering to you) Maybe... let's just move on to making the presentation slides now then I guess..."

                show annie neutral

                me "Ok great, let's move onto the presentation slides then."

                a "Sure, I'll get started with creating the slides!"

                "You don't feel that confident that Tyler's research will be helpful in your project... but maybe tomorrow will be a better work day?"

    show annie neutral
    show tyler neutralb2

    play sound bell volume 0.8

    a "Ok everyone, do your parts tonight and let's meet up tomorrow again."

    "Once again, another day of Dr. Shah's class is over. You hope tomorrow will be better..."

    jump d3lunch

label d3lunch:

    scene lunchroom with dissolve15

    "It's finally lunch time!"

    "You were so starving so you quickly went to the cafeteria."

    "Suddenly, you spot Tyler sitting alone at a table, his head buried in his arms."

    show tyler sadb2

    "Tyler..."

    "...is crying!!!"

    n "Why is Tyler crying there? He seems to be very sad."

    "What are you going to do?"

    menu:

        "What are you going to do?"

        "Ignore":

            n "Is something going on with Tyler??"

            n "Forget it! It's none of my business! I'd rather not bother with him."

            "You quickly pass by Tyler's table and find a table that is far from Tyler to sit."

            "You rush to finish lunch as you are starving and then exit the cafeteria afterwards."
        
        "Approach Tyler":

            if tylerPoints <= -2:

                $ tylerPoints = tylerPoints - 1

                "You tap Tyler on his shoulder."

                me "Hey, Tyler. Are you okay?"

                show tyler surprisedb2

                b "Huh, [name]? Why are you here?"

                show tyler madb2
                
                b "Just leave me alone!"

                "You notice Tyler quickly wiping his tears. He seems to not want you to see him crying."

                me "You think I really care much about you?"

                b "So why are you here? What do you want to know about me? Are you here to laugh at me?"

                me "No... I just wanted to see-"

                show tyler kindasadb2

                b "Just leave me alone."

                me "But-"

                show tyler madb2

                b "LEAVE."

                "You quickly leave Tyler and sit at another table."

                hide tyler

                "Since you are starving, you rush to finish lunch and then exit the cafeteria afterwards."
            
            elif tylerPoints <= 1:

                $ tylerPoints = tylerPoints + 1

                "You tap Tyler on his shoulder."

                me "Hey, Tyler. Are you okay?"

                show tyler kindasadb2

                b "Huh? Yeah, I'm fine. Why are you here?"

                "Tyler quickly wiped his tears. He seems to not want you to see him crying."

                me "You don't seem fine. I just wanted to see what was up."

                show tyler embarrassedb2

                b "uh..."

                me "After all, we are group mates. I also want to make sure you are fine now."
                
                me "You look so upset. Is there anything or anyone bothering you?"

                show tyler kindasadb2

                b "It's nothing. Just some stupid stuff happening at my home."

                me "Oh no! Are you okay!? If you need anyone to talk to, I am here."

                show tyler heheb2

                b "Thanks, but don't worry about it."
                
                show tyler smileb2

                b "You should go eat lunch."

                "You leave Tyler as he seems to want to be alone and sit at another table."

                "Since you are starving, you rush to finish lunch and then exit the cafeteria afterwards."

            else:

                $ tylerStory = True

                $ tylerPoints = tylerPoints + 2

                "You tap Tyler on his shoulder."

                me "Hey, Tyler. Are you okay?"

                show tyler kindasadb2

                b "Huh? Yeah, I'm fine. Why are you here?"

                "Tyler quickly wiped his tears. He seems to not want you to see him crying."

                me "You don't seem fine. I just wanted to see what was up."

                show tyler embarrassedb2

                b "uh..."

                me "After all, we are group mates. I also want to make sure you are fine now."
                
                me "You look so upset. Is there anything or anyone bothering you?"

                show tyler kindasadb2

                b "..."

                b "I never planned to tell this to anybody..."

                b "...but since you asked and are nice to me..."

                b "It was my Dad. He has a drinking problem."

                show tyler sadb2

                b "Last night he came home drunk and began to shout at my mum and me. I was so scared so I ran to my bedroom and locked my room."

                b "But, my mom... He kept hitting my mom."

                n "Woah! Tyler's Dad hit his mom!? Is this the first time or has this been happening for a long time?"

                show tyler kindasadb2

                b "This is also where my bruise came from. Not from a fight with the other kids. But from my Dad."

                me "Tyler... I'm so sorry to hear this. You must have suffered a lot."

                me "It's not your responsibility to fix everything. You should definitely tell someone, like a teacher or counselor. They can help you and your family."

                me "If you ever need someone to talk to, I am a good listener too."

                show tyler smileb2

                b "Thanks, [name]. I didn't think anyone would care. No one likes me anyway."

                me "Of course I care. You're not alone, Tyler."

                show tyler happyb2

                b "I appreciate this. Really. After all the crap I've pulled, you still want to do this for me."
                
                show tyler smileb2

                b "You should go eat lunch."

                "You leave Tyler as he seems to want to be alone and sit at another table."

                "Since you are starving, you rush to finish lunch and then exit the cafeteria afterwards."
    
    stop music fadeout 1.0

    jump d3bedroom

label d3bedroom:

    scene bedroom with dissolve15

    play music bedroom

    queue sound [opendoor, closedoor]

    "After a long day at school and a nice dinner, you return to your room."

    "You recall the events that happened at school today."

    if not tylerWillDoWork:

        "How are you feeling about the fact that Tyler didn't do work?"

        menu:

            "How are you feeling about the fact that Tyler didn't do work?"

            "Worried":

                n "What is going to happen for the presentation?"

                n "Tyler hasn't done enough research, so how will we be able to have enough information to present?"

            "Indifferent":

                n "I mean, ultimately it's Tyler's own fault for not doing his research."

                n "I guess there's nothing we can really do about it at this point. I'll just take whatever grade Dr. Shah gives us ..."

            "Angry":

                n "Why does he keep thinking he can get away with not doing his work?!"

                n "It's so frustrating that we have to carry his load."
        
    else:

        "You think back to class today and how Tyler did his work today. How are you feeling based on today's class?"

        menu:

            "How are you feeling based on today's class?"

            "Indifferent":

                n "I mean... he's just doing the bare minimum."

                n "There's not really much to congratulate him on when Annie and I have been doing the same thing."

            "Happy":

                n "It's so great to see Tyler participating in our group project!"

                n "I'm happy to see his progress in this project even if it's just a little bit."

            "Suspicious":

                n "I wonder what made him actually do his work..."

                n "Does this mean he will actually be a helpful team member?"

    "But then you think back to when you saw Tyler crying in the cafeteria."

    if not tylerStory:

        "Although you didn't talk much to him, you can't help but have a few thoughts."

        "What are you thinking about after seeing Tyler like that?"

        menu:

            "What are you thinking about after seeing Tyler like that?"

            "Worried":

                n "I wonder why he was crying like that... he looked so sad..."

                n "Should I have talked more with Tyler? I hope he is ok..."

            "Surprised":

                n "It is very unexpected seeing Tyler like that..."

                n "It was surprising to see Tyler express emotions like sadness."

            "Satisfied":

                n "It was oddly relieving seeing Tyler like that..."

                n "Serves him right since he's always being mean to other people."
    
    else:

        "Tyler seems to be going through a lot and you can't help but keep replaying your discussion you had with Tyler."

        "How are you feeling based on your interaction with Tyler?"

        menu:

            "How are you feeling based on your interaction with Tyler?"

            "Worried":

                n "Tyler has been through so much, I hope he is feeling ok."

                n "I am now worried about how he is going to be when he is home."

            "Understanding":

                n "I can now understand some of Tyler's behavior because of what's been happening back at home."

                n "I should also be more understanding of his circumstances like when he doesn't do good research because of what he is going through."

            "Guilty":

                n "Tyler had been going through so much and I kept judging him based on how he was acting towards other people, without even knowing there would be things going on behind the scenes for him."

                n "I feel so guilty for making a judgment about him without properly understanding his side."
    
    "After reflecting on the events from today, you decide it's time to wrap up for tonight."

    "You still have some work left to do, but you also want to play a round of Minecraft before sleeping."

    "What do you choose to do?"

    menu:

        "Work on your presentation":

            $ projectPoints = projectPoints + 1

            scene computer with pixellate

            "You work a little bit on the presentation and sprinkle in a little bit more research."

            "As a result, you feel your efforts adding to the quality of your project!"

        "Play Minecraft":

            "You decide to play a little bit of Minecraft!"

            scene computer with pixellate

            "Fortunately, this time, you are successful and find resources to upgrade your home and weapons."

            "You dig and discover iron, in which you smelt to create iron armor and swords."

            "After a bit of Minecraft, you log off for the night."

    scene bedroom with pixellate

    "It's quite late."
    
    "As the moon shines bright in the sky, you slowly drift off to sleep."

    stop music fadeout 1.0
    scene black
    with dissolve2

    jump d4start