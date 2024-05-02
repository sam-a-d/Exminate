from django.db import models

# Create your models here.
class Institute(models.Model):
    """Model definition for Institute."""

    # TODO: Define fields here
    inst_name = models.CharField(max_length=100)
    inst_short_name = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Institution."""

        verbose_name = 'Institute'
        verbose_name_plural = 'Institute'

    def __str__(self):
        """Unicode representation of Institute."""
        return self.inst_name

# the following models don't have dependencies
class Department(models.Model):
    """Model definition for Department."""

    # TODO: Define fields here
    dept_name = models.CharField(max_length=100)
    dept_code = models.CharField( max_length=10)


    class Meta:
        """Meta definition for Department."""

        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        """Unicode representation of Department."""
        return self.dept_name

# the following models don't have dependencies
class Semester(models.Model):
    """Model definition for Semester."""

    # TODO: Define fields here
    sem_name = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Semester."""

        verbose_name = 'Semester'
        verbose_name_plural = 'Semesters'

    def __str__(self):
        """Unicode representation of Semester."""
        return self.sem_name

class Field(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    field = models.ForeignKey(Field, on_delete = models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Designation(models.Model):
    """Model definition for Designation."""

    # TODO: Define fields here
    desig_name = models.CharField(max_length=50)
    desig_short = models.CharField(max_length=10)

    class Meta:
        """Meta definition for Designation."""

        verbose_name = 'Designation'
        verbose_name_plural = 'Designations'

    def __str__(self):
        """Unicode representation of Designation."""
        return self.desig_short

class Teacher(models.Model):
    """Model definition for Teacher."""
    
    name = models.CharField(max_length=50, null=True, blank=True)
    desig = models.ForeignKey(Designation , on_delete=models.CASCADE, null=True)
    institution = models.ForeignKey(Institute, on_delete=models.CASCADE, null= True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, null = True)

    contact = models.CharField(max_length=20)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)

    class Meta:
        """Meta definition for Teacher."""

        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        """Unicode representation of Teacher."""
        return self.teacher_name