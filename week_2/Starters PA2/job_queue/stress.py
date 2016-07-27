# python3
from jq import JobQueue #Import your solution
from original import OQueue #Import original naive solution

import random

class MySol(JobQueue):

    def read_data(self, n, jobs):
        self.num_workers = n
        self.jobs = jobs
        self.len_jobs = len(self.jobs)

    def assign_jobs(self):
        JobQueue.assign_jobs(self)
        return (self.assigned_workers, self.start_times)

class OrgSol(OQueue):
    def read_data(self, n, jobs):
        self.num_workers = n
        self.jobs = jobs

    def assign_jobs(self):
        OQueue.assign_jobs(self)
        return (self.assigned_workers, self.start_times)

def stress_test(tests_amount):

    my = MySol()
    ori = OrgSol()

    for test in range(tests_amount):
        n = random.randrange(1, 50)
        m = random.randrange(1, 50)
        jobs = [random.randrange(1,10) for _ in range(m)]

        my.read_data(n, jobs[::])
        ori.read_data(n, jobs[::])

        my_sol = my.assign_jobs()
        ori_sol = ori.assign_jobs()

        print "--------NEW TEST--------"
        print "n,m:", n, m
        print "Jobs:", jobs
        print "My output:", my_sol
        print "Ori output:", ori_sol
        assert my_sol == ori_sol

#stress_test(100)
