#OPERATING SYSTEMS PROJECT
#CPU Scheduling and Banker's Algorithm


PROGRAM:
Python


DESCRIPTION

This program demonstrates CPU Scheduling and
Banker's Algorithm.

The CPU Scheduling part has two algorithms:

1. FCFS
2. Round Robin


FCFS

FCFS means First Come First Serve.

The process that arrives first will run first.
The process will finish before the next process runs.


ROUND ROBIN

Round Robin gives each process a fixed amount of
CPU time called Time Quantum.

If the process is not finished, it goes back to
the queue and waits for another turn.


CPU SCHEDULING INPUT

- Number of processes
- Arrival Time
- Burst Time
- Time Quantum for Round Robin


CPU SCHEDULING OUTPUT

- Gantt Chart
- Completion Time
- Waiting Time
- Turnaround Time
- Average Waiting Time
- Average Turnaround Time


FORMULAS

Turnaround Time = Completion Time - Arrival Time

Waiting Time = Turnaround Time - Burst Time


BANKER'S ALGORITHM

Banker's Algorithm checks if the system is safe
or unsafe.

It uses:

- Allocation Matrix
- Maximum Matrix
- Available Resources


NEED FORMULA

Need = Maximum - Allocation


HOW TO RUN

Open the folder in a terminal.

Type:

python main.py

Press Enter.

The program will show a menu.

Choose:

1 - CPU Scheduling
2 - Banker's Algorithm
3 - Exit
