# The basic race tracks from Step 3
class Track(object):
    spaces = 36

    def __init__(self, *args, **kwargs):
        if "name" in kwargs:
            self.name = kwargs["name"]

    def __str__(self):
        return "{} has {} spaces".format(self.name, self.spaces)


class RaceTrack(Track):
    max_rounds = 6
