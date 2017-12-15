from RandomApproachText import RandomApproachText
from functions import cross_in_tray
from Settings import Settings

r = RandomApproachText(cross_in_tray, Settings, 100)
r.get()
print(r.formreport())