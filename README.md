# 🧠 Joke Server: Matrix Edition™

Ever wondered what it’s like to be stuck in 1999 *inside* a Docker container that serves dad jokes? No? Too bad.

This is a **tiny, intentionally ugly, gloriously useless** web server in a Docker container. It serves:

- 🧍 A **random static joke** from a file.
- 🌐 A **random joke from the internet** (to test outbound connectivity!).
- 🌍 Your **public IP address** (again, because why not).

All wrapped in a **Matrix-style animated background** to feel like you’re hacking into your own humor API.

---

## 🧪 Technical Use Case

Despite its appearance, this hot mess serves an actual purpose:

- ✅ Test Docker image building & networking
- ✅ Validate port forwarding works (via browser)
- ✅ Check outbound internet access from inside the container
- ✅ Verify dynamic content rendering via JavaScript (no Python blocking!)
- ✅ Pretend you know front-end development

---

## 🧰 Stack

- `python:3.11-slim`
- `http.server` (built-in Python web server)
- `JavaScript` for dynamic jokes + IP fetching
- No frameworks. No libraries. No remorse.

---

## 🚀 How to Use

```bash
git clone https://github.com/your-fake-org/joke-server.git
cd joke-server
docker build -t joke-server .
docker run -d -p 8080:8080 joke-server
