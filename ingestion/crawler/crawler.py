from ingestion.crawler.past_sales_page import PastSalesPage


class Crawler:
    def __init__(self):
        self.past_sales_page = PastSalesPage()

    def run(self):
        self.past_sales_page.run()