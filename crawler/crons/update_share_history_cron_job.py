from django.core import management
from django_cron import CronJobBase, Schedule


class UpdateShareHistoryCronJob(CronJobBase):
    EVERY_MINS = 4 * 60
    RETRY_AFTER_FAILURE_MINS = 5

    schedule = Schedule(run_every_mins=EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'crawler.daily_update_share_history_cron_job'  # a unique code

    def do(self):
        management.call_command("update_share_history")