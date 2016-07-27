# python3

class OQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

class JobQueue:
    def read_data(self):
        None
        # self.num_workers, m = map(int, input().split())
        # self.jobs = list(map(int, input().split()))

        # self.num_workers, m = [2,6]
        # self.jobs = [1,2,7,3,1,5]

        # self.num_workers, m = [2,6]
        # self.jobs = [1,8,2,9,3,4]

        # self.num_workers, m = [2,5]
        # self.jobs = [1,2,3,4,5]

        # self.num_workers, m = [4,20]
        # self.jobs = [1]*20

        # self.num_workers, m = [1,10]
        # self.jobs = [1,2,3,4,5,6,7,8,9,10]

        # self.num_workers, m = [4,6]
        # self.jobs = [5,9,8,4,2,7]

        # self.num_workers, m = [7,3]
        # self.jobs = [6,7,8]

        # self.num_workers, m = [3,1]
        # self.jobs = [3]

        # assert (m >= 1) and (m <= 100000)
        # assert m == len(self.jobs)

    def solve(self):
        self.read_data()

        # 1) Fill in free threads
        self.jobs_heap = HeapBuilder()
        self.threads_heap = HeapBuilder()

        self.jobs_heap._build_jobs_heap(self.jobs)

        self._thr_heap = []
        for i in range(self.num_workers):
            if self.jobs_heap.jobs_heap():
                closest_job = self.jobs_heap.ExtractMax('jid')
                self._thr_heap.append({'tid': i, 'start_at': 0, 'finish_at': closest_job['sec']})
        self.threads_heap._build_threads_heap(self._thr_heap)

        # 2) Move jobs into threads heap
        self.threads_heap.SiftUp(len(self.threads_heap.threads_heap())-1)
        length = len(self.jobs_heap.jobs_heap())
        for i in range(length):
            closest_job = self.jobs_heap.ExtractMax('jid')
            # дай тот трэд который быстрее освободится
            most_free_thread = self.threads_heap.ExtractThreadsMax('finish_at')
            self.threads_heap.Insert(closest_job, most_free_thread)

        # 3) Print output
        self.a = []
        self.b = []
        for i in range(len(self.jobs)):
            # print(self.threads_heap.result[i]['tid'], self.threads_heap.result[i]['start_at'])
            self.a.append(self.threads_heap.result[i]['tid'])
            self.b.append(self.threads_heap.result[i]['start_at'])

class HeapBuilder:
    def __init__(self):
        self._data = [] # <- jobs heap
        self.result = [] # <- contains resulting array of jobs execution

    def _build_jobs_heap(self, array):
        for index, el in enumerate(array):
            self._data.append({'jid': index, 'sec': el})

    def _build_threads_heap(self, array):
        self._threads_data = array
        self.result += self._threads_data

    # Heap accessor
    def jobs_heap(self):
        return self._data

    def threads_heap(self):
        return self._threads_data

    def Parent(self, i):
        return i//2

    def LeftChild(self,i):
        return 2*i

    def RightChild(self,i):
        return 2*i + 1

    def swap(self,idx1, idx2):
        self._data[idx1], self._data[idx2] = self._data[idx2], self._data[idx1]

    def swap_threads(self, idx1, idx2):
        self._threads_data[idx1], self._threads_data[idx2] = self._threads_data[idx2], self._threads_data[idx1]

    def SiftDown(self, index, key):
        max_index = index
        array_length = len(self._data) - 1
        l = self.LeftChild(index) + 1
        if (l <= array_length) and (self._data[l][key] < self._data[max_index][key]):
            max_index = l

        r = self.RightChild(index) + 1
        if (r <= array_length) and (self._data[r][key] < self._data[max_index][key]):
            max_index = r

        if index != max_index:
            self.swap(index, max_index)
            self.SiftDown(max_index, key)

    def SiftThreadsDown(self, index, key):
        max_index = index
        array_length = len(self._threads_data) - 1
        l = self.LeftChild(index) + 1
        if (l <= array_length) and (self._threads_data[l][key] < self._threads_data[max_index][key]):
            max_index = l
        if (l <= array_length) and (self._threads_data[l][key] == self._threads_data[max_index][key]):
            if (self._threads_data[l]['tid'] < self._threads_data[max_index]['tid']):
                max_index = l

        r = self.RightChild(index) + 1
        if (r <= array_length) and (self._threads_data[r][key] < self._threads_data[max_index][key]):
            max_index = r

        if index != max_index:
            self.swap_threads(index, max_index)
            self.SiftThreadsDown(max_index, key)
            if (r <= array_length) and (l <= array_length) and (self._threads_data[l][key] == self._threads_data[r][key]) and (self._threads_data[l]['tid'] > self._threads_data[r]['tid']):
                self.swap_threads(l, r)

    def ExtractMax(self, key):
        if len(self._data) > 1:
            result = self._data[0]
            self._data[0] = self._data.pop()
            self.SiftDown(0, key)
            return result
        else:
            return self._data.pop()

    def ExtractThreadsMax(self, key):
        if len(self._threads_data) > 1:
            result = self._threads_data[0]
            self._threads_data[0] = self._threads_data.pop()
            self.SiftThreadsDown(0, key)
            return result
        else:
            return self._threads_data.pop()

    def Insert(self, job, thread):
        _new_thread = {'tid': thread['tid'], 'finish_at': thread['finish_at'] + job['sec'], 'start_at': thread['finish_at']}
        self._threads_data.append(_new_thread)
        self.result.append(_new_thread)
        self.SiftUp(len(self._threads_data)-1)

    def SiftUp(self, index):
        while index > 0:
            parent_index = self.Parent(index)
            parent_node = self._threads_data[parent_index]
            current_node = self._threads_data[index]
            if parent_node['finish_at'] > current_node['finish_at']:
                self.swap_threads(index, parent_index)
            index = parent_index
            # parent_index = self.Parent(index)

# if __name__ == '__main__':
#     job_queue = JobQueue()
#     job_queue.solve()


import random

class MySol(JobQueue):

    def read_data(self, n, jobs):
        self.num_workers = n
        self.jobs = jobs
        # self.len_jobs = len(self.jobs)

    def assign_jobs(self):
        o = JobQueue()
        o.num_workers, m = self.num_workers, len(self.jobs)
        o.jobs = self.jobs
        o.solve()
        return (o.a, o.b)

class OrgSol(OQueue):
    def read_data(self, n, jobs):
        self.num_workers = n
        self.jobs = jobs

    def assign_jobs(self):
        o = OQueue()
        o.num_workers, m = self.num_workers, len(self.jobs)
        o.jobs = self.jobs
        o.assign_jobs()
        o.write_response()
        return (o.assigned_workers, o.start_times)

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

        print("--------NEW TEST--------")
        print("n,m:", n, m)
        print("Jobs:", jobs)
        print("My output:", my_sol)
        print("Ori output:", ori_sol)
        assert my_sol == ori_sol

stress_test(10)
