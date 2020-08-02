from django.db import models
from accounts.models import User

# Create your models here.
class Report(models.Model):
    user = models.ForeignKey(User, related_name='reports', on_delete=models.CASCADE)
    report_type = models.IntegerField(default=0,)
    date_added = models.DateTimeField(auto_now_add=True,)
    
    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return str(self.id)+" "+str(self.report_type)+" "+str(self.date_added)

class ReportInfo(models.Model):
    report = models.ForeignKey(Report, related_name='parameter_info', on_delete=models.CASCADE)
    parameter = models.CharField(max_length=100,)
    value = models.IntegerField(blank=True,)
    upper_limit = models.IntegerField(blank=True,)
    lower_limit = models.IntegerField(blank=True,)

    class Meta:
        unique_together = ['report', 'parameter']
    
    def __str__(self):
        return str(self.report.id)+" "+self.parameter