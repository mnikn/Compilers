import graphics

def interpret(trees):
    for tree in trees:
        nodetype[0] = tree[0]
        if nodetype == 'word-element':
            graphics.word(tree[1])
        elif nodetype == 'tag-element':
            tagname = tree[1]
            tagargs = tree[2]
            subtrees = tree[3]
            closetagname = tree[4]
            if tagname != closetagname:
                graphics.warning("miscatch tag!")
            else:
                graphics.begintag(tagname,tagargs)
                interpret(subtrees)
                graphics.endtag()

def eval_exp(tree,environment):
    nodetype = tree[0]
    if nodetype == "number":
        return float(tree[1])
    elif nodetype == "string":
        return exp[1] 
    elif nodetype == "true":
        return True
    elif nodetype == "false":
        return False
    elif nodetype == "not":
        return not(eval_exp(exp[1], env))
    elif nodetype == "binop":
        left_child = eval_exp(tree[1],environment)
        operator = tree[2]
        right_child = eval_exp(tree[3],environment)
        if operator == "+":
            return left_value + right_value
        elif operator == '-':
            return left_value - right_value
    elif nodetype == 'identifier'
        variable_name = tree[1]
        return environment[name]

def eval_elt(tree,environment):
    elttype = tree[0]
    if elttype == "function":
        fname = tree[1]
        fparams = tree[2]
        fbody = tree[3]

        fvalue = ("function",fparams,fbody,environment)
        add_to_env(environment,fname,fvalue)

def eval_stmt(tree,environment):
    stmttype = tree[0]
    if stmttype == "call":
        frame = tree[1] # "sqrt"
        args = tree[2]  # [("number","2")]
        fvalue = env_lookup(frame,environment)
        if fvalue[0] == "function":
            fparams = fvalue[1]
            fbody = fvalue[2]
            fenv = fvalue[3]
        if len(fparams) != len(args):
            print "ERROR : wrong number of args"
        else:
            new_env = (fenv,{})
            for i in range(len(args)):
                argval = eval_exp(args[i],env)
                new_env[fparams[i]] = argval
            try:
                eval_stmts(fbody,new_env)
                return None
            except Exception as return_value:
                return return_value
    else:
        print "ERROR: call to non-function"
        
    if stmttype == "assign":
        variable_name = tree[1]
        right_child = tree[2]
        new_value = eval_exp(right_child,environment)
    elif stmttype == "if-then-else":
        conditional_exp = tree[1]
        then_stmts = tree[2]
        else_stmts = tree[3]
    elif stmttype == "return":
        return_exp = true[1]
        retn = eval_exp(return_exp,environment)
        raise Exception(retn)

def env_update(varible_name,value,environment):
    if varible_name in environment[1]:
        environment[1][variable_name] = value
    elif not(env[0] == None):
        env_update(variable,value,environment[0])
        
        

def env_lookup(varible_name,environment):
    if varible_name in environment[1]:
        return environment[1][varible_name]
    elif emvironment[0] == None:
        return None
    else:
        return env_loopup(variable_name,emvironment[0])
