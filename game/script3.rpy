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

    "You're greeting by Dr. Shah's friendly face."

    show teacher neutral with dissolve15

    t "Hello class!"

    show teacher explain

    t "Today we will be continuing our research in our groups."

    t "Before we get into groups today, I want to be handing out more tips for positive team building."

    show teacher neutral

    "Dr. Shah begins walking around handing everyone a piece of paper once again."

    hide teacher neutral with moveoutleft

    "Dr. Shah hands out the paper on your desk."

    me "Thank you, Dr. Shah."

    "After Dr. Shah hands out the paper to everyone, she goes back to the front of the class."

    show teacher explain with moveinright

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

    hide teacher neutral with dissolve15

    n "Alright, time to get back into this group... the moment of truth..."

    "The class shuffled into their groups. You head to your group as well."

    show annie neutral slightleft
    show tyler neutral slightright

    me "Hey guys, so what new research have you guys found?"

    show annie happy

    a "I researched about the [president]'s childhood."

    show annie neutral

    me "Awesome Annie!"

    me "I did some research about [president]'s inauguration."

    if nightAction == research:

        show annie surprised

        me "I also found that [president] entered office in [presidentYear]!"
    
        show annie neutral

    me "What about you, Tyler?"

    if not tylerWillDoWork:

        show tyler hehe
        show annie bruh

        b "I didn’t do the research."

        n "Oh dear, not this again."

        n "He didn’t do his research for the second day in a row???"

        n "This is getting ridiculous. What should I do??"

        menu:

            "What should I do??"

            "Accept it and let it slide":

                me "Ummm… ok… I see… well, I guess maybe that should be fine then since Annie and I did some research for now…"

                me "I guess for now we can maybe start the presentation slides?"

                show annie think

                a "Sure… I can start by creating a document."

                "You and Annie make eye contact fully knowing this is so unfair, but you don’t want to escalate things and decide it might just be for the better and let it slide."

                "Maybe Tyler will do his work for tomorrow…"

            "Lash out":

                show tyler surprised
                show annie surprised

                me "Tyler, you didn’t do your work yesterday and then you show up today in class without your work AGAIN??"

                me "As if one time wasn’t enough, you really didn’t bother to do your work again??"

                show tyler mad

                b "Hey, watch what you’re saying."

                me "Annie and I have been consistently doing our work, so why can’t you put in the same effort, especially when this is a group project??"

                show annie embarrassed

                a "Hey [name], I think you should tone it down a bit. I understand you are angry but maybe we should take some deep breaths first."

                b "Yeah, what’s the matter with you anyway!? You better not talk to me like that again or else who knows what I’ll do to you."

                n "Oh man… maybe I took it too far… I lashed out based on my emotions too fast. My anger took over but I should try to at least talk it out."

                me "Ok, my bad for reacting too fast."

                me "I was feeling a bit angry and frustrated that you didn’t do your share of work..."
                
                me "...but would really appreciate it if you can put in some effort for our group project as well."

                show tyler bruh

                b "Whatever."

                a "How about we start trying to create the powerpoint slides?"

                me "Sure, let’s do that."

            "Ask why he hasn’t done his work":

                show tyler neutral
                show annie neutral

                me "Hmm… Tyler, is there a reason that you weren’t able to complete your research?"

                b "Uh… I just wasn’t able to get to it, ok…"

                me "Ok, just wanted to check in since we are a team and we should be working together on this section."

                me "I want to make sure you are able to have the resources to complete your part of the research."

                show tyler think

                b "… I mean, just some stuff happening at home that distracted me but it’s whatever."

                b "I guess I’ll try to get some research done tomorrow or something…"

                me "No worries, and you definitely don’t have to talk more about it if you don’t want to but thanks for being honest with us! We appreciate that."

                b "Yeah whatever…"

                show annie happy

                a "Hey [name], that was a really nice approach you took for this situation!"

                n "I’m glad I got to hear more about Tyler’s side."

                n "Seems like there’s some stuff going on and maybe I should try to be more understanding of his situation."

                show annie neutral
                show tyler neutral

                me "Alright, well how about for tomorrow we each take another section to do some research on?"

                show annie happy

                a "That sounds great, will do!"

                show annie neutral
                
                "Sure…"
            
    else:

        b "Yeah, here’s my research."

        b "Tyler hands over a crumpled piece of paper with a couple sentences written on it."

        me "Great, thanks for doing the research Tyler! Do you mind if I take a quick look at it?"

        show tyler think

        b "Sure, I don’t care."

        "You take the paper Tyler handed to you and read through his notes."

        "You notice that some of the information seem to be wrong and not as detailed."

        n "Hmm… he definitely did do some work but seems pretty low effort."

        n "What should I do about this?"

        menu:

            "What should I do about this?"

            "Offer constructive feedback":

                me "What you have seems to be great so far! I’m noticing here that you wrote that [president] was the 10th president..."

                me "... but he was actually the [presidentNum] president."

                me "Also, you wrote about [president]’s legacy, but some more details would be helpful."

                show tyler bruh
                show annie surprised

                b "Did I ask for your opinion?!"

                me "Uhh… I mean I was just trying to give you some helpful feedback…"

                show tyler think

                b "Whatever, I didn’t ask for you to help me anyway."

                me "Uh oh… seems like my feedback irritated Tyler…"

                me "…but hopefully he can take what I said into consideration for the next part of the project…"

                show annie embarrassed
                show tyler neutral

                a "How about we get started on the presentation with the research we all brought today?"

                show annie neutral
                show tyler bruh

                me "Sure, that works!"

            "Give honest feedback":

                me "What you have seems to be great so far! But I’m kind of noticing that the structure of your notes is kind of ugly…"

                show tyler mad
                show annie surprised

                b "What did you just say about my work?!"

                me "Well I mean… it’s pretty messy to look at and hard to follow. Maybe you should try rewriting it?"

                b "Hey why don’t you just shut up if you’re not even going to be helpful."

                n "Yikes… maybe I should have provided him with more helpful feedback but it seems like he’s pretty mad right now…"

                n "...maybe I’ll stop here…"

                show annie embarrassed

                a "Hey guys, how about we get started on the presentation with the research we all brought today?"

                show tyler bruh

                me "Sure, that works!"

            "Just accept it as it is":

                n "Even though it doesn’t seem that great of a job, maybe I’ll just accept it as it is because at least he did some work unlike yesterday."

                show annie embarrassed

                a "(whispering to you) Hey, Tyler’s research is so messy and pretty sure he’s got inaccurate information…"

                me "(whispering to Annie) Yeah I agree… but at least he did research today? Maybe this means it will get better from now on?"

                a "(whispering to you) Maybe… let’s just move on to making the presentation slides now then I guess…"

                show annie neutral

                me "Ok great, let’s move onto the presentation slides then."

                a "Sure, I’ll get started with creating the slides!"

                "You don’t feel that confident that Tyler’s research will be helpful in your project… but maybe tomorrow will be a better work day?"

    show annie neutral
    show tyler neutral

    play sound bell volume 0.8

    a "Ok everyone, do your parts tonight and let's meet up tomorrow again."

    "Once again, another day of Dr. Shah's class is over. You hope tomorrow will be better..."