import datetime
from datetime import datetime
import re
s = "Get detailed information about breast cancer risks, causes, symptoms, treatments, research, and more.Nov 19, 2021"
#print (datetime.now().strftime("%b %-d, %Y"))
match =re.findall(
    r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{2},\s\d{4}', s)

print(match[0])
print(len(match))

s = "new date.Nov 17, 2016"
match = re.findall(
    r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{2},\s\d{4}', s)

print(match[0])
print(len(match))
