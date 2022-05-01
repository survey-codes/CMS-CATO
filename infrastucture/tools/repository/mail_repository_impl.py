from infrastucture.tools.models import Mail


class MailRepositoryImpl:
    def isEmpty(self):
        return Mail.objects.count() == 0
