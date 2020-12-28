from pythonping import ping

Target = '8.8.8.8'
string = ""

ping(Target, verbose=True, count=1, out=string)
