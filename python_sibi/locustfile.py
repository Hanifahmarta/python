from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)  # Wait time between 1 and 5 seconds

    @task
    def index(self):
        self.client.get("/")
