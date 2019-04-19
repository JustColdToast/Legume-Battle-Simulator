# Written by Kanwarpal, JustColdToast
# This is the basic class for a creature object. All other classes build into this object
# The basic creature object relies on a provided name and starting stats
# HealthPoints, Speed, Attack, and Defense indexes are starting class properties
# exp represents the number of experience points collected, this defines the creature level


class creature:
    def __init__(self, name="Null", hpdex=1, spddex=1, atkdex=1, defdex=1, exp=1):
        self.name = name
        self.baseHealth = hpdex
        self.baseSeedModi = spddex
        self.baseAttackModi = atkdex
        self.baseDefenseModi = defdex
        self.currentLevel = exp


# Below are outlined type-specific moves along with attack values and accuracy values (measured from 0-1)
# (format) MoveName:(Base Damage, Base Speed)
fireTypeMoves = {"fireBall": (5, 1),
                 "flash": (10, .75),
                 "inferno": (25, .5)}
waterTypeMoves = {"splash": (5, 1),
                 "jetStream": (10, .75),
                 "tidalWave": (25, .5)}
earthTypeMoves = {"smash": (5, 1),
                 "boulder": (10, .75),
                 "earthquake": (25, .5)}
# For now all types of three moves of a similar attack and accuracy, this will be expanded in further balancing

# ----------------------
# Below are outlined the various creature types
# Classically, Fire beats Earth, which beats Water, which beats Fire

# Each type does 25% more damage to it's counterpart, and takes 25% less damage.
# they are, however, 50% more vulnerable to attacks from the stronger type

# Effectively, this means that type matching provides significant potential, whereas mismatches will result in severe
# reduction of overall damage output

# All attack-type objects are children of the creature object; as well, types are based on specific creature stats
class fireType(creature):
    def __init__(self, name="Null", hpdex=1, spddex=1, atkdex=1, defdex=1, exp=0):
        # Below line calls in constructor of the creature object, passing the initial values needed
        creature.__init__(self, name, hpdex, spddex, atkdex, defdex, exp)
        # Below are the modifers of type-based battle stats
        self.waterDefModi = 0.5
        self.attackWaterModi = .75
        self.EarthDefModi = 1.25
        self.attackEarthModi = 1.25
        self.moveSet = fireTypeMoves

class waterType(creature):
    def __init__(self, name="Null", hpdex=1, spddex=1, atkdex=1, defdex=1, exp=0):
        # Below line calls in constructor of the creature object, passing the initial values needed
        creature.__init__(self, name, hpdex, spddex, atkdex, defdex, exp)
        # Below are the modifers of type-based battle stats
        self.EarthDefModi = 0.5
        self.attackEarthModi = .75
        self.fireDefModi = 1.25
        self.attackFireModi = 1.25
        self.moveSet = waterTypeMoves

class earthType(creature):
    def __init__(self, name="Null", hpdex=1, spddex=1, atkdex=1, defdex=1, exp=0):
        # Below line calls in constructor of the creature object, passing the initial values needed
        creature.__init__(self, name, hpdex, spddex, atkdex, defdex, exp)
        # Below are the modifers of type-based battle stats
        self.fireDefModi = 0.5
        self.attackFireModi = .75
        self.waterDefModi = 1.25
        self.attackWaterModi = 1.25
        self.moveSet = earthTypeMoves

