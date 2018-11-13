from django.db import models

# Create your models here.
class User(models.Model):
    student_id = models.CharField(max_length = 8, unique = True, null = False)
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254,unique=True)
    phone_no = models.CharField(max_length = 10, unique = True, null = False)
    registration_date_time = models.DateTimeField(auto_now = True)


    GUITAR = 'G'
    PIANO = 'P'
    BASE = 'B'
    DRUM = 'D'
    VOCAL = 'V'
    INSTRUMENT_CHOICE = (
        (GUITAR, 'Guitar'),
        (PIANO, 'Piano'),
        (BASE, 'Base'),
        (DRUM, 'Drum'),
        (VOCAL, 'Vocal')
    )
    Instrument_1 = models.CharField(
        max_length=1,
        choices=INSTRUMENT_CHOICE,
        null = True,
        blank = True,
    )
    Instrument_2 = models.CharField(
        max_length=1,
        choices=INSTRUMENT_CHOICE,
        null = True,
        blank = True,
    )
    PERFORMANCE = 'PE'
    EVENT = 'EV'
    FINANCE = 'FI'
    SECRETARY = 'SE'
    PROPAGANDA = 'PR'
    PUBLICITY = 'PU'
    EDUCATION = 'ED'

    COMMITEE_CHOICE = (
        (EDUCATION, 'Education'),
        (EVENT, 'Event'),
        (FINANCE, 'Finanace'),
        (PERFORMANCE, 'Performance'),
        (PROPAGANDA, 'Propaganda'),
        (PUBLICITY, 'Publicity'),
        (SECRETARY, 'Secretary'),
    )

    Committee_member = models.CharField(
        max_length = 2,
        choices = COMMITEE_CHOICE,
        null = True,
        blank = True,
    )
