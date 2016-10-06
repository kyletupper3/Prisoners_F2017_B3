####

# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

#Team 3: Kris and Kyle
team_name = 'Reaper' # Only 10 chars displayed.
strategy_name = 'Hungry Grim Trigger'
strategy_description = 'Colludes until betrayed. If betrayed, betrays until game is over. If ahead in score after 10 turns, betrays.'
    
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
    if len(my_history)==0:
        return 'c'
    elif their_score<my_score and len(my_history)>9:
        return 'b'
    elif 'b' in their_history:
        return 'b'
    else:
        return 'c'
 
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             