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
            
            
