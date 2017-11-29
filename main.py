import psutil

procs = psutil.pids()
print('   ID  |                         Name  |    Status')
print('--------------------------------------------------')
for x in procs:
    p = psutil.Process(x)
    print('%6s |%30s |%10s' % (str(x), p.name(), p.status()))
done = True
while done:
    print('If you want a detailed information about any process, type its ID, or type "exit" to exit.')
    print('Type "delete" if you want to kill a process.')
    quest = raw_input()
    if quest == 'exit':
        done = False
    elif quest == 'delete':
        print('Type ID of the process you want to kill.')
        target = raw_input()
        for proc in psutil.process_iter():
            if proc.pid == int(target):
                to_kill = psutil.Process(proc.pid)

                if to_kill.username != 'SYSTEM':
                    proc.kill()
    elif int(quest) in procs:
        p = psutil.Process(int(quest))
        print('ID: ' + quest)        
        print('Name: ' + p.name())        
        print('Status: ' + p.status())        
        # print('Terminal: ' + p.terminal())       
        print('CPU percent: ' + str(p.cpu_percent()))        
        print('Memory percent: ' + str(p.memory_percent()))
        print('Open files: ' + str(p.open_files()))
    else:
        print("There is no such process.")