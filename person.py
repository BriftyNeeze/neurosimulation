import math
import random
import datapoints


class Person:
    population = 0

    def __init__(self, age=-1):
        self.has_parkinson = False
        self.parkinson_chance = 0.002 + (random.random()-0.5)/1000
        self.dopamine_capacity = 0.24
        self.social_media_use = random.random()/2
        if age == -1:
            self.age = random.randint(10, 60)
        else:
            self.age = age
        self.random_factor = random.random()
        self.dead = False
        Person.population += 1
        # Social Media to dopamine and parkinson
        dopamine_diff = self.social_media_use * datapoints.social_media_to_dopamine
        parkinson_diff = (self.social_media_use-0.5) * datapoints.social_media_to_dopamine * datapoints.dopamine_to_parkinson
        self.dopamine_capacity += dopamine_diff
        self.parkinson_chance += parkinson_diff

    def year(self):
        if self.dead:
            return
        self.age += 1
        self.media_use_change(random.random()/self.age/2-(1/self.age/4))
        if self.age <= 20:
            pass
        elif self.age <= 40:
            if random.random() < self.parkinson_chance / 800 * (self.age*self.age/1000+1) and not self.has_parkinson:
                self.has_parkinson = True
        elif self.age <= 55:
            if random.random() < self.parkinson_chance / 370 * (self.age*self.age/1000+1) and not self.has_parkinson:
                self.has_parkinson = True
        else:
            if random.random() < self.parkinson_chance / 230 * (self.age*self.age/85+1) and not self.has_parkinson:
                self.has_parkinson = True

        if self.age >= 90:
            if random.random() < datapoints.chance_to_die[-1]/100 or self.age > 110:
                self.dead = True
                Person.population -= 1
        else:
            if random.random() < datapoints.chance_to_die[self.age] / 100:
                self.dead = True
                Person.population -= 1

    def media_use_change(self, change):
        self.social_media_use += change
        self.social_media_use = max(self.social_media_use, 0)
        self.social_media_use = min(self.social_media_use, 1)
        dopamine_diff = change * datapoints.social_media_to_dopamine
        if random.randint(0, 1) == 0:
            dopamine_diff /= (self.random_factor/2+1)
        else:
            dopamine_diff *= (self.random_factor / 2 + 1)
        self.dopamine_change(dopamine_diff)

    def dopamine_change(self, change):
        self.dopamine_capacity += change
        parkinson_diff = change * datapoints.dopamine_to_parkinson
        if random.randint(0, 1) == 0:
            parkinson_diff /= (self.random_factor / 2 + 1)
        else:
            parkinson_diff *= (self.random_factor / 2 + 1)
        self.parkinson_chance += parkinson_diff

