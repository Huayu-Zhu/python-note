import os

def open_app():
	app_name = input('please input your app name: ')
	str(app_name)
	app_dir = r'/Applications/' + app_name + r'.app/Contents/MacOS/' + app_name
	os.system("open %s"  %(app_dir) )

if __name__ == '__main__':
	'''
	app_name = input('please input your app name: ')
	str(app_name)
#	app_dir = r'/Applications/BaiduNetdisk_mac.app/Contents/MacOS/BaiduNetdisk_mac'
	app_dir = r'/Applications/' + app_name + r'.app/Contents/MacOS/' + app_name

	print(app_dir)

	os.system("open %s"  %(app_dir) )
	#os.system("")

	#app_name = input("Please input your App Name: ")
	#open_app(app_name)
	'''
	open_app()