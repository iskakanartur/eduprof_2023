task = []
completed = []
def add(i):
    task.append(i)

def delete(i):
    print(i + " удалено из начального списка")
    task.remove(i)


def view():
    n = 1
    print('Список продуктов который нужно купить:', ' '.join(str(x) for x in task))
    for t in task:
        print(str(n)+" : "+t)
        n = n + 1
    n = 1
    if(completed != []):
        print("Список уже купленных продуктов")
        for t in completed:
            print(str(n)+" : "+t)
            n = n + 1
    else:
        print("Мы пока ничего не купили")
    print ('*******************END OF VIEW FUNCTION ************')



def done(i):
    print(i + " уже куплено")
    task.remove(i)
    completed.append(i)


