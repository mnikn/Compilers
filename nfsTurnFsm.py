def nfsmaccepts(current,edges,accepting,visited): 
    if current in visited:
        return None
    elif current in accepting:
        return ""
    else:
        newvisited = visited + [current]
        for edge in edges:
            if edge[0] == current:
                for newstate in edges[edge]:
                    foo = nfsmaccepts(newstate,edges,accepting,newvisited)
                    if foo != None:
                        return edge[1] + foo
        return None

def nfsmtrim(edges, accepting): 
    # find live states
    states = []
    for e in edges:
        states += [e[0]] + edges[e]
    live = []
    for s in states:
        if nfsmaccepts(s,edges,accepting,[])!= None:
            live += [s]

    # translate to finite state machine

    #create new edges
    new_edges = {}
    for e in edges:
        if e[0] in live:
            new_destation = []
            for destation in edges[e]:
                if destation in live:
                    new_destation += [destation]
            if new_destation != []:
                new_edges[e] = new_destation

    #create new accepting
    new_accepting = []
    for s in accepting:
        if s in live:
            new_accepting += [s]
            
    return (new_edges,new_accepting)


grammar = [ 
    ("exp", ["exp", "+", "exp"]),
    ("exp", ["exp", "-", "exp"]),
    ("exp", ["(", "exp", ")"]),
    ("exp", ["num"]),
    ]

def cfgempty(grammar,symbol,visited):
    if symbol in visited:
        return None
    elif not any([rule[0] == symbol for rule in grammar]):
        return [symbol]
    else:
        new_visited = visited + [symbol]
        for rhs in [r[1] for r in grammar if r[0] == symbol]:
            if all([None!= cfgempty(grammar,r,new_visited) for r in rhs]):
                result = []
                for r in rhs:
                    result += cfgempty(grammar,r,new_visited)
                return result
    return None

def cfginfinite(grammar):
    for q in [rule[0] for rule in grammar]:
        def helper(current,visited,sizexy):
            if current in visited:
                return sizexy>0
            else:
                new_visited = visited + [current]
                for rhs in [rule[1] for rule in grammar if rule[0]==current]:
                    for symbol in rhs:
                        if helper(symbol,new_visited,sizexy+len(rhs)-1):
                            return True
                return False

        if helper(q,[],0):
            return True
    return False




def expand(tokens_and_derivation,grammar):
    (tokens,derivation) = tokens_and_derivation
    for token_pos in range(len(tokens)):
        for rule_index in range(len(grammar)):
            rule = grammar[rule_index]
            if tokens[token_pos] == rule[0]:
                yield ((tokens[0:token_pos] + rule[1] + tokens[token_pos+1:]),derivation + [rule_index])

def isambig(grammar,start,utterance):
    enumerated = [([start],[])]
    while True:
        new_enumerated = enumerated

        for u in enumerated:
            for i in expand(u,grammar):
                if not i in new_enumerated:
                    new_enumerated += [i]
        
        if new_enumerated != enumerated:
            enumerated = new_enumerated
        else:
            break;
    return len([x for x in enumerated if x[0] == utterance]) > 1
            
