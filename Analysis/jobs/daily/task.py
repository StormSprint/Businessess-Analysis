from django_extensions.management.jobs import BaseJob

from Analysis.analysis import contractAnalysis


class Job(BaseJob):
    help = "My sample job."

    def execute(self):
        contractAnalysis()