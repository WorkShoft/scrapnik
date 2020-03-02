This project uses the Django web framework and the Scrapy framework to show how scraping can be automated by using periodic tasks with Celery tasks and workers, and how easy it is to integrate Scrapy in a Django project.

The scraped sites are furniture catalogs of sites such as Carrefour's and Ikea's. These sites are interesting because they have pagination and complex elements.

Some of the interesting features are:
- A custom Django command that runs a specific spider
- A custom Django command that runs all spiders
- Usage of Cloudflare-scrapy to scrape Cloudflare-protected sites
- Usage of Scrapy-DjangoItem to create a pipeline that deserializes the Scrapy data to Django objects, validates them and saves them to the Django project's database

This is the complete stack:

- Docker with Docker Compose
- Python 3.7
- PostgreSQL
- Django
- Celery
- RabbitMQ
- Scrapy 
