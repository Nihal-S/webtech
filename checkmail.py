# from validate_email import validate_email
# email = raw_input("email")
# # email = str(email)
# is_valid = validate_email(email)
# print(is_valid)
# is_valid = validate_email('nihalsreenivasu@gmail.com',check_mx=True)
# print(is_valid)
# is_valid = validate_email('nihalsreenivasu@gmail.com',verify=True)
# print(is_valid)

# from validate_email import validate_email
# is_valid = validate_email('nihalsreenivasu@gmail.com',verify=True)
# print(is_valid)

# import socket
# import smtplib

# # Get local server hostname
# host = socket.gethostname()

# # SMTP lib setup (use debug level for full output)
# server = smtplib.SMTP()
# server.set_debuglevel(0)

# # SMTP Conversation
# server.connect(mxRecord)
# server.helo(host)
# server.mail('nihalsreenivasu@gmail.com')
# code, message = server.rcpt(str("nihalsreenivasu@gmail.com"))
# server.quit()

# # Assume 250 as Success
# if code == 250:
# 	print('Success')
# else:
# 	print('Bad')
import re

def check(email):  
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$' 
    if(re.search(regex,email)):  
        return True
    else:  
        return False

print(check("nihalsreenivasu@gmailcom"))