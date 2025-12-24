# UDP Flood DDoS Tool

> ⚠️ **EDUCATIONAL PURPOSE ONLY** - Unauthorized use is illegal and unethical

A Python-based UDP flood tool designed for **educational purposes** and **authorized penetration testing** only. This tool demonstrates how DDoS attacks work using UDP packet flooding.

## ⚠️ Legal Disclaimer

**READ THIS BEFORE USING:**

- This tool is for **EDUCATIONAL and AUTHORIZED TESTING ONLY**
- Using this tool against systems without explicit written permission is **ILLEGAL**
- Unauthorized DDoS attacks can result in **criminal charges and imprisonment**
- The author assumes **NO responsibility** for misuse of this tool
- By using this tool, you agree to use it only in legal contexts

See [DISCLAIMER.md](DISCLAIMER.md) for full legal information.

## 📋 Description

This tool sends UDP packets to a specified IP address and port, demonstrating a basic UDP flood attack technique. It includes:

- UDP packet flooding capability
- Random payload generation (1490 bytes)
- Progress bar display during initialization
- Real-time packet tracking
- Automatic port cycling

**Legitimate Use Cases:**
- Network stress testing on your own infrastructure
- Security research in controlled lab environments
- Penetration testing with proper authorization
- Educational demonstrations in cybersecurity courses

## 🔧 Features

- **Simple Interface** - Easy-to-use command-line tool
- **UDP Flooding** - Sends continuous UDP packets to target
- **Port Cycling** - Automatically cycles through ports 1-65534
- **Visual Feedback** - ASCII art banner and progress indicators
- **Packet Counter** - Tracks number of packets sent

## 🛠️ Requirements

- Python 3.x
- Linux/Unix operating system (recommended)
- Required packages listed in `requirements.txt`

## 📦 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/hannan0x0/DDos-Tool.git
cd DDos-Tool
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Make script executable (Linux/Mac):**
```bash
chmod +x DDos.py
```

## 🚀 Usage

```bash
python DDos.py
```

**Interactive Prompts:**
1. Enter target IP address (e.g., `192.168.1.100`)
2. Enter target port (e.g., `80`)
3. Tool begins sending UDP packets

**Example:**
```bash
$ python DDos.py

Enter Your Target IP: 192.168.1.100

Enter Port: 8080

Attacking

sent 1 packet to 192.168.1.100 sent port:8081
sent 2 packet to 192.168.1.100 sent port:8082
sent 3 packet to 192.168.1.100 sent port:8083
...
```

**Stop the attack:** Press `Ctrl+C`

## 🎯 Technical Details

- **Protocol:** UDP (User Datagram Protocol)
- **Packet Size:** 1490 bytes of random data
- **Port Range:** 1-65534 (cycles continuously)
- **Socket Type:** SOCK_DGRAM (UDP)

## ⚙️ How It Works

1. Creates a UDP socket connection
2. Generates random byte payload (1490 bytes)
3. Displays attack initialization progress
4. Continuously sends UDP packets to target IP:Port
5. Increments port number after each packet
6. Resets port to 1 when reaching 65534

## 🛡️ Defense Against This Attack

If you're testing your network's resilience:
- Implement rate limiting
- Use firewall rules to block excessive UDP traffic
- Deploy DDoS mitigation services
- Configure intrusion detection systems (IDS)
- Use cloud-based DDoS protection

## 📚 Educational Resources

Learn more about network security:
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [Penetration Testing Frameworks](https://www.kali.org/)
- [Ethical Hacking Courses](https://www.offensive-security.com/)

## 🤝 Contributing

Contributions for educational improvements are welcome:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m "Add educational feature"`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**MD. Abdul Hannan Mir**

- GitHub: [@hannan0x0](https://github.com/hannan0x0)
- Page: Cyberdemy Bangladesh
- Email: hannanmir.me@gmail.com

## 🙏 Acknowledgments

- Created for educational purposes in cybersecurity
- Part of Cyberdemy Bangladesh educational initiatives
- Inspired by network security research

## ⚠️ Final Warning

**This tool can cause serious network disruption. Only use it:**
- On your own systems
- In isolated lab environments
- With explicit written authorization
- For legitimate security testing

**Unauthorized use is a crime. You have been warned.**

---

*For additional legal information, please read [DISCLAIMER.md](DISCLAIMER.md)*