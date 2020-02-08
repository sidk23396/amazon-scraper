from amazon_scraper_app.server import my_app

if __name__ == '__main__':
    my_app.init_db()
    my_app.run()
