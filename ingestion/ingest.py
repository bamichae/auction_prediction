from ingestion.crawler.crawler import Crawler


class Ingest:
    def __init__(self):
        self.crawler = Crawler()

    def run(self):
        self.crawler.run()


if __name__ == "__main__":
    ingest = Ingest()
    ingest.run()
