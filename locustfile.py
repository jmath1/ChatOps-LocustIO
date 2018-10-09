from locust import HttpLocust, TaskSet, task



class UserBehavior(TaskSet):

    @task(1)
    def firstTask(self):
        self.client.get("/first-task")

    @task(2)
    def secondTask(self):
        self.client.get("/second-task")

    @task(3)
    def thirdTask(self):
        self.client.get("/third-task")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 8000
