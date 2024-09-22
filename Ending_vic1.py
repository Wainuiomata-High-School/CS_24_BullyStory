victim_story = {
    1: {
        'text': "This is Zach every day he dreads going to school because of the teasing from some classmates. Today, the teasing starts again. What should he do?",
        'choices': {
            1: {'text': "Ignore them and walk away", 'next_node': 2},
            2: {'text': "Tell a teacher about the bullying", 'next_node': 3}
        }
    },
    2: {
        'text': "He tries to ignore the teasing, but it still hurts. You feel alone and scared. What do you do next?",
        'choices': {
            1: {'text': "Tell a friend about how he feels", 'next_node': 4},
            2: {'text': "Keep it to himself", 'next_node': 5}
        }
    },
    3: {
        'text': "He tells a teacher about the bullying. The teacher listens and promises to help. The bullying stops, and he feels safer at school. The end.",
        'choices': {
            1: {'text': "Restart", 'next_node': 1}
        }
    },
    4: {
        'text': "He tells a friend about how he feels. They support Zach and help him talk to a teacher. The teacher helps, and the bullying stops. The end.",
        'choices': {
            1: {'text': "Restart", 'next_node': 1}
        }
    },
    5: {
        'text': "Zach keeps his feelings to Himself, and the bullying continues. He starts to feel more isolated and depressed. What should hedo?",
        'choices': {
            1: {'text': "Try to make new friends", 'next_node': 6},
            2: {'text': "Withdraw further into Himself", 'next_node': 7}
        }
    },
    6: {
        'text': "Zach tries to make new friends and find a group that accepts him. The bullying doesn't stop completely, but he feels less alone. The end.",
        'choices': {
            1: {'text': "Restart", 'next_node': 1}
        }
    },
    7: {
        'text': "Zach withdraws further into himself, and the bullying continues. His grades start to suffer, and he feels hopeless. What should he do?",
        'choices': {
            1: {'text': "Seek help from a counselor", 'next_node': 8},
            2: {'text': "Continue to keep it to himself", 'next_node': 9}
        }
    },
    8: {
        'text': "Zach seeks help from a counselor. They provide support and help Zach build resilience. The bullying continues, but he learns how to deal with it and starts to feel better. The end.",
        'choices': {
            1: {'text': "Restart", 'next_node': 1}
        }
    },
    9: {
        'text': "Zach continues to keep it to yourself, and your mental health deteriorates. You feel increasingly isolated. The end.",
        'choices': {
            1: {'text': "Restart", 'next_node': 1}
        }
    },
    10: {
        'text': "The bullying takes a toll on Zach, and he feels like He can't go on. In a moment of desperation, Zach reaches out to a trusted adult for help. What do they do?",
        'choices': {
            1: {'text': "They provide support and take action", 'next_node': 11},
            2: {'text': "They don't take his concerns seriously", 'next_node': 12}
        }
    },
    11: {
        'text': "The trusted adult provides support and takes action. The bullying stops, and he starts to rebuild his confidence. The end.",
        'choices': {
            1: {'text': "Restart", 'next_node': 1}
        }
    },
    12: {
        'text': "The trusted adult doesn't take his concerns seriously. Zach feels more alone than ever. He considers his options. What should Zach do?",
        'choices': {
            1: {'text': "Try to seek help from another source", 'next_node': 13},
            2: {'text': "Give up trying to get help", 'next_node': 14}
        }
    },
    13: {
        'text': "Zach seeks help from another source, and this time, He is heard. They take action, and the bullying decreases. He feels a sense of hope. The end.",
        'choices': {
            1: {'text': "Restart", 'next_node': 1}
        }
    },
    14: {
        'text': "Zach gives up trying to get help, and the bullying continues. He feel hopeless and isolated. The end.",
        'choices': {
            1: {'text': "Restart", 'next_node': 1}
        }
    }
}
