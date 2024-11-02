#searching for email address

import re
email_log = """"Email recieved June 2 from user1@gmail.com. 
Email recieved June 2 from user2@gmail.com. 
Email rejected June 2nd from invalid_email@gmail.com"""

print(re.findall("\w+@\w+\.\w+",email_log))
