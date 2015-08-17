def addtochart(chart, index, state):
    if state in chart[index]:
        return False
    else:
        chart[index].append(state)
        return True

def closure(grammar,i,x,ab,cd):
    new_state = [(rule[0],[],rule[1],i) for rule in grammar if cd !=[] and rule[0]==cd[0]]
    return new_state

def shift(tokens,i,x,ab,cd,j):
    if cd != [] and tokens[i] == cd[0]:
        return (x,ab+[cd[0]],cd[1:],j)
    else:
        return None

def reductions(chart,i,x,ab,cd,j):
    return [(jstate[0],jstate[1]+[x],jstate[2][1:],jstate[3]) for jstate in chart[j] if cd ==[] and jstate[2] != [] and jstate[2][0] == x]

def parse(tokens,grammar):
    tokens += ["end_of_input_marker"]
    chart = {}
    start_rule = grammar[0]
    for i in range(len(tokens)+1):
        chart[i] = [];
    start_state = (start_rule[0],[],start_rule[1],0)
    chart[0] = [start_state]
    for i in range(len(tokens)):
        while True:
            changes = False
            for state in chart:
                x = state[0]
                ab = state[1]
                cd = state[2]
                j = state[3]

                next_states = closure(grammar,i,x,ab,cd)
                for next_state in next_states:
                    changes = addtochart(chart,i,next_state) or changes

                next_state = shift(tokens,i,x,ab,cd,j)
                if next_state != None:
                    any_changes = addtochart(chart,i+1,next_state) or any_changes

                next_states = reductions(tokens,i,x,ab,cd,j)
                for next_state in next_states:
                    changes = addtochart(chart,i,next_state) or changes

            if not changes:
                break;

# closure tests

grammar = [ 
    ("exp", ["exp", "+", "exp"]),
    ("exp", ["exp", "-", "exp"]),
    ("exp", ["(", "exp", ")"]),
    ("exp", ["num"]),
    ("t",["I","like","t"]),
    ("t",[""])
    ]

print closure(grammar,0,"exp",["exp","+"],["exp"]) == [('exp', [], ['exp', '+', 'exp'], 0), ('exp', [], ['exp', '-', 'exp'], 0), ('exp', [], ['(', 'exp', ')'], 0), ('exp', [], ['num'], 0)]
print closure(grammar,0,"exp",[],["exp","+","exp"]) == [('exp', [], ['exp', '+', 'exp'], 0), ('exp', [], ['exp', '-', 'exp'], 0), ('exp', [], ['(', 'exp', ')'], 0), ('exp', [], ['num'], 0)]
print closure(grammar,0,"exp",["exp"],["+","exp"]) == []


# shift tests

print shift(["exp","+","exp"],2,"exp",["exp","+"],["exp"],0) == ('exp', ['exp', '+', 'exp'], [], 0)
print shift(["exp","+","exp"],0,"exp",[],["exp","+","exp"],0) == ('exp', ['exp'], ['+', 'exp'], 0)
print shift(["exp","+","exp"],3,"exp",["exp","+","exp"],[],0) == None
print shift(["exp","+","ANDY LOVES COOKIES"],2,"exp",["exp","+"],["exp"],0) == None


# reductions test

chart = {0: [('exp', ['exp'], ['+', 'exp'], 0), ('exp', [], ['num'], 0), ('exp', [], ['(', 'exp', ')'], 0), ('exp', [], ['exp', '-', 'exp'], 0), ('exp', [], ['exp', '+', 'exp'], 0)], 1: [('exp', ['exp', '+'], ['exp'], 0)], 2: [('exp', ['exp', '+', 'exp'], [], 0)]}

print reductions(chart,2,'exp',['exp','+','exp'],[],0) == [('exp', ['exp'], ['-', 'exp'], 0), ('exp', ['exp'], ['+', 'exp'], 0)]
