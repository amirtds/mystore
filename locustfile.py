from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  # Users wait 1-3 seconds between tasks

    @task
    def index_page(self):
        self.client.get("/store/")

    @task(3)
    def view_product_detail(self):
        self.client.get("/store/product/smartphone/")

    @task(2)
    def view_checkout_page(self):
        self.client.get("/store/checkout/smartphone/")