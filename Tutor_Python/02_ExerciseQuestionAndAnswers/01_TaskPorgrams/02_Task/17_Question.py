# 17. In a company, worker efficiency is determined on the basis of the time required for a worker to complete a particular job. If the time taken by the worker is between 2 – 3 hours, then the worker is said to be highly efficient. If the time required by the worker is between 3 – 4 hours, then the worker is ordered to improve speed. If the time taken is between 4 – 5 hours, the worker is given training to improve his speed, and if the time taken by the worker is more than 5 hours, then the worker has to leave the company. If the time taken by the worker is input through the keyboard, find the efficiency of the worker.


hrs = float(input("Enter the Time Taken by Worker : "))
if(hrs>=2 and hrs<=3):
	print("Worker is Highly Efficient..")
elif(hrs>3 and hrs <=4):
	print("Worker Needs to Improve Speed..")
elif(hrs>4 and hrs <=5):
	print("Give Training to Worker..")
else:
	print("Worker is Leave the Company..")