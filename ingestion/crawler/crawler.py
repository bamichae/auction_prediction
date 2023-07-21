from ingestion.crawler.past_sales import PastSales


class Crawler:
    def __init__(self):
        self.past_sales = PastSales()

    def run(self):
        self.past_sales.run()