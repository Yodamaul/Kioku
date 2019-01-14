import urllib.request

def send_name(name):
	data = {'name':name}
	data = bytes(urllib.parse.urlencode(data).encode())
	handler = urllib.request.urlopen('http://192.168.88.232:3000/url', data)
	print( handler.read().decode( 'utf-8' ) )