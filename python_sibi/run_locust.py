from locust import HttpUser, task, between
from locust.main import main

# Your Locust test scenario
class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def index(self):
        self.client.get("/")

if __name__ == "__main__":
    # Run Locust by invoking the Python script from the command line
    import sys
    from locust.main import main

    # Append the locustfile.py to sys.argv to simulate the command line arguments
    sys.argv.append("-f")
    sys.argv.append("locustfile.py")
    sys.argv.append("--host")
    sys.argv.append("http://localhost:5000/")
    sys.argv.append("--user")
    sys.argv.append("5000")
    sys.argv.append("--spawn-rate")
    sys.argv.append("20")

    # Call the main() function to start Locust
    main()
