from django.db import models

class Feedback(models.Model):
    problem=models.ForeignKey(
        'problems.Problem',
        on_delete=models.CASCADE
    )

    user=models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE
    )

    feedback_details=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback - {self.problem.title}"
