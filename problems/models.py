from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Problem(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
        ('resolved', 'Resolved'),
    ]

    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    photo = models.ImageField(
        upload_to='problems/',
        blank=True,
        null=True
    )

    location = models.CharField(max_length=255)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    department_remark = models.TextField(blank=True)

    user_remark = models.TextField(blank=True)

    department_approval = models.BooleanField(default=False)

    user_approval = models.BooleanField(default=False)

    resolved_at = models.DateTimeField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class ProblemAssignment(models.Model):

    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE
    )

    department = models.ForeignKey(
        'accounts.Department',
        on_delete=models.CASCADE
    )

    assigned_at = models.DateTimeField(auto_now_add=True)

    assignment_status = models.CharField(
        max_length=20,
        default='assigned'
    )

    assigned_by = models.ForeignKey(
    'accounts.User',
    on_delete=models.CASCADE
)

    def __str__(self):
        return f"{self.problem.title} - {self.department.name}"