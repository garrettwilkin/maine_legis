from django.db import models

SHORT = 30
MEDIUM = 100
LONG = 255

class Bill(models.Model):
    state = models.CharField(max_length=2)
    session = models.CharField(max_length=SHORT)
    bill_id = models.CharField(max_length=SHORT)
    action_dates = models.TextField()
    chamber = models.CharField(max_length=5)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    # TODO: length guess.
    sunlight_id = models.CharField(max_length=SHORT)
    scraped_subjects = models.CharField(max_length=SHORT)
    subjects = models.CharField(max_length=SHORT)
    type = models.CharField(max_length=SHORT)


class Version(models.Model):
    bill = models.ForeignKey(Bill)
    url = models.URLField()
    name = models.CharField(max_length=SHORT)
    mimetype = models.CharField(max_length=SHORT)
    doc_id = models.CharField(max_length=SHORT)


class Document(models.Model):
    bill = models.ForeignKey(Bill)
    url = models.URLField()
    name = models.CharField(max_length=SHORT)
    mimetype = models.CharField(max_length=SHORT)
    doc_id = models.CharField(max_length=SHORT)


class Action(models.Model):
    bill = models.ForeignKey(Bill)
    date = models.DateTimeField()
    action = models.CharField(max_length=SHORT)
    actor = models.CharField(max_length=SHORT)
    type = models.CharField(max_length=SHORT)


class Title(models.Model):
    bill = models.ForeignKey(Bill)
    title = models.CharField(max_length=SHORT)

class AlternateTitle(Title):
    pass

class Vote(models.Model):
    bill = models.ForeignKey(Bill)
    motion = models.CharField(max_length=SHORT)
    chamber = models.CharField(max_length=SHORT)
    date = models.DateTimeField()
    sunlight_id = models.CharField(max_length=SHORT)
    state = models.CharField(max_length=2)
    session = models.CharField(max_length=SHORT)
    yes_count = models.PositiveSmallIntegerField()
    no_count = models.PositiveSmallIntegerField()
    other_count = models.PositiveSmallIntegerField()


class Voter(models.Model):
    vote = models.ForeignKey(Vote)
    name = models.CharField(max_length=SHORT)
    leg_id = models.CharField(max_length=SHORT)
    # yes, no, other
    response = models.CharField(max_length=5)


class Source(models.Model):
    bill = models.ForeignKey(Bill)
    vote = models.ForeignKey(Vote)
    url = models.URLField()


class Sponsor(models.Model):
    bill = models.ForeignKey(Bill)
    name = models.CharField(max_length=SHORT)
    leg_id = models.CharField(max_length=SHORT)
    type = models.CharField(max_length=9)
