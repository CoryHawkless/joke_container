import http.server
import socketserver
import random

PORT = 8080

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why do Java developers wear glasses? Because they don't C#.",
    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
    "To understand what recursion is, you must first understand recursion.",
    "I told my computer I needed a break, and now it won’t stop sending me KitKat ads.",
    "There are 10 kinds of people in the world: those who understand binary and those who don't.",
    "My code doesn't always work, but when it does, I don’t know why.",
    "Why was the developer unhappy at their job? They wanted arrays!",
    "I asked the computer for help. It said: '404 Advice Not Found.'",
    "Debugging: Removing the needles from the haystack.",
    "Computers make very fast, very accurate mistakes.",
    "Why did the function cross the road? To get to the other side effect.",
    "I would tell you a UDP joke, but you might not get it.",
    "Why do Python developers wear glasses? Because they can't C.",
    "What did the router say to the doctor? It hurts when IP.",
    "A user interface is like a joke. If you have to explain it, it’s not that good.",
    "I changed my password to 'incorrect'. So whenever I forget, it says 'Your password is incorrect.'",
    "Why did the developer go broke? Because he used up all his cache.",
    "There’s no place like 127.0.0.1.",
    "I'm not lazy. I'm on energy-saving mode.",
    "Knock knock. Who's there? Race condition. Race condition who?",
    "How many programmers does it take to change a light bulb? None. It's a hardware problem.",
    "Real programmers count from 0.",
    "Why did the DevOps engineer quit? He didn't get arrays.",
    "In case of fire: git commit, git push, leave building.",
    "Why was the cell phone wearing glasses? It lost its contacts.",
    "Why do programmers hate nature? It has too many bugs.",
    "There are two hard things in computer science: cache invalidation, naming things, and off-by-one errors.",
    "An infinite loop walks into a bar. An infinite loop walks into a bar.",
    "Why did the CSS developer break up with the HTML developer? They had too many style differences.",
    "The best thing about a Boolean is even if you are wrong, you are only off by a bit.",
    "I would tell you a joke about Java, but it's too class-based.",
    "Why do programmers always mix up Halloween and Christmas? Because Oct 31 == Dec 25.",
    "What do you call 8 hobbits? A hobbyte.",
    "Why did the computer get cold? It left its Windows open.",
    "What’s a computer’s least favorite food? Spam.",
    "Why was the computer tired when it got home? It had too many tabs open.",
    "Artificial intelligence is no match for natural stupidity.",
    "Never trust a computer you can’t throw out a window.",
    "Computers are like air conditioners. They stop working properly if you open Windows.",
    "To err is human – and to blame it on a computer is even more so.",
    "Why did the web developer drown? He forgot to close his div.",
    "Your mom is so classless, she could be a JavaScript function.",
    "I told a joke about a pointer the other day. It went nowhere.",
    "My code works… I have no idea why.",
    "Why is Git like a relationship? You commit, then push.",
    "Don’t anthropomorphize computers. They hate that.",
    "Keyboard not found… Press any key to continue.",
    "404: Joke Not Found.",
    "Welcome to the Internet: Where men are men, women are men, and children are FBI agents.",
]

class JokeHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("index.html", "r") as file:
                html = file.read()
            joke = random.choice(JOKES)
            html = html.replace("{{joke}}", joke)
            self.wfile.write(html.encode("utf-8"))
        else:
            self.send_error(404, "File not found")

with socketserver.TCPServer(("", PORT), JokeHandler) as httpd:
    print(f"Serving at http://0.0.0.0:{PORT}")
    httpd.serve_forever()
