victim_story = {
# Zach's journey begins, establishing the foundation of his mental health struggles
    1: {
        'text': "Zach has always been quiet, a little different from his classmates. But things got worse once Bryan and his group started targeting him. Every day at school feels like a battlefield, and Zach is finding it harder to keep going. Today, Bryan tripped him in the hallway, sending Zach's books flying. What should Zach do?",
        'choices': {
            1: {'text': "Ignore it and walk away", 'next_node': 2},
            2: {'text': "Tell a teacher", 'next_node': 3}
        }
    },

    2: {
        'text': "Zach picks up his books and walks away, trying to stay invisible. But inside, his anger is bubbling. His heart races, and he feels a tightness in his chest. Lately, he's been having these strange feelings more often, especially after run-ins with Bryan. What should Zach do?",
        'choices': {
            1: {'text': "Try to calm himself down", 'next_node': 4},
            2: {'text': "Ignore the feelings and push through", 'next_node': 5}
        }
    },

    3: {
        'text': "Zach decides to tell a teacher about the incident. The teacher listens but doesn't seem to do much, just giving Bryan a quick talking-to. Zach wonders if it was even worth saying anything. The bullying doesn’t stop. What should Zach do next?",
        'choices': {
            1: {'text': "Tell his parents about the bullying", 'next_node': 6},
            2: {'text': "Keep everything to himself", 'next_node': 7}
        }
    },

    4: {
        'text': "Zach tries to calm down by taking deep breaths. But every time he sees Bryan in the hallway, his heart pounds. He's not sure how much longer he can deal with this. The fear is starting to take over. What should he do next?",
        'choices': {
            1: {'text': "Open up to a friend", 'next_node': 8},
            2: {'text': "Keep bottling up the fear", 'next_node': 9}
        }
    },

    5: {
        'text': "Zach tries to ignore his rising anxiety and pushes through the day. But by lunchtime, he's too overwhelmed to eat. His hands are shaky, and he feels dizzy. He realizes that he's having a panic attack. What should he do?",
        'choices': {
            1: {'text': "Go to the nurse", 'next_node': 10},
            2: {'text': "Find a quiet place and hide", 'next_node': 11}
        }
    },

    6: {
        'text': "Zach tells his parents about the bullying, but they're not sure how to help. They tell him to stand up for himself, but that feels impossible. Zach feels more alone than ever. What should he do next?",
        'choices': {
            1: {'text': "Start skipping school", 'next_node': 12},
            2: {'text': "Try to confront Bryan on his own", 'next_node': 13}
        }
    },

    7: {
        'text': "Zach decides to keep the bullying a secret from his parents. He doesn't want them to worry or think he's weak. But every night, he lies awake, replaying the bullying over and over in his mind. His sleep is getting worse. What should he do?",
        'choices': {
            1: {'text': "Start using sleeping pills to cope", 'next_node': 14},
            2: {'text': "Try to tough it out without help", 'next_node': 15}
        }
    },

    #### **Introduction to Mental Health Struggles (Panic Attacks, Isolation, Social Withdrawal)**

    8: {
        'text': "Zach confides in his best friend, but even though they try to comfort him, the friend doesn’t really understand what Zach is going through. Still, it's nice to have someone listen. But the next day, Bryan’s bullying escalates. Zach feels like there's no escape. What next?",
        'choices': {
            1: {'text': "Cut himself off from his friend", 'next_node': 16},
            2: {'text': "Keep opening up to others", 'next_node': 17}
        }
    },

    9: {
        'text': "Zach continues bottling up his fear. It’s harder and harder to concentrate in class, and he’s falling behind. Every time Bryan walks past him, Zach's heart pounds, and he feels like he can't breathe. His panic attacks are getting worse. What should he do?",
        'choices': {
            1: {'text': "Start skipping class", 'next_node': 18},
            2: {'text': "Push himself to keep attending class", 'next_node': 19}
        }
    },

    10: {
        'text': "Zach goes to the nurse, who tells him that he’s likely having a panic attack. She suggests he talk to a counselor, but Zach isn’t sure he’s ready to open up to someone new. What should he do?",
        'choices': {
            1: {'text': "Talk to the school counselor", 'next_node': 20},
            2: {'text': "Leave the nurse’s office and handle it on his own", 'next_node': 21}
        }
    },

    11: {
        'text': "Zach finds a quiet corner in the school library, his heart still racing. He feels light-headed, like he’s about to pass out. It takes him almost an hour to calm down. Zach starts avoiding the hallways entirely, taking alternate routes to avoid Bryan. What next?",
        'choices': {
            1: {'text': "Avoid school completely", 'next_node': 22},
            2: {'text': "Tell his parents about his panic attacks", 'next_node': 23}
        }
    },

    #### **Deepening Struggles: Self-Harm, Suicidal Ideation, and Drug Use**

    12: {
        'text': "Zach starts skipping school entirely. At first, it feels like relief. But as he spends more and more time alone, his thoughts grow darker. He's starting to feel trapped and hopeless, and he can’t see a way out. What next?",
        'choices': {
            1: {'text': "Start cutting himself to feel something", 'next_node': 24},
            2: {'text': "Try to numb the pain with alcohol", 'next_node': 25}
        }
    },

    13: {
        'text': "Zach tries to confront Bryan, but it only makes things worse. Bryan and his friends laugh, and Zach is humiliated in front of the entire class. He feels like the walls are closing in on him, and he starts thinking about suicide. What should Zach do?",
        'choices': {
            1: {'text': "Reach out to a suicide hotline", 'next_node': 26},
            2: {'text': "Start self-harming", 'next_node': 27}
        }
    },

    14: {
        'text': "Zach starts using sleeping pills to cope, taking more than the recommended dose to escape the anxiety and insomnia. The pills help him sleep, but when he wakes up, the same feelings of dread return. What should Zach do?",
        'choices': {
            1: {'text': "Increase his dosage", 'next_node': 28},
            2: {'text': "Tell his parents about his struggles", 'next_node': 29}
        }
    },

    15: {
        'text': "Zach continues toughing it out, refusing to take any pills or tell anyone about his problems. But each day, his mental state deteriorates further. The thoughts of self-harm and suicide are becoming harder to ignore. What should he do?",
        'choices': {
            1: {'text': "Finally reach out for help", 'next_node': 30},
            2: {'text': "Act on his suicidal thoughts", 'next_node': 31}
        }
    },
    16: {
        'text': "Zach feels guilty for cutting himself off from his friend. The isolation is suffocating, and he struggles to find reasons to get out of bed. Bryan’s bullying echoes in his mind, and he starts to self-harm more frequently. What should Zach do?",
        'choices': {
            1: {'text': "Seek help from a counselor", 'next_node': 32},
            2: {'text': "Continue isolating himself", 'next_node': 33}
        }
    },

    17: {
        'text': "Zach decides to keep opening up to others, but each time he shares, he feels like a burden. His anxiety peaks, and he worries that no one can truly understand his pain. The pressure mounts. What should he do next?",
        'choices': {
            1: {'text': "Try to talk to a school counselor", 'next_node': 34},
            2: {'text': "Seek comfort in unhealthy coping mechanisms", 'next_node': 35}
        }
    },

    18: {
        'text': "Zach starts skipping classes frequently. The relief is temporary, but the anxiety about falling behind in school becomes overwhelming. He feels like he’s losing control of his life. What should Zach do next?",
        'choices': {
            1: {'text': "Try to catch up on his own", 'next_node': 36},
            2: {'text': "Skip school altogether and stay home", 'next_node': 37}
        }
    },

    19: {
        'text': "Zach pushes himself to keep attending class, but he can’t focus. The panic attacks are becoming more frequent. He feels like he’s trapped in a cycle of anxiety and fear. What should he do?",
        'choices': {
            1: {'text': "Talk to a friend about his struggles", 'next_node': 38},
            2: {'text': "Continue to suffer in silence", 'next_node': 39}
        }
    },

    20: {
        'text': "Zach decides to talk to the school counselor. At first, he struggles to open up, but gradually, he begins to share his feelings about the bullying and his anxiety. The counselor offers support and coping strategies. What should Zach do next?",
        'choices': {
            1: {'text': "Commit to regular counseling sessions", 'next_node': 40},
            2: {'text': "Still keep some feelings to himself", 'next_node': 41}
        }
    },


    21: {
        'text': "Zach is now in high school. Though Bryan is no longer at the same school, the damage he caused remains. Zach's panic attacks have become less frequent, but he still feels on edge in social situations. He avoids crowded places and spends most of his time alone. What should Zach focus on?",
        'choices': {
            1: {'text': "Try to make new friends despite his anxiety", 'next_node': 22},
            2: {'text': "Stay withdrawn, focusing only on surviving high school", 'next_node': 23}
        }
    },

    22: {
        'text': "Zach tries to open up and make new friends, but he struggles. Small talk feels overwhelming, and he often second-guesses himself in conversations. His new friends don't know about his past, but they notice his awkwardness. One day, Zach overhears them laughing about him behind his back. How should Zach respond?",
        'choices': {
            1: {'text': "Confront them", 'next_node': 24},
            2: {'text': "Withdraw further into isolation", 'next_node': 25}
        }
    },

    23: {
        'text': "Zach decides to keep to himself. High school is just something he needs to get through. He focuses on his studies, but without friends, his mental health continues to deteriorate. He begins feeling increasingly disconnected from the world around him. The isolation feeds into a growing sense of dissociation. What should he do?",
        'choices': {
            1: {'text': "Seek out counseling for the dissociation", 'next_node': 26},
            2: {'text': "Try to handle it on his own, without professional help", 'next_node': 27}
        }
    },

    24: {
        'text': "Zach confronts his friends, but they brush it off, saying they were 'just joking.' The confrontation leaves Zach feeling even more isolated. His trust in people diminishes further. He wonders if he's overreacting or if he'll ever feel truly connected to anyone again. What should he do next?",
        'choices': {
            1: {'text': "Stop trying to make friends entirely", 'next_node': 28},
            2: {'text': "Give friendship another try with different people", 'next_node': 29}
        }
    },

    25: {
        'text': "Zach retreats into himself, avoiding any social interaction. His grades start slipping, and he spends more time at home, disconnected from reality. The dissociation becomes more frequent, with Zach feeling like he's living outside of his own body, watching his life from a distance. How should Zach cope?",
        'choices': {
            1: {'text': "Start using drugs or alcohol to numb the dissociation", 'next_node': 30},
            2: {'text': "Attempt to find comfort in solitary activities, like reading or gaming", 'next_node': 31}
        }
    },
    26: {
        'text': "Zach decides to seek counseling for his dissociation. The counselor helps him explore his feelings of disconnect and offers grounding techniques to help him feel more present. While it's a tough journey, Zach starts to feel a small sense of hope. What should he focus on next?",
        'choices': {
            1: {'text': "Practice grounding techniques regularly", 'next_node': 32},
            2: {'text': "Continue avoiding social situations", 'next_node': 33}
        }
    },

    27: {
        'text': "Zach tries to handle it on his own, but the dissociation worsens. He feels trapped in a fog, unable to connect with anyone or anything. The isolation leads him to darker thoughts. What should he do?",
        'choices': {
            1: {'text': "Reach out for help before it's too late", 'next_node': 34},
            2: {'text': "Give in to the feelings of hopelessness", 'next_node': 35}
        }
    },

    28: {
        'text': "Zach decides to stop trying to make friends entirely. He immerses himself in his studies, but the loneliness deepens. The lack of social interaction exacerbates his mental health issues. What should he do to cope with the pain of isolation?",
        'choices': {
            1: {'text': "Join a club to try and meet new people", 'next_node': 36},
            2: {'text': "Keep isolating himself, believing it’s safer", 'next_node': 37}
        }
    },

    29: {
        'text': "Zach decides to give friendship another try. He approaches a different group of classmates, but his past experiences make him hesitant. He fears rejection. Should he take a leap of faith?",
        'choices': {
            1: {'text': "Try to engage in conversations slowly", 'next_node': 38},
            2: {'text': "Hold back and observe from a distance", 'next_node': 39}
        }
    },

    30: {
        'text': "Zach starts using drugs and alcohol to numb the feelings of dissociation. While it provides temporary relief, he soon finds himself in a downward spiral. His grades plummet, and he becomes even more isolated. What should he do?",
        'choices': {
            1: {'text': "Seek help for substance abuse", 'next_node': 40},
            2: {'text': "Continue using substances to cope", 'next_node': 41}
        }
    },

    31: {
        'text': "Zach finds comfort in solitary activities like reading and gaming. Although it helps him escape, he knows it's not a solution. He’s becoming more withdrawn, and the dissociation lingers. What should he focus on?",
        'choices': {
            1: {'text': "Balance solitary activities with social interactions", 'next_node': 42},
            2: {'text': "Continue to isolate himself", 'next_node': 43}
        }
    },

    32: {
        'text': "Zach practices grounding techniques regularly, learning to connect with his surroundings. Slowly, he starts feeling more present. Though it’s not perfect, there’s improvement. What should he do next?",
        'choices': {
            1: {'text': "Share his progress with a trusted friend", 'next_node': 44},
            2: {'text': "Keep it to himself and focus on his own growth", 'next_node': 45}
        }
    },

    33: {
        'text': "Zach continues avoiding social situations, and the feelings of dissociation return stronger than ever. He realizes he’s missing out on life but feels too scared to change. What should he do?",
        'choices': {
            1: {'text': "Consider joining a support group", 'next_node': 46},
            2: {'text': "Stay in his comfort zone and avoid risks", 'next_node': 47}
        }
    },

    34: {
        'text': "Zach reaches out for help before it's too late. He finds a support group that focuses on mental health and connects with others who understand his struggles. This step gives him hope. What should he do next?",
        'choices': {
            1: {'text': "Continue attending the support group", 'next_node': 48},
            2: {'text': "Try to face his issues without support", 'next_node': 49}
        }
    },

    35: {
        'text': "Zach gives in to the feelings of hopelessness, spiraling deeper into despair. His grades suffer, and he finds it harder to get out of bed each day. What should he do?",
        'choices': {
            1: {'text': "Contact a helpline for immediate support", 'next_node': 50},
            2: {'text': "Ignore the thoughts and try to carry on", 'next_node': 51}
        }
    },

    36: {
        'text': "Zach decides to join a club to try and meet new people. It’s challenging, but he finds a bit of connection. Some members are welcoming, and Zach feels a glimmer of hope. What should he do next?",
        'choices': {
            1: {'text': "Open up about his past to the group", 'next_node': 52},
            2: {'text': "Keep his past a secret and just enjoy the moment", 'next_node': 53}
        }
    },

    37: {
        'text': "Zach continues isolating himself, believing it’s safer. But the loneliness becomes unbearable, leading to feelings of worthlessness. What should he do?",
        'choices': {
            1: {'text': "Reach out to an old friend", 'next_node': 54},
            2: {'text': "Stay isolated and hope things change", 'next_node': 55}
        }
    },

    38: {
        'text': "Zach tries to engage in conversations slowly. He finds that some people are friendly and interested in getting to know him. This is encouraging, but he still feels insecure. What should he do next?",
        'choices': {
            1: {'text': "Invite someone out for coffee", 'next_node': 56},
            2: {'text': "Keep the conversations light and casual", 'next_node': 57}
        }
    },

    39: {
        'text': "Zach holds back and observes from a distance, feeling safer. He worries about being judged or rejected. However, he realizes he might miss out on potential friendships. What should he do?",
        'choices': {
            1: {'text': "Take a risk and approach someone", 'next_node': 58},
            2: {'text': "Stay in the background and watch", 'next_node': 59}
        }
    },

    40: {
        'text': "Zach seeks help for substance abuse, entering a program that focuses on recovery. It’s tough, but he begins to understand his triggers and learns healthier coping strategies. What should he focus on?",
        'choices': {
            1: {'text': "Commit to his recovery journey", 'next_node': 60},
            2: {'text': "Doubt his ability to change", 'next_node': 61}
        }
    },

    41: {
        'text': "Zach is now 25. He has a job, but his social anxiety makes it hard to interact with colleagues. He often feels like an outsider, even in group settings. His panic attacks are less frequent, but moments of intense anxiety still catch him off guard. What should Zach focus on?",
        'choices': {
            1: {'text': "Focus on building a career despite his anxiety", 'next_node': 42},
            2: {'text': "Find solace in unhealthy coping mechanisms like drinking", 'next_node': 43}
        }
    },

    42: {
        'text': "Zach throws himself into his career, but the pressure to be perfect triggers his anxiety. He starts having trouble sleeping again, staying up late worrying about mistakes or how others perceive him. He's becoming burnt out, and his mental health is deteriorating. How should he handle the stress?",
        'choices': {
            1: {'text': "Talk to a therapist about work-related stress", 'next_node': 44},
            2: {'text': "Ignore the signs of burnout and push harder", 'next_node': 45}
        }
    },

    43: {
        'text': "Zach starts drinking more regularly. At first, it helps numb the anxiety, but soon he finds himself needing a drink to even get through the day. His work performance is slipping, and he's distancing himself from friends and family. What should he do?",
        'choices': {
            1: {'text': "Admit to himself he has a problem and seek help", 'next_node': 46},
            2: {'text': "Keep drinking, convincing himself he has it under control", 'next_node': 47}
        }
    },

    44: {
        'text': "Zach starts therapy and begins to address the underlying causes of his anxiety. His therapist helps him unpack the bullying he endured and how it's affected his self-worth. It’s a slow process, but Zach is starting to feel more in control. What should he focus on next?",
        'choices': {
            1: {'text': "Continue working through his trauma and start healing", 'next_node': 48},
            2: {'text': "Back away from therapy when it gets too overwhelming", 'next_node': 49}
        }
    },

    45: {
        'text': "Zach keeps pushing himself at work, but his mental health deteriorates. He's constantly exhausted, and the anxiety is beginning to affect his performance. His boss pulls him aside to talk about his declining productivity. Zach feels like he's on the verge of breaking down. What should he do?",
        'choices': {
            1: {'text': "Take a leave of absence to focus on his mental health", 'next_node': 50},
            2: {'text': "Continue working and risk a breakdown", 'next_node': 51}
        }
    },

    #### **The Impact on Relationships and Dissociation**

    46: {
        'text': "Zach admits to himself that his drinking is out of control and checks into rehab. The process is difficult, but he's committed to turning his life around. Slowly, he begins to rebuild his life without alcohol. However, his anxiety and dissociation still linger. What should he focus on now?",
        'choices': {
            1: {'text': "Continue therapy to address the deeper issues", 'next_node': 52},
            2: {'text': "Try to manage his anxiety without professional help", 'next_node': 53}
        }
    },

    47: {
        'text': "Zach keeps drinking, spiraling further into addiction. His relationships with friends and family are falling apart, and he's losing control of his life. One night, after a particularly bad binge, he wakes up in a hospital, not remembering how he got there. What should he do?",
        'choices': {
            1: {'text': "Finally seek help", 'next_node': 54},
            2: {'text': "Ignore the wake-up call and continue drinking", 'next_node': 55}
        }
    },

    48: {
        'text': "Zach continues working through therapy, uncovering layers of trauma from his childhood. He begins to understand how the bullying affected his self-image and his ability to trust others. His dissociation is less frequent, but it still happens during moments of high stress. How should Zach proceed?",
        'choices': {
            1: {'text': "Focus on developing coping strategies for stress", 'next_node': 56},
            2: {'text': "Try to avoid stress altogether", 'next_node': 57}
        }
    },

    #### **Node 61 to 80**: Midlife and Beyond – The Long-Term Battle

    #Zach’s mental health continues to shape his midlife, impacting his career, relationships, and overall quality of life. He may find healing, or his struggles may deepen, depending on earlier choices.

 
    61: {
        'text': "Zach is now in his 40s. His career is stable, but he's never truly been able to shake the anxiety. He still struggles with feelings of inadequacy, always fearing that his colleagues will see him as weak or incompetent. His panic attacks have decreased, but stress triggers occasional episodes. How should Zach manage his mental health now?",
        'choices': {
            1: {'text': "Continue therapy to manage his stress", 'next_node': 62},
            2: {'text': "Rely on his coping mechanisms without professional help", 'next_node': 63}
        }
    },

    62: {
        'text': "Zach decides to continue therapy. With each session, he learns more about managing stress and anxiety. While the past still affects him, he has developed healthy coping mechanisms. He reconnects with family members he had distanced himself from during his darker years, finding a sense of belonging he thought he'd lost. However, his work environment remains stressful, and he's considering a career change. What should Zach do?",
        'choices': {
            1: {'text': "Pursue a career that aligns more with his passions", 'next_node': 64},
            2: {'text': "Stay in his current job, feeling it's too late to change", 'next_node': 65}
        }
    },

    63: {
        'text': "Zach decides not to return to therapy, relying on the coping mechanisms he has developed over the years. He convinces himself that he can handle his anxiety without professional help. However, the stress from work and life builds up over time. He starts experiencing episodes of dissociation again, where he feels disconnected from reality. How should Zach proceed?",
        'choices': {
            1: {'text': "Return to therapy before things get worse", 'next_node': 66},
            2: {'text': "Ignore the signs and continue pushing through on his own", 'next_node': 67}
        }
    },

    64: {
        'text': "Zach decides to pursue a career that aligns with his passions. Though it's a risk, the change brings him a sense of purpose and fulfillment that his previous job lacked. His mental health improves as he begins to enjoy his work, and his anxiety lessens significantly. However, starting over is challenging, and financial instability creates new stressors. What should Zach prioritize?",
        'choices': {
            1: {'text': "Focus on long-term goals and trust the process", 'next_node': 68},
            2: {'text': "Fall back into unhealthy habits to cope with new stress", 'next_node': 69}
        }
    },

    65: {
        'text': "Zach decides to stay in his current job, feeling that it's too late to make a major career change. While he maintains financial stability, the stress continues to weigh on him. Over time, he feels more burnt out, and his dissociative episodes become more frequent. He's unsure how much longer he can handle the pressure. What should Zach do?",
        'choices': {
            1: {'text': "Take a break from work to focus on his mental health", 'next_node': 70},
            2: {'text': "Push through and hope things improve on their own", 'next_node': 71}
        }
    },

    66: {
        'text': "Zach returns to therapy, realizing that trying to cope alone was leading him back down a dangerous path. His therapist helps him work through the resurfacing dissociation and anxiety, and Zach starts to feel more grounded again. The healing process is slow, but Zach knows he's moving in the right direction. What should he focus on now?",
        'choices': {
            1: {'text': "Rebuild relationships with friends and family", 'next_node': 72},
            2: {'text': "Focus on self-improvement without relying on others", 'next_node': 73}
        }
    },

    67: {
        'text': "Zach continues to ignore the signs of worsening mental health. He tells himself that he's managing, but deep down, he knows he's not. His dissociation becomes more severe, and he starts to question reality at times, feeling like he's losing control. One night, he experiences a full breakdown, unsure of where to turn. What should he do?",
        'choices': {
            1: {'text': "Seek emergency help and commit to recovery", 'next_node': 74},
            2: {'text': "Try to cope by self-medicating with alcohol or drugs", 'next_node': 75}
        }
    },

    68: {
        'text': "Zach remains committed to his long-term goals, focusing on building a fulfilling career despite the early challenges. Over time, his financial situation improves, and he feels a deep sense of accomplishment. His anxiety is manageable, and he has developed a strong support network. Zach starts feeling more in control of his life than ever before. What should he focus on now?",
        'choices': {
            1: {'text': "Continue building a meaningful career", 'next_node': 76},
            2: {'text': "Reconnect with the personal aspects of life he neglected", 'next_node': 77}
        }
    },

    69: {
        'text': "The stress of starting over becomes overwhelming, and Zach slips back into old habits. He begins drinking again to cope with the financial and emotional strain. At first, it seems to help, but soon he's using alcohol more frequently. His relationships suffer, and his new career begins to unravel. What should Zach do?",
        'choices': {
            1: {'text': "Seek help before it's too late", 'next_node': 78},
            2: {'text': "Continue drinking, convincing himself he can handle it", 'next_node': 79}
        }
    },

    70: {
        'text': "Zach decides to take a break from work to focus on his mental health. During this time, he engages in self-care practices, reconnects with his passions, and attends therapy sessions regularly. This period of rest proves beneficial, and he starts to feel more grounded and hopeful about the future. What should he do next?",
        'choices': {
            1: {'text': "Create a plan for returning to work with better boundaries", 'next_node': 80},
            2: {'text': "Consider exploring a completely new career path", 'next_node': 81}
        }
    },

    71: {
        'text': "Zach pushes through, hoping things will improve on their own. However, the pressure builds, leading to a complete burnout. He realizes he can no longer function at work, and his mental health deteriorates rapidly. What should he do?",
        'choices': {
            1: {'text': "Reach out to a trusted colleague for support", 'next_node': 82},
            2: {'text': "Continue to suffer in silence", 'next_node': 83}
        }
    },

    72: {
        'text': "Zach focuses on rebuilding relationships with friends and family. This support system helps him feel more connected and understood. As he shares his struggles, he realizes he’s not alone in his journey. What should he prioritize next?",
        'choices': {
            1: {'text': "Engage in social activities to strengthen these bonds", 'next_node': 84},
            2: {'text': "Balance social life with personal growth efforts", 'next_node': 85}
        }
    },

    73: {
        'text': "Zach decides to focus on self-improvement without relying on others. He immerses himself in personal development books and activities. While he learns a lot, he starts to feel increasingly isolated. What should he do next?",
        'choices': {
            1: {'text': "Reach out to others to share what he’s learned", 'next_node': 86},
            2: {'text': "Continue alone, believing it's best for his growth", 'next_node': 87}
        }
    },

    74: {
        'text': "Zach seeks emergency help and commits to recovery. With professional support, he starts addressing the root causes of his anxiety and dissociation. The path is difficult, but he feels a renewed sense of determination. What should he focus on now?",
        'choices': {
            1: {'text': "Build a structured routine to support his recovery", 'next_node': 88},
            2: {'text': "Explore creative outlets for self-expression", 'next_node': 89}
        }
    },

    75: {
        'text': "Zach tries to cope by self-medicating with alcohol or drugs. Initially, he finds temporary relief, but soon the consequences catch up with him. He faces mounting problems at work and in his personal life. What should he do?",
        'choices': {
            1: {'text': "Confront the reality of his addiction and seek help", 'next_node': 90},
            2: {'text': "Continue to deny the impact of his habits", 'next_node': 91}
        }
    },

    76: {
        'text': "Zach continues building a meaningful career and thrives professionally. His confidence grows, and he feels empowered by his achievements. He realizes that he wants to give back to others facing similar challenges. What should he focus on next?",
        'choices': {
            1: {'text': "Mentor others who struggle with mental health issues", 'next_node': 92},
            2: {'text': "Pursue advanced education in his field", 'next_node': 93}
        }
    },

    77: {
        'text': "Zach reconnects with the personal aspects of life he neglected. He spends time with family and friends, nurturing relationships that matter. This balance brings him joy and fulfillment. What should he prioritize now?",
        'choices': {
            1: {'text': "Plan regular gatherings with loved ones", 'next_node': 94},
            2: {'text': "Focus on personal hobbies and interests", 'next_node': 95}
        }
    },

    78: {
        'text': "Zach seeks help before it's too late. He joins a support group for those struggling with addiction, finding solace in sharing his experiences. With the support of others, he begins to address his unhealthy habits. What should he do next?",
        'choices': {
            1: {'text': "Commit to sobriety and recovery practices", 'next_node': 96},
            2: {'text': "Tempted to relapse but resist the urge", 'next_node': 97}
        }
    },

    79: {
        'text': "Zach continues drinking, convincing himself he can handle it. However, his life spirals further out of control. He faces mounting consequences, including loss of relationships and professional setbacks. What should he do?",
        'choices': {
            1: {'text': "Hit rock bottom and finally seek help", 'next_node': 98},
        2: {'text': "Try to manage everything on his own", 'next_node': 99}
         }
    },

    81: {
    'text': "Zach is now in his 60s. The decisions he made throughout his life have brought him to this point. Looking back, Zach reflects on the way bullying shaped him and how he responded to the challenges of mental health. As he enters retirement, what should Zach focus on?",
    'choices': {
        1: {'text': "Find peace and fulfillment in the relationships he's built", 'next_node': 82},
        2: {'text': "Focus on resolving the regrets of his past", 'next_node': 83}
         }
    },

    82: {
        'text': "Zach has found peace in his later years. He maintained a successful career, worked through his trauma, and built meaningful relationships. While his anxiety still occasionally surfaces, he knows how to manage it. Zach retires surrounded by loved ones, feeling that he's finally achieved the happiness he once thought was out of reach.",
        'ending': "Good Ending"
    },

    83: {
        'text': "Zach realizes that many of the decisions he made led to regret. His relationships with family and friends are strained, and his mental health remains fragile. He spends his later years trying to make amends and come to terms with the choices he made. Though he finds some peace, the weight of his unresolved trauma lingers.",
        'ending': "Neutral Ending"
    },

    84: {
        'text': "Zach's lifelong struggle with addiction and anxiety has taken its toll. He alienated the people who cared about him, and in his later years, he finds himself alone. His mental health has deteriorated, and he feels isolated from the world. Zach spends his final years battling the same demons he faced as a young man, never truly finding relief.",
        'ending': "Bad Ending"
    },

    85: {
        'text': "Zach managed to avoid a complete breakdown, but his life never reached its full potential. He worked hard but always felt like he was on the edge of falling apart. In his later years, Zach has moments of peace but is haunted by the 'what ifs' of his life. He finds some comfort in his achievements, but his mental health always felt like a barrier he couldn't fully overcome.",
        'ending': "Semi-Bad Ending"
    },

    86: {
        'text': "Though Zach struggled throughout his life, he found a path to partial recovery. He dealt with anxiety and occasional bouts of dissociation, but he never let them consume him entirely. His relationships were strained at times, but he managed to hold onto a few close friends and family. In the end, Zach finds some level of peace, though he knows that his past will always be a part of him.",
        'ending': "Semi-Good Ending"
    },

}