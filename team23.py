#Team 23: Kris and Kyle
team_name = 'Obey' # Only 10 chars displayed.
strategy_name = 'given'
strategy_description = 'Recognizes kin'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    '''if len(my_history)==0:
        return 'ccbbcc'
    if their_history[:6]=='cccbbb':
        strat='c-til-b'
    elif their_history[:6]=='cccbbc':
        strat='t4t'
    elif their_history[:6]=='bbbbbb':
        strat='all-b'
    elif their_history[:6]=='cccccc':
        strat='all-c'
    elif their_history[:6]=='cbcbcb':
        strat='alt1'
    elif their_history[:6]=='bcbcbc':
        strat='alt2'
    elif their_history[:6]=='cccbcc':
        strat='ret'
    elif their_history[:6]=='bccbbc':
        strat='st4t'
    elif their_history[:6]=='ccccbc':
        strat='t42t'
    else:
        strat='null'
        
    if strat=='t42t' or strat=='t4t' or strat=='st4t' or strat=='ret':
        return 'c'
    elif strat=='c-til-b' or strat=='alt1' or strat=='alt2' or strat=='all-c' or strat=='all-b':
        return 'b'
    else:'''
  #Strategy here
    if len(my_history)%2 == 0:
        return 'c'
    else:
        return 'b'
 
        