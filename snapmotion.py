#SnapMotion by Technoboy10
import SimpleHTTPServer
import Leap, sys
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
class CORSHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def send_head(self):
        frame = controller.frame()
        path = self.path
        print path
        ospath = os.path.abspath('')
        if path == '/handcount': 
            f = open(ospath + '/return', 'w+')
            f.write(str(len(frame.hands)))
            f.close()
            f = open(ospath + '/return', 'rb')
            ctype = self.guess_type(ospath + '/return')
            self.send_response(200)
            self.send_header("Content-type", ctype)
            fs = os.fstat(f.fileno())
            self.send_header("Content-Length", str(fs[6]))
            self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            return f
        elif path == '/fingercount': 
            f = open(ospath + '/return', 'w+')
            f.write(str(len(frame.fingers)))
            f.close()
            f = open(ospath + '/return', 'rb')
            ctype = self.guess_type(ospath + '/return')
            self.send_response(200)
            self.send_header("Content-type", ctype)
            fs = os.fstat(f.fileno())
            self.send_header("Content-Length", str(fs[6]))
            self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            return f
        elif path == '/toolcount': 
            f = open(ospath + '/return', 'w+')
            f.write(str(len(frame.tools)))
            f.close()
            f = open(ospath + '/return', 'rb')
            ctype = self.guess_type(ospath + '/return')
            self.send_response(200)
            self.send_header("Content-type", ctype)
            fs = os.fstat(f.fileno())
            self.send_header("Content-Length", str(fs[6]))
            self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            return f
        elif 'handpos' in path: 
            regex = re.compile('/handpos([xyz])([1|2])')
            m = regex.match(path)
            hand = int(m.group(2)) - 1
            f = open(ospath + '/return', 'w+')
            if m.group(1) == 'x':
                f.write(str(frame.hands[hand].palm_position.x))
            if m.group(1) == 'y':
                f.write(str(frame.hands[hand].palm_position.y))
            if m.group(1) == 'z':
                f.write(str(frame.hands[hand].palm_position.z))
            f.close()
            f = open(ospath + '/return', 'rb')
            ctype = self.guess_type(ospath + '/return')
            self.send_response(200)
            self.send_header("Content-type", ctype)
            fs = os.fstat(f.fileno())
            self.send_header("Content-Length", str(fs[6]))
            self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            return f
        elif 'fingerpos' in path: 
            regex = re.compile('/fingerpos([xyz])([0-9]+)')
            m = regex.match(path)
            finger = int(m.group(2)) - 1
            f = open(ospath + '/return', 'w+')
            if m.group(1) == 'x':
                f.write(str(frame.fingers[finger].tip_position.x))
            if m.group(1) == 'y':
                f.write(str(frame.fingers[finger].tip_position.y))
            if m.group(1) == 'z':
                f.write(str(frame.fingers[finger].tip_position.z))
            f.close()
            f = open(ospath + '/return', 'rb')
            ctype = self.guess_type(ospath + '/return')
            self.send_response(200)
            self.send_header("Content-type", ctype)
            fs = os.fstat(f.fileno())
            self.send_header("Content-Length", str(fs[6]))
            self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            return f
        elif 'toolpos' in path: 
            regex = re.compile('/toolpos([xyz])([0-9]+)')
            m = regex.match(path)
            tool = int(m.group(2)) - 1
            f = open(ospath + '/return', 'w+')
            if m.group(1) == 'x':
                f.write(str(frame.tools[tool].tip_position.x))
            if m.group(1) == 'y':
                f.write(str(frame.tools[tool].tip_position.y))
            if m.group(1) == 'z':
                f.write(str(frame.tools[tool].tip_position.z))
            f.close()
            f = open(ospath + '/return', 'rb')
            ctype = self.guess_type(ospath + '/return')
            self.send_response(200)
            self.send_header("Content-type", ctype)
            fs = os.fstat(f.fileno())
            self.send_header("Content-Length", str(fs[6]))
            self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            return f
        elif 'handypr' in path: 
            regex = re.compile('/handypr([ypr])([1|2])')
            m = regex.match(path)
            hand = int(m.group(2)) - 1
            f = open(ospath + '/return', 'w+')
            if m.group(1) == 'y':
                f.write(str(frame.hands[hand].palm_position.yaw))
            if m.group(1) == 'p':
                f.write(str(frame.hands[hand].palm_position.pitch))
            if m.group(1) == 'r':
                f.write(str(frame.hands[hand].palm_position.roll))
            f.close()
            f = open(ospath + '/return', 'rb')
            ctype = self.guess_type(ospath + '/return')
            self.send_response(200)
            self.send_header("Content-type", ctype)
            fs = os.fstat(f.fileno())
            self.send_header("Content-Length", str(fs[6]))
            self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            return f
        
if __name__ == "__main__":
    import os
    import re
    import SocketServer
    PORT = 3434 #L+E+A+P twice
    Handler = CORSHTTPRequestHandler
    controller = Leap.Controller()
    print "Connected to Leap Motion controller"
    #Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "serving at port", PORT
    print "Go ahead and launch Snap!."
    httpd.serve_forever()

