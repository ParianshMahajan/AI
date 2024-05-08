import copy

stack=[]
visited=[]

def DFS(s,g):
    stack.append(s)
    while True:
        curr=stack.pop()
        visited.append(curr)
        print('Steps are : ', curr)
        if(curr in g):
            print(curr)
            print('Goal Achieved')
            return
        
        curr1=copy.deepcopy(curr)
        curr2=copy.deepcopy(curr)
        curr3=copy.deepcopy(curr)
        curr4=copy.deepcopy(curr)
        curr5=copy.deepcopy(curr)
        curr6=copy.deepcopy(curr)

        if curr1[0]:
            curr1[1].append(curr1[0].pop())
            if curr1 not in visited:
                stack.append(curr1)

        
        if curr2[0]:
            curr2[2].append(curr2[0].pop())
            if curr2 not in visited:
                stack.append(curr2)

        if curr3[1]:
            curr3[2].append(curr3[1].pop())
            if curr3 not in visited:
                stack.append(curr3)

        if curr4[1]:
            curr4[0].append(curr4[1].pop())
            if curr4 not in visited:
                stack.append(curr4)

        if curr5[2]:
            curr5[1].append(curr5[2].pop())
            if curr5 not in visited:
                stack.append(curr5)

        if curr6[2]:
            curr6[0].append(curr6[2].pop())
            if curr6 not in visited:
                stack.append(curr6)

        if not stack:
            print('Not Found')
            return

initial_State=[['a'],['b','c'],[]]
final_State=[[[],['a','b','c'],[]],[['a','b','c'],[],[]],[[],[],['a','b','c']]]
DFS(initial_State,final_State)


