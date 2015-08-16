import re

edges = {(1,'q'):1}
accepting = [1]
string = "99999"

def fsm(string,current,edges,accepting):
    if string == '':
        return current in accepting
    else:
        letter = string[0]
        if (current,letter) in edges:
            destation = edges[(current,letter)]
            return fsm(string[1:],destation,edges,accepting)
        else:
            return False

def nfsm(string, current, edges, accepting): 
    if string =='':
        return current in accepting
    else:
        letter = string[0]
        if(current,letter) in edges:
            destation_list = edges[(current,letter)]
            for i in destation_list:
                if nfsm(string[1:],i,edges,accepting):
                    return True
        return False

print fsm(string,1,edges,accepting)
