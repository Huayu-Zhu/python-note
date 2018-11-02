# With open_app.py you can open applications on 
# your MacOS.

import os

def open_app():
	app_name = input('please input your app name: ')
	str(app_name)
	app_dir = r'/Applications/' + app_name + r'.app/Contents/MacOS/' + app_name
	os.system("open %s"  %(app_dir) )

if __name__ == '__main__':

	open_app()