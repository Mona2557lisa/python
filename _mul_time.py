_mul_time.py
#📄 Description:
#Multiplies time by a number to calculate duration or pace (e.g., in a race).
print("name : Monalisa.N \n usn : 1AY24AI73\n section : O ")
class Time:
    def _init_(self, hours=0, minutes=0, seconds=0):
        self.seconds = hours * 3600 + minutes * 60 + seconds

    def _str_(self):
        h = self.seconds // 3600
        m = (self.seconds % 3600) // 60
        s = self.seconds % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

def mul_time(time, multiplier):
    return Time(seconds=int(time.seconds * multiplier))

def pace(time, distance):
    return mul_time(time, 1 / distance)

# Example usage
t = Time(1, 30, 0)  # 1 hour 30 min
print("Original time:", t)
print("Doubled time:", mul_time(t, 2))
print("Pace per mile:", pace(t, 10))
