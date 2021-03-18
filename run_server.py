from amazon_scraper_app import my_app
from amazon_scraper_app.models.database_models import db
from amazon_scraper_app.server import ScraperApp


if __name__ == '__main__':
    f_app = ScraperApp(my_app, db)
    f_app.run()
