bully_story = {
    # Introduction - The Start of Bryan's Journey
    1: {
        'text': "Bryan feels the pressure from his group of friends. They've been teasing Zach for a while, and today the group looks to Bryan for the next move. What will Bryan do?",
        'choices': {
            1: {'text': "Join in the bullying", 'next_node': 2},
            2: {'text': "Refuse to join", 'next_node': 3}
        }
    },
    
    # Branch 1 - Bullying Starts
    2: {
        'text': "Bryan joins in the bullying. His friends laugh, but Zach looks devastated. Later, Bryan feels a pang of guilt. Should Bryan apologize or ignore it?",
        'choices': {
            1: {'text': "Apologize to Zach", 'next_node': 4},
            2: {'text': "Ignore the guilt and continue bullying", 'next_node': 5}
        }
    },

    # Branch 2 - Standing Up to Friends
    3: {
        'text': "Bryan refuses to join in the bullying. His friends look annoyed and accuse him of going soft. Later, Zach seems grateful. What will Bryan do?",
        'choices': {
            1: {'text': "Stick to his decision", 'next_node': 6},
            2: {'text': "Try to regain the group's approval", 'next_node': 7}
        }
    },

    # Apologizing to Zach
    4: {
        'text': "Bryan decides to apologize to Zach. Zach looks surprised but grateful. Bryan feels relieved, but his friends might find out. What next?",
        'choices': {
            1: {'text': "Tell his friends he apologized", 'next_node': 8},
            2: {'text': "Keep it a secret", 'next_node': 9}
        }
    },

    # Ignoring the Guilt
    5: {
        'text': "Bryan ignores the guilt and continues bullying. Over time, the bullying escalates, and more students are targeted. Will Bryan continue, or will he start feeling worse?",
        'choices': {
            1: {'text': "Continue bullying", 'next_node': 10},
            2: {'text': "Start feeling conflicted", 'next_node': 11}
        }
    },

    # Standing by His Decision
    6: {
        'text': "Bryan stands by his decision and distances himself from the group. His friends start treating him differently, and Bryan feels isolated. Should Bryan try to make new friends?",
        'choices': {
            1: {'text': "Yes, seek new friends", 'next_node': 12},
            2: {'text': "No, remain isolated", 'next_node': 13}
        }
    },

    # Regaining the Group's Approval
    7: {
        'text': "Bryan tries to regain the approval of his friends. He cracks a joke at Zach's expense to fit in, but it doesn't feel right. His friends laugh, but Bryan feels conflicted. What should he do next?",
        'choices': {
            1: {'text': "Continue seeking approval", 'next_node': 14},
            2: {'text': "Step away from the group again", 'next_node': 15}
        }
    },

    # Branch 4 - Telling Friends About Apology
    8: {
        'text': "Bryan tells his friends that he apologized to Zach. His friends are shocked and start mocking him for being soft. They say he's changing. Does Bryan defend his decision or back down?",
        'choices': {
            1: {'text': "Defend his decision", 'next_node': 16},
            2: {'text': "Back down and try to regain their trust", 'next_node': 17}
        }
    },

    # Branch 5 - Keeping the Apology Secret
    9: {
        'text': "Bryan decides to keep the apology to Zach a secret. He tries to maintain his image with his friends, but the guilt weighs on him. What should Bryan do next?",
        'choices': {
            1: {'text': "Confess to his friends", 'next_node': 18},
            2: {'text': "Continue keeping it a secret", 'next_node': 19}
        }
    },

    # Continuing Bullying (Escalation)
    10: {
        'text': "Bryan continues bullying, and the group escalates their teasing of Zach and other students. Bryan starts skipping class and avoiding teachers. One day, a teacher notices his change in behavior. What should Bryan do?",
        'choices': {
            1: {'text': "Speak with the teacher", 'next_node': 20},
            2: {'text': "Avoid the teacher", 'next_node': 21}
        }
    },

    # Feeling Conflicted About Bullying
    11: {
        'text': "Bryan begins to feel conflicted about bullying Zach and others. His friends don't notice his hesitation, but inside, Bryan starts to doubt himself. What should he do?",
        'choices': {
            1: {'text': "Talk to someone about how he feels", 'next_node': 22},
            2: {'text': "Keep quiet and continue bullying", 'next_node': 23}
        }
    },

    # Seeking New Friends
    12: {
        'text': "Bryan starts seeking new friends, distancing himself from the bullies. It's not easy, and people notice he's alone a lot. But he feels better about himself. Will he stick with this new path?",
        'choices': {
            1: {'text': "Yes, keep seeking new friends", 'next_node': 24},
            2: {'text': "No, rejoin the old group", 'next_node': 25}
        }
    },

    # Remaining Isolated
    13: {
        'text': "Bryan decides to remain isolated, distancing himself from his old friends but not making any new ones. He starts to feel lonely and unsure of himself. What's next for Bryan?",
        'choices': {
            1: {'text': "Reach out to Zach", 'next_node': 26},
            2: {'text': "Stay isolated", 'next_node': 27}
        }
    },

    # Continuing to Seek Approval
    14: {
        'text': "Bryan continues trying to gain approval from his friends. The more he does, the worse he feels. The bullying escalates, and Bryan realizes he’s becoming someone he doesn’t like. What now?",
        'choices': {
            1: {'text': "Confront his friends", 'next_node': 28},
            2: {'text': "Keep going", 'next_node': 29}
        }
    },

    # Stepping Away Again
    15: {
        'text': "Bryan steps away from his group of friends again. This time, they notice and start teasing him. Bryan feels torn between doing the right thing and fitting in. What does he do next?",
        'choices': {
            1: {'text': "Try to stand his ground", 'next_node': 30},
            2: {'text': "Give in and apologize to his friends", 'next_node': 31}
        }
    },

    # Defending His Decision to Apologize
    16: {
        'text': "Bryan stands up to his friends, explaining why he apologized to Zach. They mock him for it, but Bryan feels a sense of pride for standing up for what’s right. What happens next?",
        'choices': {
            1: {'text': "Leave the group for good", 'next_node': 32},
            2: {'text': "Try to balance both sides", 'next_node': 33}
        }
    },

    # Backing Down to Regain Trust
    17: {
        'text': "Bryan backs down from defending Zach, telling his friends it was a mistake. They laugh it off and accept him back into the group. But deep down, Bryan feels worse than ever. What should he do?",
        'choices': {
            1: {'text': "Start reflecting on his actions", 'next_node': 34},
            2: {'text': "Ignore the feeling and continue bullying", 'next_node': 35}
        }
    },

    # Confessing to His Friends
    18: {
        'text': "Bryan confesses to his friends that he apologized to Zach. They laugh and ridicule him. Bryan has to decide whether to stick to his values or try to win their approval back.",
        'choices': {
            1: {'text': "Stick to his values", 'next_node': 36},
            2: {'text': "Seek their approval again", 'next_node': 37}
        }
    },

    # Continuing to Keep It a Secret
    19: {
        'text': "Bryan keeps the apology a secret, but the guilt weighs heavier on him. He can’t look at Zach without feeling bad. His friends don’t notice, but Bryan feels increasingly isolated. What next?",
        'choices': {
            1: {'text': "Confess to Zach", 'next_node': 38},
            2: {'text': "Continue hiding it", 'next_node': 39}
        }
    },
    


    20: {
        'text': "Bryan decides to speak with the teacher about his change in behavior. The teacher is understanding and encourages Bryan to make better choices. Bryan feels relieved. What should he do next?",
        'choices': {
            1: {'text': "Apologize to Zach and start making amends", 'next_node': 40},
            2: {'text': "Focus on fixing his own behavior", 'next_node': 41}
        }
    },

    # Avoiding the teacher and continuing down a darker path
    21: {
        'text': "Bryan avoids the teacher and skips classes more often. His grades begin to slip, and his relationships with friends deteriorate. He feels lost and unsure of himself. What should Bryan do?",
        'choices': {
            1: {'text': "Confront his behavior and seek help", 'next_node': 42},
            2: {'text': "Double down on ignoring the problem", 'next_node': 43}
        }
    },

    # Bryan starts feeling conflicted and opens up to someone
    22: {
        'text': "Bryan talks to a counselor about how conflicted he feels. The counselor listens and helps Bryan understand the importance of empathy. Bryan feels better after opening up. What next?",
        'choices': {
            1: {'text': "Apologize to Zach and the others", 'next_node': 44},
            2: {'text': "Continue working on himself quietly", 'next_node': 45}
        }
    },

    # Apologizing to Zach and building a new path
    40: {
        'text': "Bryan approaches Zach after school, apologizing for everything he's done. Zach is cautious but appreciates the gesture. Over time, Bryan continues to show he's changed, and they eventually become acquaintances. What's next?",
        'choices': {
            1: {'text': "Help others who might be going through the same thing", 'next_node': 80},  # Leads to the Good Ending
            2: {'text': "Focus on repairing his own friendships", 'next_node': 81}
        }
    },

    # Bryan's complete redemption (GOOD ENDING)
    80: {
        'text': "Bryan starts helping other students who are dealing with bullying, becoming an advocate for kindness in school. Zach forgives him, and Bryan gains new respect from his peers. He feels proud of the changes he's made. (GOOD ENDING)",
        'choices': {}
    },

    #### **Semi-Good Ending** Path (Partial Redemption, Still Struggling)
    #Bryan makes some efforts to change but still struggles with certain aspects of his past.

    # Working on himself but keeping a distance from Zach
    41: {
        'text': "Bryan decides to focus on improving his own behavior without directly confronting Zach. He makes gradual changes and stops participating in bullying, but there's always a feeling of unresolved tension with Zach.",
        'choices': {
            1: {'text': "Reach out to Zach eventually", 'next_node': 82},
            2: {'text': "Focus on repairing his relationships with other friends", 'next_node': 83}
        }
    },

    # Partial Redemption
    82: {
        'text': "Months later, Bryan finally reaches out to Zach to apologize. Zach accepts the apology but remains distant. Bryan feels better but knows that some damage can never be fully undone. (SEMI-GOOD ENDING)",
        'choices': {}
    },

    # Repairing Friendships but Ignoring Zach
    83: {
        'text': "Bryan fixes his relationships with some old friends and tries to move forward, but the shadow of his actions toward Zach looms. Bryan lives with a sense of lingering guilt but manages to avoid slipping back into old habits. (SEMI-GOOD ENDING)",
        'choices': {}
    },

    #### **Neutral Ending** Path (No Growth, No Deterioration)
    #Bryan doesn't actively harm anyone anymore, but he avoids responsibility and doesn't grow much either.

    # Staying isolated and not dealing with his past
    42: {
        'text': "Bryan avoids confronting his behavior and keeps to himself. He stops bullying, but he also avoids dealing with his emotions. Bryan drifts through school, feeling empty but not causing any more harm.",
        'choices': {
            1: {'text': "Reach out to someone eventually", 'next_node': 84},
            2: {'text': "Keep isolating himself", 'next_node': 85}
        }
    },

    # Complete Neutral Path
    84: {
        'text': "Years later, Bryan reflects on his time in school. He never apologized to Zach, but he also avoided slipping back into toxic behavior. He feels indifferent about his choices, unsure if he really learned anything. (NEUTRAL ENDING)",
        'choices': {}
    },

    #### **Semi-Bad Ending** Path (Trying to Improve but Relapsing)
    #Bryan attempts to change but struggles, eventually falling back into old habits.

    # Relapsing into old behavior
    43: {
        'text': "Bryan tries to be better but keeps getting dragged into old habits. The pressure from his friends and his own insecurities are too strong, and he eventually slips back into bullying.",
        'choices': {
            1: {'text': "Try again to improve", 'next_node': 86},
            2: {'text': "Give up on trying to change", 'next_node': 87}
        }
    },

    # Partial relapse into bullying
    86: {
        'text': "Bryan makes another attempt to distance himself from the group but finds it hard. His friends laugh at his attempts to change, and Bryan finds himself caught in a cycle of trying and failing. (SEMI-BAD ENDING)",
        'choices': {}
    },

    #### **Bad Ending** Path (Total Collapse and Further Isolation)
    #Bryan doesn't learn from his actions, and everything continues to spiral downward, leading to a dark conclusion.

    # Giving up completely
    44: {
        'text': "Bryan gives up on trying to change. He fully immerses himself back into his old ways, bullying others more intensely and isolating himself further from anyone who cares. His grades drop, and he begins to feel like he's lost control of his life.",
        'choices': {
            1: {'text': "Fully embrace the darkness", 'next_node': 88},  # Leads to the Bad Ending
            2: {'text': "Try one last time to get out", 'next_node': 89}
        }
    },

    # Total Collapse (BAD ENDING)
    88: {
        'text': "Bryan spirals out of control. He becomes more aggressive, loses most of his friends, and gets expelled from school. He feels completely alone, with no idea how to fix his life. (BAD ENDING)",
        'choices': {}
    },

    # Continuing downward spiral but with a hint of regret
    89: {
        'text': "Bryan continues down a bad path but occasionally feels pangs of regret. He knows he's too far gone, and the chances of repairing anything seem slim. He wonders if things could have been different. (BAD ENDING)",
        'choices': {}
    },
}