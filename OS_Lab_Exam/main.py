#FCFS - NON-PREEMTIVE

def fcfs(processes):
    processes.sort(key=lambda x: x[1])

    time = 0
    gantt_chart = []
    results = []

    for p in processes:
        name = p[0]
        arrival_time = p[1]
        burst_time = p[2]

#If CPU has no process yet
        if time < arrival_time:
            time = arrival_time

        start = time 

#Process runs until finished
        time = time + burst_time
        completion_time = time

#Calculate turnaround time
        turnaround_time = completion_time - arrival_time

#Calculate waiting time
        waiting_time = turnaround_time - burst_time

        gantt_chart.append((name, start, completion_time))
        results.append([name, arrival_time, burst_time, completion_time, waiting_time, turnaround_time])

    return gantt_chart, results

#ROUND ROBIN

def round_robin(processes, quantum):
    processes.sort(key=lambda x: x[1])

#Copy burst time
    remaining = []

    for p in processes:
        remaining.append(p[2])

#Completion time
    completion_time = [0] * len(processes)

 #Queue
    queue = []
    time = 0
    finished = 0
    gantt_chart = []

 #Add first process
    queue.append(0)

    added = [False] * len(processes)
    added[0] = True

    while finished < len(processes):

 #If queue is empty, find next process
        if len(queue) == 0:
            for i in range(len(processes)):
                if not added[i] and processes[i][1] <= time:
                    queue.append(i)
                    added[i] = True

#Get first process
        i = queue.pop(0)
        name = processes[i][0]
        start = time

# Decide how long the process will run
        if remaining[i] > quantum:
            time = time + quantum
            remaining[i] = remaining[i] - quantum 
        else:
            time = time + remaining[i]
            remaining[i] = 0
            completion_time[i] = time
            finished = finished + 1

        gantt_chart.append((name, start, time))

#Add processes that have arrived
        for j in range(len(processes)):
            if not added[j] and processes[j][1] <= time:
                queue.append(j) 
                added[j] = True

#If process is not finished

        if remaining[i] > 0:
            queue.append(i)

    results = []

    for i in range(len(processes)):
        name = processes[i][0]
        arrival_time = processes[i][1]
        burst_time = processes[i][2]
        turnaround_time = completion_time[i] - arrival_time
        waiting_time = turnaround_time - burst_time
        results.append([name, arrival_time, burst_time, completion_time[i], waiting_time, turnaround_time])

    return gantt_chart, results
                                        
# SHOW GANTT CHART

def show_gantt(gantt_chart):
    print("\n Gantt Chart: ")

    for item in gantt_chart:
        name = item[0]
        start = item[1]
        end = item[2]

        print("|", name, "(", start, "-", end, ")", end=" ")
    print("|")

# SHOW RESULTS

def show_results(gantt_chart, results):

    show_gantt(gantt_chart)
    print("\nProcess\tAT\tBT\tCT\tWT\tTAT")
    print("---------------")

    total_waiting = 0
    total_turnaround = 0

    for p in results:
        print(
            p[0], "\t",
            p[1], "\t",
            p[2], "\t",
            p[3], "\t",
            p[4], "\t",
            p[5]
        )

        total_waiting = total_waiting + p[4]
        total_turnaround = total_turnaround + p[5]

    average_waiting = total_waiting / len(results)
    average_turnaround = total_turnaround / len(results)

    print("\nAverage Waiting Time:",
          round(average_waiting, 2))

    print("Average Turnaround Time:",
          round(average_turnaround, 2))


# CPU SCHEDULING

def cpu_scheduling():

    print("\n---- CPU Scheduling ----")

    number = int(input("Number of processes: "))

    processes = []

    # Get process information
    for i in range(number):

        print("\nProcess P" + str(i))

        arrival = int(input("Arrival Time: "))
        burst = int(input("Burst Time: "))

        processes.append(
            ["P" + str(i), arrival, burst]
        )

    print("\nChoose Algorithm")
    print("1. FCFS")
    print("2. Round Robin")

    choice = int(input("Choice: "))

    # FCFS
    if choice == 1:

        gantt, results = fcfs(processes)

        print("\n---- FCFS ----")

        show_results(gantt, results)

    # Round Robin
    elif choice == 2:

        quantum = int(input("Time Quantum: "))

        gantt, results = round_robin(
            processes, quantum
        )

        print("\n---- Round Robin ----")

        show_results(gantt, results)

    else:

        print("Invalid choice.")



# BANKER'S ALGORITHM

def bankers_algorithm():

    print("\n---- Banker's Algorithm ----")

    number = int(input("Number of processes: "))
    resources = int(input("Number of resources: "))

    # Get Allocation Matrix
    print("\nEnter Allocation Matrix")

    allocation = []

    for i in range(number):

        print("P" + str(i), end=": ")

        row = list(map(int, input().split()))

        allocation.append(row)

    # Get Maximum Matrix
    print("\nEnter Maximum Matrix")

    maximum = []

    for i in range(number):

        print("P" + str(i), end=": ")

        row = list(map(int, input().split()))

        maximum.append(row)

    # Get Available Resources
    print("\nEnter Available Resources")

    available = list(
        map(int, input().split())
    )

    # Calculate Need Matrix
    need = []

    for i in range(number):

        row = []

        for j in range(resources):

            value = maximum[i][j] - allocation[i][j]

            row.append(value)

        need.append(row)

    # Show Need Matrix
    print("\nNeed Matrix:")

    for i in range(number):

        print("P" + str(i) + ":", need[i])

    # Check if system is safe
    work = available.copy()

    finished = [False] * number

    safe_sequence = []

    while len(safe_sequence) < number:

        found = False

        for i in range(number):

            if finished[i]:
                continue

            can_finish = True

            # Check resources
            for j in range(resources):

                if need[i][j] > work[j]:

                    can_finish = False

            # Process can finish
            if can_finish:

                # Give back allocated resources
                for j in range(resources):

                    work[j] = work[j] + allocation[i][j]

                finished[i] = True

                safe_sequence.append("P" + str(i))

                found = True

        # No process can finish
        if not found:
            break

    # Show result
    if len(safe_sequence) == number:

        print("\nSystem is in a Safe State.")

        print(
            "Safe Sequence:",
            " -> ".join(safe_sequence)
        )

    else:

        print("\nSystem is in an Unsafe State.")

        print("No safe sequence exists.")



# MAIN MENU

def main():

    while True:

        print(" Operating System Simulator")
        print("1. CPU Scheduling")
        print("2. Banker's Algorithm")
        print("3. Exit")

        choice = int(
            input("Enter your choice: ")
        )

        if choice == 1:

            cpu_scheduling()

        elif choice == 2:

            bankers_algorithm()

        elif choice == 3:

            print("Program ended.")
            break

        else:

            print("Invalid choice.")


# Start program
main()
                                            