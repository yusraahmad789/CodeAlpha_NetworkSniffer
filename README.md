#NetworkSniffer

📌 Task 1 - Basic Network Sniffer
Cyber Security Internship Project | CodeAlpha

📖 Description
This project is a basic network sniffer built in Python using the **Scapy** library. It captures live network traffic on the system and displays key details about each packet, including:

- Source and Destination IP addresses
- Protocol type (TCP, UDP, ICMP, or other)
- Source and Destination ports (for TCP/UDP)
- A preview of the packet's payload data

The goal of this project is to understand how data flows through a network and how packets are structured at a basic level.

🛠 Tools & Libraries Used
- Python 3
- Scapy
- Npcap (required on Windows for packet capture)

## ⚙ How It Works
1. The script uses Scapy's `sniff()` function to capture live packets on the network interface.
2. Each captured packet is analyzed to identify its protocol (TCP, UDP, ICMP, etc.).
3. Relevant details (IPs, ports, payload) are extracted and printed to the console in real time.
4. The sniffer runs continuously until manually stopped.

 ▶ How to Run
1. Install Python 3 and the required library:
   ```
   pip install scapy
   ```
2. On Windows, install **Npcap** from https://npcap.com (required for packet capture).
3. Run the script with administrator/root privileges:
   - **Windows:** Run Command Prompt as Administrator, then:
     ```
     python network_sniffer.py
     ```
   - **Linux/Mac:**
     ```
     sudo python3 network_sniffer.py
     ```
4. Generate some network traffic (browse a website, run `ping google.com`, etc.) to see packets being captured.
5. Press `Ctrl+C` to stop the sniffer and view the total packet count.

📸 Sample Output
See `sample_output.png` for an example of the sniffer capturing live UDP traffic, showing source/destination IPs, ports, and payload data.

⚠ Disclaimer
This tool is built strictly for educational purposes as part of the CodeAlpha Cyber Security Internship. It should only be used on networks you own or have explicit permission to monitor.

👤 Author
Internship Task submission for CodeAlpha - Cyber Security Domain
