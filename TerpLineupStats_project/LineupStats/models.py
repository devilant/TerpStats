from django.db import models

import datetime

class Team(models.Model):
    name = models.CharField(max_length=100)
    conference = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Game(models.Model):
    homeTeam = models.ForeignKey(Team, related_name='game_homeTeam')
    awayTeam = models.ForeignKey(Team, related_name='game_awayTeam')
    date = models.DateField()
    isConferenceGame = models.BooleanField()
    neutralCourtGame = models.BooleanField()

    def __unicode__(self):
        return str(self.homeTeam) + ' vs. ' + str(self.awayTeam) + ' ' + str(self.date)

class LineupStats(models.Model):
    lineup = models.CharField(max_length=1000)
    possessionCount = models.IntegerField(default=0)
    made2pCount = models.IntegerField(default=0)
    total2pCount = models.IntegerField(default=0)
    made3pCount = models.IntegerField(default=0)
    total3pCount = models.IntegerField(default=0)
    oppMade2pCount = models.IntegerField(default=0)
    oppTotal2pCount = models.IntegerField(default=0)
    oppMade3pCount = models.IntegerField(default=0)
    oppTotal3pCount = models.IntegerField(default=0)
    turnoverCount = models.IntegerField(default=0)
    defReboundCount = models.IntegerField(default=0)
    totalDefReboundCount = models.IntegerField(default=0)
    offReboundCount = models.IntegerField(default=0)
    totalOffReboundCount = models.IntegerField(default=0)
    pointsFor = models.IntegerField(default=0)
    pointsAgainst = models.IntegerField(default=0)
    stealsCount = models.IntegerField(default=0)
    blockCount = models.IntegerField(default=0)
    foulCount = models.IntegerField(default=0)
    assistCount = models.IntegerField(default=0)
    elapsedTime = models.FloatField(default=0)
    team = models.ForeignKey(Team)
    game = models.ForeignKey(Game)

    def __unicode__(self):
        return self.lineup

    def getPointsPerPossession(self):
        if self.possessionCount > 0:
            return round(self.pointsFor * 1.0 / self.possessionCount, 2)
        return 0

    def getOppPointsPerPossession(self):
        if self.possessionCount > 0:
            return round(self.pointsAgainst * 1.0 / self.possessionCount, 2)
        return 0

    def getEfficiencyMargin(self):
        return self.getPointsPerPossession() - self.getOppPointsPerPossession()

    def get2pPercentage(self):
        if self.total2pCount > 0:
            return round(self.made2pCount * 1.0 / self.total2pCount, 2)
        return 0

    def get3pPercentage(self):
        if self.total3pCount > 0:
            return round(self.made3pCount * 1.0 / self.total3pCount, 2)
        return 0

    def getOpp2pPercentage(self):
        if self.oppTotal2pCount > 0:
            return round(self.oppMade2pCount * 1.0 / self.oppTotal2pCount, 2)
        return 0

    def getOpp3pPercentage(self):
        if self.oppTotal3pCount > 0:
            return round(self.oppMade3pCount * 1.0 / self.oppTotal3pCount, 2)
        return 0

    def getAssistPercentage(self):
        return round(self.assistCount * 1.0 / self.possessionCount)

    def getDefReboundPercentage(self):
        if self.totalDefReboundCount > 0:
            return round(self.defReboundCount * 1.0 / self.totalDefReboundCount, 2)
        return 0

    def getOffReboundPercentage(self):
        if self.totalOffReboundCount > 0:
            return round(self.offReboundCount * 1.0 / self.totalOffReboundCount, 2)
        return 0

    def getTurnoverPercentage(self):
        if self.turnoverCount > 0:
            return round(self.turnoverCount * 1.0 / self.possessionCount, 2)
        return 0
    
    def getElapsedTime(self):
        return datetime.timedelta(seconds = self.elapsedTime)

    def setElapsedTime(self, elapsed):
        self.elapsedTime = elapsed.total_seconds()

    def __add__(self, other):
        self.possessionCount += other.possessionCount
        self.made2pCount += other.made2pCount
        self.total2pCount += other.total2pCount
        self.made3pCount += other.made3pCount
        self.total3pCount += other.total3pCount
        self.turnoverCount += other.turnoverCount
        self.elapsedTime += other.elapsedTime
        self.defReboundCount += other.defReboundCount
        self.totalDefReboundCount += other.totalDefReboundCount
        self.totalOffReboundCount += other.totalOffReboundCount
        self.offReboundCount += other.offReboundCount
        self.pointsAgainst += other.pointsAgainst
        self.pointsFor += other.pointsFor
        self.stealsCount += other.stealsCount
        self.blockCount += other.blockCount
        self.foulCount += other.foulCount
        self.assistCount += other.assistCount
        self.oppMade2pCount += other.oppMade2pCount
        self.oppTotal2pCount += other.oppTotal2pCount
        self.oppMade3pCount += other.oppMade3pCount
        self.oppTotal3pCount += other.oppTotal3pCount
        return self
