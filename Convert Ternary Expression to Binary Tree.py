def convert_expression(expression, i):
    #code here
    if i >= len(expression):
        return 
    root=Node(expression[i])
    i+=1
    if i < len(expression):
        if expression[i]=="?":
            root.left=convert_expression(expression, i+1)
        elif expression[i]==":":
            root.right=convert_expression(expression, i+1)
    return root