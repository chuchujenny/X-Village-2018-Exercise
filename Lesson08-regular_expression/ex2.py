import re
class AuthSystem:
    
    def __init__(self):
        self.username_regex = re.compile(r'(?P<department>[a-zA-Z][a-z][a-z])')
        self.password_regex = re.compile(r'(?P<room_id>[a-z][a-z][a-z][0][0-9][0-9][0-9][0-9][0-9])')
    def check_name(self, username):
    	if self.username_regex.search(username) is not None:
    		return True
    	elif (chr(ord(username[0]))>122 or chr(ord(username[0]))<97) or (chr(ord(username[0]))>90 or chr(ord(username[0]))<65):
    		print("Username format error! Your username is ",username)
		for i in range(1:len(username)):
			if chr(ord(username[i]))>122 or chr(ord(username[i]))<97:
				print("Username format error! Your username is ",username)
		elif len(username) != 3:
			print("Username legnth error! Your password length is ",len(username))
	def _check_password(self, password):
        if self.password_regex.search(password) is not None:
            return True
        for i in range(0,2):
        	if chr(ord(password[i]))>122 or chr(ord(password[i]))<97:
        		print("Password format error! Your password is ",password)
        for i in range(3,len(password)):
            if i <0 or i >9:
            	print("Password format error! Your password is ",password)
        elif len(password) != 9:
			print("Password legnth error! Your password length is ",len(password))
	def authenticate(self, username, password):
        if not self._check_username(username):
            return
        
        if not self._check_password(password):
            return
        print("Welcome, {}!".format(username))

idcheck=AuthSystem()
idcheck.authenticate("Tom", "tom059357")
          


