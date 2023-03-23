task = []
completed = []

def add(i):
    task.append(i)
    print ('Added ', i, 'to task ')



def delete(i):
    print("n"+i + " is deleted from the list")
    task.remove(i)



def view():
    n = 1
    # print('There are ', n, " Tasks in list")
    print('This items are in our shopping list',      ' '.join(str(x) for x in task))

    for t in task:
        print(str(n)+" : "+t)
        n = n + 1
    n = 1 
    if(completed != []):
        print("Tasks Completed")
        for t in completed:
            print(str(n)+" : "+t)
            n = n + 1
    else:
        print("No task completed yet ")

#itvoyagers.in

def done(i):
    print("n"+ i + " is done")
    task.remove(i)
    completed.append(i)