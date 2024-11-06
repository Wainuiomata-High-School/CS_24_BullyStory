victim_story = {
    1: {
        'text': (
            "Zach is starting high school. He feels nervous, awkward, and out of place. On his first day, he meets Bryan, a "
            "popular student who quickly notices Zach’s quiet demeanor."
        ),
        'choices': {
            1: {'text': "Try to avoid Bryan as much as possible", 'next_node': 2},
            2: {'text': "Pretend to laugh along with Bryan’s jokes", 'next_node': 3}
        },
        'image' :   'images/Node_1.webp'
    },

    2: {
        'text': (
            "Zach tries to avoid Bryan, but Bryan seems to find him in the hallways and at recess. The bullying begins with "
            "insults and teasing about his awkwardness. Zach doesn’t tell his parents, choosing to keep his problems hidden."
        ),
        'choices': {
            1: {'text': "Continue avoiding Bryan", 'next_node': 4},
            2: {'text': "Stand up to Bryan", 'next_node': 5}
        },
        'image' : 'images/bullygamescene.png'
    },

    3: {
        'text': (
            "Zach pretends to laugh along with Bryan’s jokes, hoping to fit in, but it only makes things worse. Bryan starts "
            "to bully Zach more openly, calling him names and spreading rumors. Zach feels trapped."
        ),
        'choices': {
            1: {'text': "Talk to his parents about it", 'next_node': 6},
            2: {'text': "Keep hiding the bullying from his family", 'next_node': 7}
        }
    },

    4: {
        'text': (
            "Zach continues to avoid Bryan, but Bryan finds new ways to torment him. Bryan and his friends start cyberbullying "
            "Zach by creating fake profiles and catfishing him online. Zach’s home life is affected as he withdraws from his "
            "parents, pretending everything is fine."
        ),
        'choices': {
            1: {'text': "Seek help from the school counselor", 'next_node': 8},
            2: {'text': "Stay silent and try to endure the bullying", 'next_node': 9}
        }
    },

    5: {
        'text': (
            "Zach stands up to Bryan, but Bryan reacts aggressively. Zach feels more isolated and starts developing symptoms "
            "of anxiety and depression. He begins to dissociate, feeling disconnected from his surroundings."
        ),
        'choices': {
            1: {'text': "Try to ignore the bullying", 'next_node': 10},
            2: {'text': "Seek support from a friend", 'next_node': 11}
        }
    },

    6: {
        'text': (
            "Zach tells his parents about the bullying. They try to help by contacting the school, but the situation only "
            "escalates. Bryan finds out that Zach told on him, and the bullying intensifies. Zach begins to feel like there’s "
            "no escape."
        ),
        'choices': {
            1: {'text': "Talk to a teacher directly", 'next_node': 12},
            2: {'text': "Withdraw and isolate himself", 'next_node': 13}
        }
    },

    7: {
        'text': (
            "Zach continues to hide the bullying from his parents, putting on a mask at home. He begins struggling with eating "
            "disorders and suicidal ideation, feeling overwhelmed and unable to cope."
        ),
        'choices': {
            1: {'text': "Start smoking to cope with the anxiety", 'next_node': 14},
            2: {'text': "Try to keep going despite the mounting pressure", 'next_node': 15}
        }
    },

    8: {
        'text': (
            "Zach seeks help from the school counselor. While the counselor tries to provide advice, it feels inadequate. The "
            "bullying continues, and Zach starts smoking weed to cope with the stress and anxiety."
        ),
        'choices': {
            1: {'text': "Keep seeing the counselor", 'next_node': 16},
            2: {'text': "Stop seeking help and rely on weed to manage", 'next_node': 17}
        }
    },

    9: {
        'text': (
            "Zach chooses to stay silent, hiding his pain. The bullying becomes a constant in his life, and his mental health "
            "deteriorates further. He begins to dissociate regularly and contemplates suicide more frequently."
        ),
        'choices': {
            1: {'text': "Start drinking to numb the pain", 'next_node': 18},
            2: {'text': "Keep enduring without reaching out for help", 'next_node': 19}
        }
    },

    10: {
        'text': (
            "Zach tries to ignore the bullying, but Bryan doesn’t let up. The constant ridicule starts to affect Zach’s "
            "academic performance, and he feels more isolated than ever."
        ),
        'choices': {
            1: {'text': "Talk to a teacher or school counselor", 'next_node': 20},
            2: {'text': "Continue trying to avoid Bryan", 'next_node': 21}
        }
    },

    11: {
        'text': (
            "Zach opens up to a friend about the bullying. While his friend offers some support, it doesn’t stop Bryan from "
            "continuing the abuse. Zach still feels alone and overwhelmed."
        ),
        'choices': {
            1: {'text': "Seek help from his parents", 'next_node': 22},
            2: {'text': "Try to deal with the situation on his own", 'next_node': 23}
        }
    },

    12: {
        'text': (
            "Zach talks to a teacher about the bullying. The teacher takes some action, but it only makes Bryan more subtle "
            "with his bullying. Zach still feels trapped and begins to lose hope."
        ),
        'choices': {
            1: {'text': "Seek help outside of school", 'next_node': 24},
            2: {'text': "Withdraw and isolate himself further", 'next_node': 25}
        }
    },

    13: {
        'text': (
            "Zach withdraws completely from social life. He stops interacting with his friends and family, and his grades "
            "begin to slip. His parents start to worry, but Zach keeps pretending everything is fine."
        ),
        'choices': {
            1: {'text': "Try to get his grades back on track", 'next_node': 26},
            2: {'text': "Ignore his schoolwork and continue isolating", 'next_node': 27}
        }
    },

    14: {
        'text': (
            "Zach starts smoking cigarettes to cope with his anxiety. It becomes a regular habit, providing him with a momentary "
            "escape from the stress. However, his mental health continues to worsen."
        ),
        'choices': {
            1: {'text': "Keep smoking to manage his anxiety", 'next_node': 28},
            2: {'text': "Try to find healthier ways to cope", 'next_node': 29}
        }
    },

    15: {
        'text': (
            "Zach tries to keep going despite the immense pressure he’s feeling. The bullying doesn’t stop, and his mental health "
            "continues to decline. He struggles to maintain a normal facade in front of his family."
        ),
        'choices': {
            1: {'text': "Seek professional help for his anxiety", 'next_node': 30},
            2: {'text': "Continue hiding his struggles from everyone", 'next_node': 31}
        }
    },

    16: {
        'text': (
            "Zach continues to see the school counselor, but the progress is slow. He still feels the weight of the bullying and "
            "the isolation. His reliance on weed grows as he struggles to deal with his emotions."
        ),
        'choices': {
            1: {'text': "Try to reduce his weed consumption", 'next_node': 32},
            2: {'text': "Continue using weed as a coping mechanism", 'next_node': 33}
        }
    },

    17: {
        'text': (
            "Zach stops seeking help from the counselor and begins using weed more frequently to cope. His parents notice his "
            "distant behavior, but Zach denies that anything is wrong. His mental health worsens as he becomes more detached."
        ),
        'choices': {
            1: {'text': "Consider going back to the counselor", 'next_node': 34},
            2: {'text': "Continue avoiding professional help", 'next_node': 35}
        }
    },

    18: {
        'text': (
            "Zach starts drinking to numb the pain. At first, it helps him forget about the bullying and his anxiety, but soon he "
            "finds himself drinking more frequently. His grades start slipping further."
        ),
        'choices': {
            1: {'text': "Recognize he’s developing a drinking problem", 'next_node': 36},
            2: {'text': "Keep drinking to cope", 'next_node': 37}
        }
    },

    19: {
        'text': (
            "Zach continues enduring the bullying without reaching out for help. His dissociation becomes more frequent, and he "
            "often feels disconnected from reality. He contemplates suicide more regularly."
        ),
        'choices': {
            1: {'text': "Reach out to someone before it's too late", 'next_node': 38},
            2: {'text': "Keep silent and try to deal with it on his own", 'next_node': 39}
        }
    },

    20: {
        'text': (
            "Zach talks to the school counselor about the bullying. They try to intervene, but Bryan continues bullying Zach in "
            "more subtle ways. Zach’s mental health continues to spiral."
        ),
        'choices': {
            1: {'text': "Focus on self-care to improve his mental health", 'next_node': 40},
            2: {'text': "Continue struggling without addressing his feelings", 'next_node': 41}
        }
    },

    21: {
        'text': (
            "Zach keeps avoiding Bryan, but the constant bullying wears him down. He isolates himself from his peers and his family, "
            "feeling like there’s no escape from the situation."
        ),
        'choices': {
            1: {'text': "Consider leaving school to escape the bullying", 'next_node': 42},
            2: {'text': "Try to keep enduring despite the pain", 'next_node': 43}
        }
    },

    22: {
        'text': (
            "Zach opens up to his parents about the bullying. They are supportive and try to help, but the school is slow to take action. "
            "Bryan’s bullying continues, and Zach’s mental health continues to decline."
        ),
        'choices': {
            1: {'text': "Consider switching schools", 'next_node': 44},
            2: {'text': "Stay and try to deal with the situation", 'next_node': 45}
        }
    },

    23: {
        'text': (
            "Zach tries to deal with the situation on his own, but the weight of the bullying is too much to handle. He feels trapped "
            "and isolated, with no end in sight."
        ),
        'choices': {
            1: {'text': "Seek help from an external support group", 'next_node': 46},
            2: {'text': "Continue bottling up his emotions", 'next_node': 47}
        }
    },

    24: {
        'text': (
            "Zach seeks help from an external counselor. The process is slow, but he starts to make some progress in dealing with his "
            "anxiety and depression. However, the bullying continues at school."
        ),
        'choices': {
            1: {'text': "Continue therapy and try to endure the bullying", 'next_node': 48},
            2: {'text': "Consider changing schools to start fresh", 'next_node': 49}
        }
    },

    25: {
        'text': (
            "Zach isolates himself further, shutting out friends and family. His mental health deteriorates to the point where he "
            "feels completely numb to the world around him."
        ),
        'choices': {
            1: {'text': "Seek professional help for his dissociation", 'next_node': 50},
            2: {'text': "Keep retreating into his dissociative episodes", 'next_node': 51}
        }
    },
    26: {
        'text': (
            "Zach tries to get his grades back on track, but the stress from the bullying and his deteriorating mental health "
            "makes it difficult to focus. He spends more time dissociating and daydreaming to escape reality."
        ),
        'choices': {
            1: {'text': "Seek academic support from a teacher", 'next_node': 52},
            2: {'text': "Continue to struggle in silence", 'next_node': 53}
        }
    },

    27: {
        'text': (
            "Zach ignores his schoolwork, focusing instead on surviving each day. His grades continue to slip, and his parents start "
            "to notice. They pressure him to improve, but he feels overwhelmed."
        ),
        'choices': {
            1: {'text': "Open up to his parents about how overwhelmed he feels", 'next_node': 54},
            2: {'text': "Keep his feelings hidden and ignore their concerns", 'next_node': 55}
        }
    },

    28: {
        'text': (
            "Zach keeps smoking to manage his anxiety, but it doesn't address the root of his problems. He feels like he's losing control, "
            "and his dependence on cigarettes becomes another source of anxiety."
        ),
        'choices': {
            1: {'text': "Try to quit smoking", 'next_node': 56},
            2: {'text': "Increase his smoking to cope", 'next_node': 57}
        }
    },

    29: {
        'text': (
            "Zach tries to find healthier ways to cope, but it’s difficult to break away from his established habits. He starts exercising "
            "to release some stress, but the bullying at school continues."
        ),
        'choices': {
            1: {'text': "Focus more on exercise and healthy outlets", 'next_node': 58},
            2: {'text': "Fall back into old habits like smoking", 'next_node': 59}
        }
    },

    30: {
        'text': (
            "Zach seeks professional help for his anxiety. A therapist helps him explore his feelings, but it's a slow and painful process. "
            "Meanwhile, the bullying continues to affect his daily life."
        ),
        'choices': {
            1: {'text': "Commit fully to therapy", 'next_node': 60},
            2: {'text': "Give up on therapy when it feels too overwhelming", 'next_node': 61}
        }
    },

    31: {
        'text': (
            "Zach continues hiding his struggles from everyone. His eating disorder becomes more severe, and he avoids meals whenever "
            "possible. He’s losing weight rapidly, but no one seems to notice."
        ),
        'choices': {
            1: {'text': "Try to eat and take care of himself", 'next_node': 62},
            2: {'text': "Continue restricting food to feel in control", 'next_node': 63}
        }
    },

    32: {
        'text': (
            "Zach tries to reduce his weed consumption, but the stress from school and home makes it difficult. He often finds himself "
            "turning back to it when things feel overwhelming."
        ),
        'choices': {
            1: {'text': "Commit to quitting weed", 'next_node': 64},
            2: {'text': "Continue using weed as a way to cope", 'next_node': 65}
        }
    },

    33: {
        'text': (
            "Zach continues using weed as a coping mechanism. It helps him escape the harsh reality of his life, but he begins to lose focus "
            "on his schoolwork and relationships."
        ),
        'choices': {
            1: {'text': "Consider seeking help for his addiction", 'next_node': 66},
            2: {'text': "Keep using weed to numb the pain", 'next_node': 67}
        }
    },

    34: {
        'text': (
            "Zach considers going back to the counselor, but he feels too ashamed to admit how badly things have gotten. His dissociation "
            "becomes more frequent, and he starts having trouble remembering entire days."
        ),
        'choices': {
            1: {'text': "Return to the counselor", 'next_node': 68},
            2: {'text': "Keep bottling everything up", 'next_node': 69}
        }
    },

    35: {
        'text': (
            "Zach avoids returning to the counselor and continues spiraling. His mental health deteriorates, and he starts missing more "
            "school. His parents are concerned, but Zach pushes them away."
        ),
        'choices': {
            1: {'text': "Talk to his parents about how he’s feeling", 'next_node': 70},
            2: {'text': "Shut his parents out completely", 'next_node': 71}
        }
    },

    36: {
        'text': (
            "Zach recognizes that he’s developing a drinking problem. He tries to cut back, but the stress and bullying make it hard. His "
            "grades continue to drop, and he feels trapped in a vicious cycle."
        ),
        'choices': {
            1: {'text': "Seek help for his drinking", 'next_node': 72},
            2: {'text': "Continue drinking despite the consequences", 'next_node': 73}
        }
    },

    37: {
        'text': (
            "Zach keeps drinking to cope, but it’s starting to affect his relationships with his family and friends. He feels distant from "
            "everyone and wonders if things will ever get better."
        ),
        'choices': {
            1: {'text': "Try to repair his relationships", 'next_node': 74},
            2: {'text': "Keep isolating himself", 'next_node': 75}
        }
    },

    38: {
        'text': (
            "Zach finally reaches out to a friend for help. They encourage him to talk to a professional, and Zach starts seeing a therapist. "
            "The progress is slow, but Zach starts to feel a glimmer of hope."
        ),
        'choices': {
            1: {'text': "Keep going to therapy", 'next_node': 76},
            2: {'text': "Give up when therapy becomes too hard", 'next_node': 77}
        }
    },

    39: {
        'text': (
            "Zach keeps silent, continuing to deal with everything on his own. His suicidal ideation becomes more intense, and he feels like "
            "he’s running out of options."
        ),
        'choices': {
            1: {'text': "Consider seeking help", 'next_node': 78},
            2: {'text': "Contemplate acting on his suicidal thoughts", 'next_node': 79}
        }
    },

    40: {
        'text': (
            "Zach decides to focus on self-care. He tries to develop better coping mechanisms, like journaling and meditation, but it’s hard "
            "to maintain with the constant bullying."
        ),
        'choices': {
            1: {'text': "Keep working on self-care", 'next_node': 80},
            2: {'text': "Give up and let the bullying take over his life", 'next_node': 81}
        }
    },

    41: {
        'text': (
            "Zach continues to struggle without addressing his feelings. His mental health continues to decline, and he begins to lose all "
            "motivation for school and socializing."
        ),
        'choices': {
            1: {'text': "Reach out to someone for support", 'next_node': 82},
            2: {'text': "Keep withdrawing from everyone", 'next_node': 83}
        }
    },

    42: {
        'text': (
            "Zach considers leaving school to escape the bullying. He feels like he can’t handle another day, but he worries about what his "
            "parents will think."
        ),
        'choices': {
            1: {'text': "Leave school to focus on his mental health", 'next_node': 84},
            2: {'text': "Stay and try to push through", 'next_node': 85}
        }
    },

    43: {
        'text': (
            "Zach tries to keep enduring despite the pain, but his mental health continues to worsen. He feels like he’s suffocating, with no "
            "escape in sight."
        ),
        'choices': {
            1: {'text': "Seek professional help", 'next_node': 86},
            2: {'text': "Continue ignoring his feelings", 'next_node': 87}
        }
    },

    44: {
        'text': (
            "Zach considers switching schools, but the thought of starting over scares him. He wonders if things will be any different at "
            "another school, or if he’ll just encounter the same problems."
        ),
        'choices': {
            1: {'text': "Switch schools for a fresh start", 'next_node': 88},
            2: {'text': "Stay at his current school", 'next_node': 89}
        }
    },

    45: {
        'text': (
            "Zach decides to stay at his current school. He tries to find ways to cope with the bullying, but it continues to take a toll on "
            "his mental health."
        ),
        'choices': {
            1: {'text': "Seek help from a trusted adult", 'next_node': 90},
            2: {'text': "Keep dealing with it on his own", 'next_node': 91}
        }
    },

    46: {
        'text': (
            "Zach seeks help from an external support group. He starts to meet other people who have experienced bullying, and it helps him "
            "feel less alone."
        ),
        'choices': {
            1: {'text': "Continue attending support group meetings", 'next_node': 92},
            2: {'text': "Stop going when it feels too uncomfortable", 'next_node': 93}
        }
    },

    47: {
        'text': (
            "Zach continues bottling up his emotions. The weight of the bullying, combined with his anxiety and depression, makes it harder "
            "and harder for him to function."
        ),
        'choices': {
            1: {'text': "Finally seek help", 'next_node': 94},
            2: {'text': "Continue suffering in silence", 'next_node': 95}
        }
    },

    48: {
        'text': (
            "Zach continues therapy and tries to endure the bullying. It’s a long, painful process, but Zach is slowly starting to feel more "
            "in control of his emotions."
        ),
        'choices': {
            1: {'text': "Keep going to therapy", 'next_node': 96},
            2: {'text': "Give up on therapy", 'next_node': 97}
        }
    },

    49: {
        'text': (
            "Zach considers changing schools to start fresh. He feels hopeful about the possibility of a new beginning, but he’s also "
            "afraid of the unknown."
        ),
        'choices': {
            1: {'text': "Change schools", 'next_node': 98},
            2: {'text': "Stay where he is", 'next_node': 99}
        }
    },

    50: {
        'text': (
            "Zach seeks professional help for his dissociation. Therapy helps him recognize the signs of his dissociative episodes and "
            "teaches him grounding techniques to stay present. However, the bullying continues, and Zach struggles to apply these techniques "
            "in stressful situations."
        ),
        'choices': {
            1: {'text': "Focus more on applying therapy techniques at school", 'next_node': 100},
            2: {'text': "Stop attending therapy when it becomes too overwhelming", 'next_node': 101}
        }
    },

    51: {
        'text': (
            "Zach continues retreating into his dissociative episodes, using them as an escape from reality. His grades fall further, and "
            "his relationships with family and friends suffer. He begins to feel completely disconnected from his surroundings."
        ),
        'choices': {
            1: {'text': "Reach out to his parents for help", 'next_node': 102},
            2: {'text': "Try to deal with everything on his own", 'next_node': 103}
        }
    },

    52: {
        'text': (
            "Zach seeks academic support from a teacher. While his grades improve slightly, the bullying continues, and Zach still struggles "
            "with anxiety and dissociation. He feels like he’s fighting an uphill battle."
        ),
        'choices': {
            1: {'text': "Focus on his mental health over academics", 'next_node': 104},
            2: {'text': "Push through and try to balance everything", 'next_node': 105}
        }
    },

    53: {
        'text': (
            "Zach continues to struggle in silence. The bullying remains constant, and his mental health deteriorates further. He begins to "
            "lose hope, questioning whether things will ever get better."
        ),
        'choices': {
            1: {'text': "Seek help from a school counselor again", 'next_node': 106},
            2: {'text': "Continue to isolate himself from everyone", 'next_node': 107}
        }
    },

    54: {
        'text': (
            "Zach opens up to his parents about how overwhelmed he feels. They try to support him, but they don’t fully understand the depth "
            "of his mental health struggles. Zach feels a mixture of relief and frustration."
        ),
        'choices': {
            1: {'text': "Ask his parents to help find a better therapist", 'next_node': 108},
            2: {'text': "Keep trying to manage everything on his own", 'next_node': 109}
        }
    },

    55: {
        'text': (
            "Zach keeps his feelings hidden, ignoring his parents' concerns. His mental health worsens, and his dissociation becomes more "
            "frequent. He begins feeling like he’s losing touch with reality entirely."
        ),
        'choices': {
            1: {'text': "Start self-harming to feel something real", 'next_node': 110},
            2: {'text': "Try to stay grounded through journaling", 'next_node': 111}
        }
    },

    56: {
        'text': (
            "Zach tries to quit smoking but finds it difficult. The stress from school and bullying makes it almost impossible to quit, and "
            "he feels guilty about his continued reliance on cigarettes."
        ),
        'choices': {
            1: {'text': "Reach out to his school counselor for support", 'next_node': 112},
            2: {'text': "Keep trying to quit on his own", 'next_node': 113}
        }
    },

    57: {
        'text': (
            "Zach increases his smoking to cope with the overwhelming anxiety. His dependence on cigarettes grows, but it offers only "
            "temporary relief. The stress and dissociation continue to worsen."
        ),
        'choices': {
            1: {'text': "Try vaping as a substitute for cigarettes", 'next_node': 114},
            2: {'text': "Look for a healthier coping mechanism", 'next_node': 115}
        }
    },

    58: {
        'text': (
            "Zach starts focusing more on exercise and healthy outlets. He begins running in the mornings, which helps him clear his mind, "
            "but the bullying and stress at school persist."
        ),
        'choices': {
            1: {'text': "Join a sports team to stay active", 'next_node': 116},
            2: {'text': "Stick to solo activities like running", 'next_node': 117}
        }
    },

    59: {
        'text': (
            "Zach falls back into old habits like smoking. Despite his attempts to exercise, the constant stress from bullying wears him down, "
            "and he returns to unhealthy coping mechanisms."
        ),
        'choices': {
            1: {'text': "Try to quit smoking again", 'next_node': 118},
            2: {'text': "Accept that smoking is his only way to cope", 'next_node': 119}
        }
    },

    60: {
        'text': (
            "Zach commits fully to therapy. It’s a long and difficult process, but he begins to see progress. His dissociation becomes less "
            "frequent, and he learns to manage his anxiety better."
        ),
        'choices': {
            1: {'text': "Open up to his therapist about everything", 'next_node': 120},
            2: {'text': "Keep some of his struggles to himself", 'next_node': 121}
        }
    },

    61: {
        'text': (
            "Zach gives up on therapy when it feels too overwhelming. He stops attending sessions and returns to unhealthy coping mechanisms, "
            "like smoking and isolating himself from others."
        ),
        'choices': {
            1: {'text': "Try therapy again after a break", 'next_node': 122},
            2: {'text': "Stick to his own methods of coping", 'next_node': 123}
        }
    },

    62: {
        'text': (
            "Zach tries to eat and take care of himself, but his eating disorder worsens. He’s losing weight rapidly, and the bullying at "
            "school only exacerbates his body image issues."
        ),
        'choices': {
            1: {'text': "Talk to a nutritionist or therapist about his eating habits", 'next_node': 124},
            2: {'text': "Continue restricting his food intake", 'next_node': 125}
        }
    },

    63: {
        'text': (
            "Zach continues restricting his food to feel in control. The weight loss becomes severe, and his health starts to decline. His "
            "parents and teachers notice but feel unsure how to help."
        ),
        'choices': {
            1: {'text': "Admit that he needs help with his eating disorder", 'next_node': 126},
            2: {'text': "Keep hiding his eating disorder", 'next_node': 127}
        }
    },

    64: {
        'text': (
            "Zach commits to quitting weed and seeks support from his friends. The process is difficult, but he begins to feel more in control "
            "of his life."
        ),
        'choices': {
            1: {'text': "Stay away from friends who still smoke", 'next_node': 128},
            2: {'text': "Try to balance his social life with staying sober", 'next_node': 129}
        }
    },

    65: {
        'text': (
            "Zach continues using weed as a way to cope with the overwhelming stress. It becomes harder for him to focus on school or engage "
            "with his family, and his mental health declines further."
        ),
        'choices': {
            1: {'text': "Consider rehab to address his addiction", 'next_node': 130},
            2: {'text': "Keep using weed to numb his feelings", 'next_node': 131}
        }
    },
    

    66: {
        'text': (
            "Zach’s addiction to weed worsens. He starts skipping school more frequently and spends most of his days high, detached from "
            "the world. His parents confront him, but he shuts down, unwilling to acknowledge his problem."
        ),
        'choices': {
            1: {'text': "Finally admit to his parents that he needs help", 'next_node': 132},
            2: {'text': "Continue lying to his parents and avoid the issue", 'next_node': 133}
        }
    },

    67: {
        'text': (
            "Zach distances himself from his friends who still smoke weed. It’s a painful process, but he realizes he needs to be in control "
            "of his own health. His friends don’t understand, and he starts to feel isolated."
        ),
        'choices': {
            1: {'text': "Seek out new friendships with people who support his sobriety", 'next_node': 134},
            2: {'text': "Withdraw into himself, avoiding social situations altogether", 'next_node': 135}
        }
    },

    68: {
        'text': (
            "Zach attempts to balance his social life while staying sober. It’s challenging, as many of his friends don’t understand why he "
            "wants to quit. He constantly feels tempted, but he is determined to stay on track."
        ),
        'choices': {
            1: {'text': "Open up to his friends about his mental health struggles", 'next_node': 136},
            2: {'text': "Keep his struggles hidden and hope things improve on their own", 'next_node': 137}
        }
    },

    69: {
        'text': (
            "Zach admits that he needs professional help for his addiction. His parents find a rehab facility, and Zach begins the recovery "
            "process. It’s difficult, but he starts to see some hope for the first time in a while."
        ),
        'choices': {
            1: {'text': "Stay committed to the rehab process", 'next_node': 138},
            2: {'text': "Leave rehab early when things get tough", 'next_node': 139}
        }
    },

    70: {
        'text': (
            "Zach hides his addiction from his parents and continues using weed to cope. His grades plummet, and he’s in danger of failing "
            "the school year. His relationship with his family deteriorates further."
        ),
        'choices': {
            1: {'text': "Try to pull himself together and stop using weed on his own", 'next_node': 140},
            2: {'text': "Continue avoiding his responsibilities", 'next_node': 141}
        }
    },

    71: {
        'text': (
            "Zach begins feeling the physical effects of his eating disorder. His energy levels drop, and he starts feeling faint in class. "
            "Despite his worsening condition, Zach is reluctant to seek help, afraid of losing the one thing he can control."
        ),
        'choices': {
            1: {'text': "Confide in a teacher or counselor about his struggles", 'next_node': 142},
            2: {'text': "Keep his eating disorder hidden and push through the pain", 'next_node': 143}
        }
    },

    72: {
        'text': (
            "Zach’s health deteriorates further due to his eating disorder. He collapses during gym class and is rushed to the hospital. His "
            "parents are horrified when they learn the extent of his condition."
        ),
        'choices': {
            1: {'text': "Agree to go to inpatient treatment for his eating disorder", 'next_node': 144},
            2: {'text': "Resist treatment, insisting he can handle it on his own", 'next_node': 145}
        }
    },

    73: {
        'text': (
            "Zach opens up to a counselor about his eating disorder. The counselor encourages him to seek help and provides him with resources "
            "for recovery. Zach feels a sense of relief but is still uncertain about taking the next steps."
        ),
        'choices': {
            1: {'text': "Follow the counselor's advice and start recovery", 'next_node': 146},
            2: {'text': "Avoid taking action and continue down the same path", 'next_node': 147}
        }
    },

    74: {
        'text': (
            "Zach’s dissociation worsens as his mental health declines. He starts to feel disconnected from his body and emotions for longer "
            "periods of time, struggling to stay grounded. He begins losing touch with reality completely."
        ),
        'choices': {
            1: {'text': "Seek help from a mental health professional", 'next_node': 148},
            2: {'text': "Continue to isolate himself and live in a dissociated state", 'next_node': 149}
        }
    },

    75: {
        'text': (
            "Zach reaches out to a trusted teacher for help with his mental health. The teacher listens and helps Zach find a therapist who "
            "specializes in dissociation and trauma. It’s the first time Zach feels like someone truly understands him."
        ),
        'choices': {
            1: {'text': "Commit to therapy and make an effort to heal", 'next_node': 150},
            2: {'text': "Start therapy but remain skeptical and disengaged", 'next_node': 151}
        }
    },

    76: {
        'text': (
            "Zach’s dissociation reaches a breaking point. He no longer feels in control of his life and starts experiencing episodes where he "
            "can’t remember entire days. His friends and family become increasingly concerned."
        ),
        'choices': {
            1: {'text': "Tell his parents about his dissociation", 'next_node': 152},
            2: {'text': "Hide his condition and hope it goes away on its own", 'next_node': 153}
        }
    },

    77: {
        'text': (
            "Zach finally tells his parents about how severe his dissociation has become. They are supportive and help him find a specialist, "
            "but Zach still feels unsure if he’ll ever fully recover."
        ),
        'choices': {
            1: {'text': "Focus on his recovery with professional help", 'next_node': 154},
            2: {'text': "Resist the help, feeling that it's too late for him", 'next_node': 155}
        }
    },

    78: {
        'text': (
            "Zach keeps his dissociation hidden from everyone. He feels like he’s slipping further and further away from reality. Soon, it’s "
            "hard for him to distinguish between what’s real and what’s not."
        ),
        'choices': {
            #1: {'text': "Reach out for help before it’s too late", 'next_node': 156},
            #2: {'text': "Continue to withdraw from the world", 'next_node': 157}
        }
    },

    79: {
        'text': (
            "Zach feels overwhelmed by his emotions but knows he needs to take a step forward."
        ),
        'choices': {
           #1: {'text': "Reach out to a friend for support.", 'next_node': 133},
           #2: {'text': "Write in his journal to process his feelings.", 'next_node': 134}
        }
    },

    80: {
        'text': (
            "Zach confronts a bully at school, surprising himself with his courage."
        ),
        'choices': {
            #1: {'text': "Feel proud and empowered.", 'next_node': 135},
            #2: {'text': "Worry about potential retaliation.", 'next_node': 136}
        }
    },

    81: {
        'text': (
            "Zach has a heart-to-heart with his parents about his struggles."
        ),
        'choices': {
            #1: {'text': "Feel closer to them and supported.", 'next_node': 137},
            #2: {'text': "Still feel misunderstood and alone.", 'next_node': 138}
        }
    },

    82: {
        'text': (
            "Zach finds solace in a new hobby, allowing him to express himself creatively."
        ),
        'choices': {
            #1: {'text': "Dedicate more time to this hobby.", 'next_node': 139},
            #2: {'text': "Feel guilty for not focusing on his issues.", 'next_node': 140}
        }
    },

    83: {
        'text': (
            "Zach starts to feel a sense of belonging with a new group of friends."
        ),
        'choices': {
            #1: {'text': "Open up to them about his past.", 'next_node': 141},
            2: {'text': "Keep his struggles to himself for now.", 'next_node': 142}
        }
    },

    84: {
        'text': (
            "Zach experiences a setback in his recovery journey, feeling lost again."
        ),
        'choices': {
            1: {'text': "Seek support from a counselor.", 'next_node': 143},
            2: {'text': "Try to handle it on his own.", 'next_node': 144}
        }
    },

    85: {
        'text': (
            "Zach learns about the importance of self-care and begins to practice it."
        ),
        'choices': {
            1: {'text': "Create a self-care routine.", 'next_node': 145},
            2: {'text': "Struggle to maintain the routine.", 'next_node': 146}
        }
    },

    86: {
        'text': (
            "Zach gets involved in a support group for bullying victims."
        ),
        'choices': {
            1: {'text': "Feel understood and accepted.", 'next_node': 147},
            2: {'text': "Feel anxious sharing his story.", 'next_node': 148}
        }
    },

    87: {
        'text': (
            "Zach faces his fears and decides to confront the bullies again."
        ),
        'choices': {
            1: {'text': "Stand tall and assert himself.", 'next_node': 149},
            2: {'text': "Back down, feeling overwhelmed.", 'next_node': 150}
        }
    },
    88: {
        'text': (
            "Zach realizes he has to let go of the past to move forward."
        ),
        'choices': {
            1: {'text': "Start a journey of forgiveness.", 'next_node': 151},
            2: {'text': "Struggle with resentment.", 'next_node': 152}
        }
    },
    89: {
        'text': (
            "Zach attends a workshop on building resilience."
        ),
        'choices': {
            1: {'text': "Learn valuable tools for coping.", 'next_node': 153},
            2: {'text': "Feel skeptical about their effectiveness.", 'next_node': 154}
        }
    },
    90: {
        'text': (
            "Zach finally tells his parents about how severe his dissociation has become. They are supportive and help him find a specialist, "
            "but Zach still feels unsure if he’ll ever fully recover."
        ),
        'choices': {
            1: {'text': "Focus on his recovery with professional help", 'next_node': 155},
            2: {'text': "Resist the help, feeling that it's too late for him", 'next_node': 156}
        }
    },
    91: {
        'text': (
            "Zach starts to feel a sense of hope as he engages more with therapy."
        ),
        'choices': {
            1: {'text': "Continue attending sessions regularly.", 'next_node': 157},
            2: {'text': "Consider taking a break from therapy.", 'next_node': 158}
        }
    },
    92: {
        'text': (
            "Zach has a breakthrough during a session, realizing the impact of bullying on his life."
        ),
        'choices': {
            1: {'text': "Feel empowered to share his story.", 'next_node': 159},
            2: {'text': "Still feel hesitant about opening up.", 'next_node': 160}
        }
    },
    93: {
        'text': (
            "Zach decides to take a break from social media to focus on himself."
        ),
        'choices': {
            1: {'text': "Feel more at peace without the online pressure.", 'next_node': 161},
            2: {'text': "Struggle with feelings of loneliness.", 'next_node': 162}
        }
    },
    94: {
        'text': (
            "Zach joins a local community service project, finding purpose in helping others."
        ),
        'choices': {
            1: {'text': "Feel a sense of fulfillment.", 'next_node': 163},
            2: {'text': "Worry about being overwhelmed by the commitment.", 'next_node': 164}
        }
    },
    95: {
        'text': (
            "Zach's relationship with his parents improves as they communicate better."
        ),
        'choices': {
            1: {'text': "Express gratitude for their support.", 'next_node': 165},
            2: {'text': "Still harbor some resentment towards them.", 'next_node': 166}
        }
    },
    96: {
        'text': (
            "Zach feels motivated to advocate for bullying prevention at school."
        ),
        'choices': {
            1: {'text': "Start a campaign to raise awareness.", 'next_node': 167},
            2: {'text': "Feel unsure if he can make a difference.", 'next_node': 168}
        }
    },
    97: {
        'text': (
            "Zach continues to build resilience and learns to cope with setbacks."
        ),
        'choices': {
            1: {'text': "Embrace his journey of healing.", 'next_node': 169},
            2: {'text': "Still feel overwhelmed at times.", 'next_node': 170}
        }
    },
    98: {
        'text': (
            "Zach's confidence grows as he finds ways to express himself."
        ),
        'choices': {
            1: {'text': "Join a club or team to make new friends.", 'next_node': 171},
            2: {'text': "Continue to work on his individual interests.", 'next_node': 172}
        }
    },
    99: {
        'text': (
            "Zach reflects on his journey and acknowledges the progress he has made."
        ),
        'choices': {
            1: {'text': "Feel hopeful about the future.", 'next_node': 173},
            2: {'text': "Worry about potential relapses.", 'next_node': 174}
        }
    },
    100: {
        'text': (
            "Zach realizes the importance of self-advocacy and begins to stand up for his needs and feelings."
        ),
        'choices': {
            1: {'text': "Continue to advocate for himself and others", 'next_node': 175},
            2: {'text': "Wrestle with self-doubt about his ability to advocate", 'next_node': 176}
        }
    },

    101: {
        'text': (
            "Zach attends his first group therapy session and is nervous but finds comfort in hearing others share their stories."
        ),
        'choices': {
            1: {'text': "Open up about his own experiences.", 'next_node': 177},
            2: {'text': "Stay quiet, unsure if he’s ready to share.", 'next_node': 178}
        }
    },
    102: {
        'text': (
            "Zach makes a close friend from the group therapy who understands him deeply."
        ),
        'choices': {
            1: {'text': "Invest time in building this friendship.", 'next_node': 179},
            2: {'text': "Keep a distance, fearing vulnerability.", 'next_node': 180}
        }
    },
    103: {
        'text': (
            "Zach has a difficult day, but a small act of kindness from a stranger lifts his spirits."
        ),
        'choices': {
            1: {'text': "Pay it forward by helping someone else.", 'next_node': 181},
            2: {'text': "Keep the moment to himself, cherishing it privately.", 'next_node': 182}
        }
    },
    104: {
        'text': (
            "Zach is invited to speak at a school event about bullying awareness."
        ),
        'choices': {
            1: {'text': "Accept the invitation and prepare his speech.", 'next_node': 183},
            2: {'text': "Decline, feeling too nervous to speak in front of others.", 'next_node': 184}
        }
    },
    105: {
        'text': (
            "Zach decides to use his experience to mentor younger students."
        ),
        'choices': {
            1: {'text': "Find fulfillment in guiding others.", 'next_node': 185},
            2: {'text': "Feel unsure if he’s really helping.", 'next_node': 186}
        }
    },
    106: {
        'text': (
            "Zach’s confidence grows as he continues working on his personal development."
        ),
        'choices': {
            1: {'text': "Feel proud of how far he’s come.", 'next_node': 187},
            2: {'text': "Wonder if his progress is enough.", 'next_node': 188}
        }
    },
    107: {
        'text': (
            "Zach begins writing a blog to share his story with others."
        ),
        'choices': {
            1: {'text': "Receive positive feedback and feel encouraged.", 'next_node': 189},
            2: {'text': "Worry about negative responses.", 'next_node': 190}
        }
    },
    108: {
        'text': (
            "Zach finally feels like he’s beginning to forgive himself for the years of pain he’s endured."
        ),
        'choices': {
            1: {'text': "Focus on the future and his continued growth.", 'next_node': 191},
            2: {'text': "Reflect more deeply on the past, still haunted by memories.", 'next_node': 192}
        }
    },
    109: {
        'text': (
            "Zach receives an unexpected apology from one of his former bullies."
        ),
        'choices': {
            1: {'text': "Accept the apology and begin to heal.", 'next_node': 193},
            2: {'text': "Struggle to forgive, still carrying resentment.", 'next_node': 194}
        }
    },
    110: {
        'text': (
            "Zach notices that his relationships with others have become stronger over time."
        ),
        'choices': {
            1: {'text': "Continue nurturing these connections.", 'next_node': 195},
            2: {'text': "Still feel hesitant to trust completely.", 'next_node': 196}
        }
    },
    111: {
        'text': (
            "Zach is offered an opportunity to help design a school anti-bullying program."
        ),
        'choices': {
            1: {'text': "Accept and contribute his ideas.", 'next_node': 197},
            2: {'text': "Feel unprepared for such responsibility.", 'next_node': 198}
        }
    },
    112: {
        'text': (
            "Zach reflects on how far he’s come since the darkest days of being bullied."
        ),
        'choices': {
            1: {'text': "Feel hopeful for what’s to come.", 'next_node': 199},
            2: {'text': "Worry about slipping back into old patterns.", 'next_node': 200}
        }
    },
    113: {
        'text': (
            "Zach takes a solo trip to clear his mind and reflect on his journey."
        ),
        'choices': {
            1: {'text': "Find peace and clarity in solitude.", 'next_node': 201},
            2: {'text': "Feel isolated and unsure about his path.", 'next_node': 202}
        }
    },
    114: {
        'text': (
            "Zach’s newfound self-awareness helps him identify and avoid toxic relationships."
        ),
        'choices': {
            1: {'text': "Build healthier connections going forward.", 'next_node': 203},
            2: {'text': "Still feel wary of trusting others.", 'next_node': 204}
        }
    },
    115: {
        'text': (
            "Zach finds himself drawn to helping others heal from their own experiences of bullying."
        ),
        'choices': {
            1: {'text': "Volunteer to support others through their recovery.", 'next_node': 205},
            2: {'text': "Focus on continuing his personal healing journey.", 'next_node': 206}
        }
    },
    116: {
        'text': (
            "Zach begins to develop a more positive outlook on life, recognizing the value of resilience."
        ),
        'choices': {
            1: {'text': "Embrace this newfound optimism.", 'next_node': 207},
            2: {'text': "Worry about setbacks challenging his positivity.", 'next_node': 208}
        }
    },
    117: {
        'text': (
            "Zach starts to focus more on his long-term goals, including education and career."
        ),
        'choices': {
            1: {'text': "Pursue a career in psychology to help others.", 'next_node': 209},
            2: {'text': "Look into other fields of interest.", 'next_node': 210}
        }
    },
    118: {
        'text': (
            "Zach is surprised by how much he has changed since his most difficult moments."
        ),
        'choices': {
            1: {'text': "Feel proud of his growth.", 'next_node': 211},
            2: {'text': "Still doubt whether he’s truly healed.", 'next_node': 212}
        }
    },
    119: {
        'text': (
            "Zach feels a deep sense of closure when he visits the places where he was once bullied."
        ),
        'choices': {
            1: {'text': "Let go of the painful memories.", 'next_node': 213},
            2: {'text': "Still feel haunted by the past.", 'next_node': 214}
        }
    },
    120: {
        'text': (
            "Zach starts to dream about the future, imagining a life free from the shadows of his past."
        ),
        'choices': {
            1: {'text': "Pursue his dreams with new confidence.", 'next_node': 215},
            2: {'text': "Feel uncertain about the future.", 'next_node': 216}
        }
    },
    121: {
        'text': (
            "Zach's empathy for others grows as he becomes more in tune with his emotions."
        ),
        'choices': {
            1: {'text': "Reach out to others who might be struggling.", 'next_node': 217},
            2: {'text': "Focus on protecting his own emotional boundaries.", 'next_node': 218}
        }
    },
    # Endings from 122 onward would connect all possible outcomes, 
    # ensuring each choice leads to a conclusion that matches the narrative direction.
    122: {
        'text': "Zach finds peace and acceptance in his journey, fully embracing his new sense of self."
    },
    123: {
        'text': "Zach continues to struggle, but he knows he’s not alone in his fight anymore."
    },
    124: {
        'text': "Zach becomes a powerful advocate for bullying prevention, sharing his story to inspire others."
    },
    125: {
        'text': "Zach finds solace in helping others heal, realizing that his experiences have given him strength."
    },
    126: {
        'text': "Zach faces setbacks, but each time he gets back up, he grows stronger and more resilient."
    },
    127: {
        'text': "Zach forgives those who hurt him and moves forward with a sense of peace and freedom."
    },

    129: {
        'text': "Zach finds fulfillment in helping others, using his own experiences to guide them through their challenges."
    },
    130: {
        'text': "Zach builds strong relationships with those who support him, finding a community that cares for him."
    },
    131: {
        'text': "Zach becomes a mentor for younger people, sharing his story and offering advice."
    },
    132: {
        'text': "Zach decides to focus on his own recovery before helping others, ensuring he’s strong enough to support them."
    },
    133: {
        'text': "Zach feels a sense of closure after finally confronting the painful memories of his past."
    },
    134: {
        'text': "Zach embraces the future with newfound confidence, knowing he has the tools to overcome challenges."
    },
    135: {
        'text': "Zach struggles to let go of the past, but realizes that his journey is ongoing and that it’s okay to take his time."
    },
    136: {
        'text': "Zach becomes an advocate for mental health, helping others who have experienced similar struggles."
    },
    137: {
        'text': "Zach feels proud of the progress he’s made, even though there are still difficult days."
    },
    138: {
        'text': "Zach forgives himself for the years of pain and begins to focus on a brighter future."
    },
    139: {
        'text': "Zach accepts that healing is a lifelong journey, but he’s committed to doing the work."
    },
    140: {
        'text': "Zach’s relationships with others become stronger as he learns to trust and open up."
    },
    141: {
        'text': "Zach feels a deep sense of purpose in helping others, turning his pain into a source of strength."
    },
    142: {
        'text': "Zach decides to pursue a career in mental health, inspired by his own experiences."
    },
    143: {
        'text': "Zach feels hopeful for the future, knowing that he’s no longer defined by his past."
    },
    144: {
        'text': "Zach continues to work on himself, understanding that healing takes time and patience."
    },
    145: {
        'text': "Zach finds peace in the realization that his past does not control his future."
    },
    146: {
        'text': "Zach becomes a source of strength for others, offering support and understanding to those who need it."
    },
    147: {
        'text': "Zach finds comfort in the friendships he’s built, realizing he’s not alone in his journey."
    },
    148: {
        'text': "Zach reflects on how far he’s come, feeling proud of the progress he’s made."
    },
    149: {
        'text': "Zach feels empowered by his ability to overcome challenges and help others do the same."
    },
    150: {
        'text': "Zach continues to grow, accepting that healing is a process that takes time and effort."
    },
    151: {
        'text': "Zach feels a sense of accomplishment as he looks back on his journey and how much he’s grown."
    },
    152: {
        'text': "Zach forgives those who hurt him, realizing that forgiveness is a key part of his healing process."
    },
    153: {
        'text': "Zach accepts that while the past has shaped him, it doesn’t define who he is."
    },
    154: {
        'text': "Zach focuses on his recovery with professional help, beginning to see the light at the end of the tunnel."
    },
    155: {
        'text': "Zach resists help, feeling that it’s too late for him, but his loved ones continue to support him."
    },
    156: {
        'text': "Zach finally realizes that it’s never too late to heal, and he begins to accept the help he’s been offered."
    },
    157: {
        'text': "Zach decides to take one day at a time, focusing on small victories in his journey toward healing."
    },





    158: {'text': "Zach fully commits to therapy, making steady progress. Though the road to recovery is long, he starts to find peace within himself. (ENDING 1: Recovery & Growth)"},
    159: {'text': "Zach quits therapy, unable to overcome his skepticism. Without the support he needs, his mental health continues to deteriorate. (ENDING 2: Downward Spiral)"},
    160: {'text': "Zach seeks help and is able to regain control of his life. It’s a difficult journey, but he starts to heal. (ENDING 3: A Second Chance)"},
    161: {'text': "Zach retreats further into isolation. His dissociation becomes so severe that he’s eventually hospitalized. (ENDING 4: Collapse)"},
    162: {'text': "Zach opens up to his parents, and they support him through his recovery. Slowly, he starts to rebuild his life. (ENDING 5: Family Support)"},
    163: {'text': "Zach keeps his parents in the dark, and his mental health worsens. Eventually, the isolation becomes unbearable. (ENDING 6: Breaking Point)"},
    164: {'text': "Zach reaches out for professional help, and though it’s difficult, he begins to regain control of his dissociation. (ENDING 7: Grounded)"},
    165: {'text': "Zach avoids seeking help, and his dissociation spirals out of control, leading to a complete breakdown. (ENDING 8: Fragmented Mind)"},
    166: {'text': "Zach confides in his teacher, who helps him access mental health resources. It’s a turning point in his recovery. (ENDING 9: A Lifeline)"},
    167: {'text': "Zach tells his teacher everything is fine, but the pressure eventually causes him to collapse. (ENDING 10: Overwhelmed)"},
    168: {'text': "Zach opens up about his darkest thoughts, leading to immediate intervention and support. It’s a step towards healing. (ENDING 11: Intervention)"},
    169: {'text': "Zach keeps his feelings hidden, leading to a dangerous escalation of his mental health struggles. (ENDING 12: Silence & Despair)"},
    170: {'text': "Zach makes an effort to reconnect with his friends. Though it’s awkward at first, they welcome him back with open arms. (ENDING 13: Friendship & Healing)"},
    171: {'text': "Zach lets his friendships fade, and his sense of isolation deepens. Without support, his recovery falters. (ENDING 14: Alone)"},
    172: {'text': "Zach stays committed to therapy, and though the road is hard, he makes meaningful progress. (ENDING 15: Steady Progress)"},
    173: {'text': "Zach gets overwhelmed and quits therapy. Without the guidance and structure, his mental health declines again. (ENDING 16: Relapse)"},
    174: {'text': "Zach accepts the need for medical intervention, and after a long recovery process, he begins to rebuild his health. (ENDING 17: Physical & Mental Healing)"},
    175: {'text': "Zach refuses to cooperate with doctors, and his health continues to deteriorate. (ENDING 18: Physical Decline)"},
    176: {'text': "Zach accepts his parents' support, and together, they work towards rebuilding their relationship and his health. (ENDING 19: Family Rebuilding)"},
    177: {'text': "Zach struggles with the idea that he’s too far gone, and it affects his ability to move forward in recovery. (ENDING 20: Stuck in Limbo)"},
    178: {'text': "Zach stays committed to therapy and, in time, finds ways to cope with his trauma. (ENDING 21: Trauma Healing)"},
    179: {'text': "Zach avoids delving too deep into his trauma, which leads to his recovery stalling. (ENDING 22: Stagnation)"},
    180: {'text': "Zach agrees to hospitalization, and though it’s a frightening experience, it’s a turning point in his recovery. (ENDING 23: Emergency Intervention)"},
    181: {'text': "Zach resists hospitalization, leading to further escalation in his mental health struggles. (ENDING 24: Escalation)"},
    182: {'text': "Zach listens to his friends, and with their support, he begins to get the help he needs. (ENDING 25: Friendship Saves)"},
    183: {'text': "Zach insists he’s fine, and without their help, he continues to spiral. (ENDING 26: Isolation & Decline)"},
    184: {'text': "Zach tells a trusted adult about his struggles, and with their help, he begins the road to recovery. (ENDING 27: Saved in Time)"},
    185: {'text': "Zach keeps his struggles hidden, and eventually, his health reaches a breaking point. (ENDING 28: Hidden Struggles)"},
    186: {'text': "Zach embraces the ups and downs of recovery, staying resilient even through setbacks. (ENDING 29: Resilience)"},
    187: {'text': "Zach gets discouraged and abandons recovery, falling back into old habits. (ENDING 30: Abandonment)"},
    188: {'text': "Zach celebrates his progress and continues to work on his mental health, knowing the journey is ongoing. (ENDING 31: Lifelong Healing)"},
    189: {'text': "Zach fears relapse and pulls away from his support network, putting himself at risk. (ENDING 32: Fear of Relapse)"},
    190: {'text': "Zach finally accepts the need for help after a health scare, and though the journey is long, he begins to heal. (ENDING 33: Healing After Crisis)"},
    191: {'text': "Zach continues in a downward spiral, believing he has nothing left to lose. (ENDING 34: Total Decline)"}
}
