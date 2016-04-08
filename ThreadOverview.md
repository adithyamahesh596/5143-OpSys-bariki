Name: Adithya Mahesh Bariki
Course: 5143 Operating Sysytems
Date: 08 April 2016
Mustangs ID: M20227682

#Question 1

Explain the differences between Threads1 and Threads2 using lines from the code and a precise explanation.

Threads1.py has threads that run independently which have copies of their local variables so that we dont need to have access to same memory space.
While coming to the case in Threads2.py there is a variable named shared counter where the threads of the program try to access together during execution
and this arises complex condition.

#Question 2

After running Thread3.py does it fix the problems that occured in Threads2.py? What's the down-side?

Thread3.py has the set of instructions which fixes the complex/race condition by using lock method, i.e.,
when a single thread has the chance of access to global variable, it locks this access to this global variable so that 
no thread cannot access it.
By following this mechanism, the total execution time increases.

#Question 3

Comment out the join statements at the bottom of the program and describe what happens.

When we comment out join the print statement in the main program is executed
and the threads of the program are still executing.This clearly indicates that
when join is included in the code the main program waits for all the threads 
to be executed and then the main thread will be executed. 


#Question 4

What happens if you try to Ctrl-C out of the program before it terminates?

The execution flow of the threads never ends and this results program's abnormal behaviour.

#Question 5

Read and run Threads4.py. This generates a different and more ridiculous race condition.
Write concise explanation of what's happening to cause this bizarre behavior using lines from the code and precise explanation.

The situation in this program here is each and every thread tries to intiate or assign a value to 
the variable.The complexity here is when a thread requests for global variable, another thread may
be working on that global variable and this leads to the situation where the contents are altered 
and this gives incorrect value to the thread which is requesting the resource.So, in this situation
both the threads keep on running , both resulting in incorrect values.

#Question 6

Does uncommenting the lock operations clear up the problem in question 5?

Yes when the lock section is uncommented, each thread has exclusive right to sharedNumber at a specific point 
in time and neither thread prints hat was weird because they both have correct values at everyy point during the execution.
