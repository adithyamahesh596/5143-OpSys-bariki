# Chapter 3 Review Questions
Name: Adithya Mahesh Bariki
Course: 5143 Operating Systems
Date:02 Mar 2016


## What does it mean to preempt a process?

The operating system moves a process from running to ready without the process requesting it and this phenomenon is called as Preemption. A process can be preempted at any time if the kernel finds that a higher-priority process is now dispatchable.


## What is swapping and what is its purpose?
 
Swapping is the process of exchanging data between the RAM and hard disk.o maximize the number of processes in the system, we swap a process from the ready state to the ready suspend state. 
Purpose:The purpose of swapping, is to access data being stored in hard disk and to bring it into the RAM so that it can be used by the application program. Excessive Swapping Causes Thrashing 


## List three general categories of information in a process control block.

The three general categories of information in a process control block are
1.Process Identification:A unique numeric identifier has been assigned to a process.
2.Process State Information:This is the information about contents of the process registers.
Some of them are:User-visible registers,Control and Status registers.Status information is 
stored in Program Status Word(PSW).
3.Process Control Information:The additional information needed by the Operating system to control
and coordinate the various active processes is called Proces Control Information.


## Why are two modes (user and kernel) needed?

Kernel mode:In kernel mode, the CPU has instructions to manage memory and how it can be accessed, plus the ability to access peripheral 
devices like disks and network cards. The CPU can also switch itself from one running program to another.

User mode:In user mode, access to memory is limited to only some memory locations, and access to peripheral devices is denied. 
The ability to keep or relinquish the CPU is removed, and the CPU can be taken away from a program at any time.


## What is the difference between an interrupt and a trap?

An alternative way for the system to find out when input has arrived, or when output has been completed, is to use interrupts. If you need to disallow hardware interrupts until a trap is served, you need to explicitly clear the interrupt flag. And usually the interrupt flag on the computeraffects (hardware) interrupts as opposed to traps. This means that clearing thisflag will not prevent traps.Unlike traps, interrupts should preserve the previous state of the CPU.Occurrences of hardware interrupts usually disable other hardware interrupts, but this is not true for traps. A trap is a software generated interrupt caused by an exception or by an explicit instruction


## Give three examples of an interrupt.

Hardware interrupt: When a power suppy failure occurs and when a reset button is pressed.

Software interrupt:when an error is occured in a software then it sends a signal to the CPU to run instructions to clear the error.

Timer interrupt: A data logging application which must read input sensor for every one second.


## What is the difference between a mode switch and a process switch?

Process switch:
A process switch is what it is called when the processor switches from one process to another process.
The old program is no longer executing, but it's state is saved in memory for when the kernel decides that it is ready to execute it again

Mode switch:
A mode switch is what is referred to when the cpu changes privilege levels. The kernel works at a higher privilege than a standard user task

Difference:
In process switch,the old program is no longer executing, but it's state is saved in memory for when the kernel decides that it is ready to execute it again
but in the mode switch the currently executing process doesn't change. Generally a mode switch is considered less expensive compared to a process switch.


