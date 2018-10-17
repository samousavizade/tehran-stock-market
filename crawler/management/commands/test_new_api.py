import asyncio
import logging

from django.core.management.base import BaseCommand

from crawler.helper import update_stock_list

logging.basicConfig(level=logging.DEBUG)


class Command(BaseCommand):
    help = 'test new api'
    requires_migrations_checks = True

    def handle(self, *args, **options):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(update_stock_list())
        loop.close()
