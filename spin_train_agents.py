import trains
import time
import datetime
import os

from trains.backend_api import Session
from trains.backend_api.services import tasks, events, projects, queues, workers

PERIOD_BETWEEN_WORKER_CREATION = 30
KILL_IDLE_WORKER_PERIOD = 60
MAX_WORKERS = 10

session = Session()
last_worker_created_timestamp = 0
since_when_worker_idle = {}

while True:
    num_workers = 0
    res = session.send(workers.GetAllRequest())
    for worker in res.response.workers:
        if worker.id.startswith('slurm_worker_'):
            slurm_job_id = worker.id.split('_')[2]
            timestamp = datetime.datetime.now().timestamp()
            num_workers += 1

            print(worker)
            print(worker.id, worker.task, slurm_job_id)

            if worker.task is not None or slurm_job_id not in since_when_worker_idle:
                since_when_worker_idle[slurm_job_id] = timestamp
            elif since_when_worker_idle[slurm_job_id] + KILL_IDLE_WORKER_PERIOD < timestamp:
                command = f'scancel {slurm_job_id}'
                print(f'Killing worker {worker.id}. Executing {command}.')
                os.system(command)

    task_list = trains.Task.get_tasks(task_filter=dict(system_tags=["-archived"], status=["queued"]))
    print(len(task_list))
    if num_workers < MAX_WORKERS and len(task_list) > 0 and datetime.datetime.now().timestamp() > last_worker_created_timestamp + PERIOD_BETWEEN_WORKER_CREATION:
        last_worker_created_timestamp = datetime.datetime.now().timestamp()
        print(f'Creating a new worker at timestamp={last_worker_created_timestamp}.')
        os.system('sbatch /home/cygan/utils/job_trains_agent.sh')

    time.sleep(1)
