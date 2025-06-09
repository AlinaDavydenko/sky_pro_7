from django.db import models

# Реализовать возможность добавлять, просматривать, редактировать и удалять получателей рассылки (клиентов).


class Recipient(models.Model):
    """ Получатель рассылки """
    email = models.EmailField(unique=True, verbose_name='email')
    full_name = models.CharField(max_length=255, verbose_name='полное имя')
    comment = models.TextField(blank=True, verbose_name='комментарии')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'получатель_рассылки'
        verbose_name_plural = 'получатели_рассылок'
        ordering = ['email']


class Message(models.Model):
    """ сообщение """
    subject = models.CharField(max_length=255, verbose_name='тема письма')
    body = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ['subject']


class Newsletter(models.Model):
    """ рассылки """
    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    ]

    start_time = models.DateTimeField(verbose_name='время старта')
    end_time = models.DateTimeField(verbose_name='время окончания')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created', verbose_name='статус')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение')
    recipients = models.ManyToManyField(Recipient)

    def __str__(self):
        return f"Newsletter {self.id} - {self.status}"


class Attempt(models.Model):
    """ модель попытки рассылки """
    STATUS_CHOICES = [
        ('success', 'Успешно'),
        ('failed', 'Не успешно'),
    ]

    attempt_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    server_response = models.TextField(blank=True)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)

    def __str__(self):
        return f"Attempt {self.id} - {self.status}"
