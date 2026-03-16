### AI‑Powered SOC Monitoring System

##### ⚡ Testing Instructions (SOC System) : Important: Before testing, ensure your machine is on an isolated network. Packet sniffing may be blocked by Windows Security/Defender. You can either temporarily
disable Defender/firewall or allow exceptions for Python, Npcap, and Docker. Do not use this on public networks.
Local Setup & Contributor Implementation Guide

### Project: AI‑Powered Security Operations Center (SOC)

- Purpose: Real‑time network attack detection using packet sniffing and machine learning.

- Implemented Feature: Network traffic monitoring and port‑scan (reconnaissance) detection.(by Contributor-Gauri Arun Khedekar.)

  #### 1. System Requirements

- Before starting the setup, ensure the following requirements are met.

- Operating System

`Windows 10 / Windows 11`

- Software Requirements

`Python 3.10 or 3.11`

`Docker Desktop`

`Nmap`

`Visual Studio Code`

`Administrator privileges'

`Internet connection`

- Python Libraries

- Required libraries include:

`scapy`
`pandas`
`numpy`
`scikit-learn`
`joblib`
`pyqt6`
`pyqtgraph`
`plyer`
`google-generativeai`

#### 2. Installing Python

- Download Python from:

'https://www.python.org/downloads/`

- During installation enable:

- ✔ Add Python to PATH

- Verify installation:

`python --version`

- Example output:

`Python 3.11.5`

#### 3. Install Npcap (Required for Packet Sniffing)

- Packet sniffing with Scapy requires the Npcap driver.

- Download:

`https://npcap.com/#download`

- Important installation options:

- ✔ Install Npcap
- ✔ Enable WinPcap API-compatible mode

- Npcap allows the system to capture live network packets.

#### 4. Install Docker Desktop

- Download Docker:

`https://www.docker.com/products/docker-desktop/`

- Verify installation:

`docker --version`

- Docker is used to run the vulnerable application OWASP Juice Shop.

#### 5. Install Nmap

- Download Nmap:

`https://nmap.org/download.html`

- Verify installation:

`nmap --version`

- Nmap is used to simulate network attacks such as port scanning.

#### 6. Project Folder Structure

- Create a main project folder.

- Example:

`VIT-HACKATHON2026`

Project structure:
```
VIT-HACKATHON2026
│
├── backend
│   ├── train_brain.py
│   ├── detection_engine.py
│   ├── packet_sniffer.py
│
├── frontend
│   ├── main_app.py
│
├── dataset
│   └── cic_ids_2017_data.csv
│
├── models
│
└── requirements.txt
```

#### 7. Create Python Virtual Environment

- Navigate to the project folder.

- Create virtual environment:

`python -m venv soc-env`

Activate environment:

`soc-env\Scripts\activate`

Terminal should display:

`(soc-env)`

#### 8. Install Required Python Libraries

Install dependencies using:

`pip install -r requirements.txt`

If installing manually:

`pip install scapy pandas numpy scikit-learn joblib pyqt6 pyqtgraph plyer google-generativeai`

Verify installation:

`pip list`

#### 9. Download IDS Dataset

Dataset used:

`CIC IDS 2017`

Download from:

`https://www.unb.ca/cic/datasets/ids-2017.html`

Download:

`MachineLearningCSV.zip`

- Extract the file.

- Copy one CSV file into:

`dataset/` (in file explorer VIT-HACKATHON2026's dataset folder)

Rename it:

`cic_ids_2017_data.csv`

#### 10. Train the Machine Learning Model

- Navigate to backend folder.

'cd backend'

- Run training script:

'python train_brain.py'

- Expected output:

- Model trained successfully

- Model will be saved in:

- models/brain.joblib

- The model uses Isolation Forest to detect anomalous network behavior.

#### 11. Running the Vulnerable Target Application

- To simulate cyber attacks we run OWASP Juice Shop.

- Start the container:

`docker run -d -p 3000:3000 bkimminich/juice-shop`

- Verify container:

`docker ps`

- Expected output:

`0.0.0.0:3000->3000/tcp`

- Open browser:

`http://localhost:3000`(instead of localhost use IPv4 of you laptop/PC which you will get by following next steps:-
`Win + R -> cmd -> ipconfig -> IPv4`

- This confirms the vulnerable application is running.

#### 12. Verify Port 3000 is Open

- Check port status:

`netstat -ano | findstr :3000`

- Expected output:

`TCP    0.0.0.0:3000     LISTENING`

- This means the web application is listening on port 3000.

#### 13. Identify Network IP Address

- correctly capture network traffic and perform attacks, you need to know your machine’s active network interfaces and IP addresses.

- Run in Command Prompt:

`ipconfig`

- From your output, key interfaces and addresses are:

- Interface	IPv4 Address	Notes:-
```
Wi-Fi	-> 172.16.6.208 -> This is your main machine IP on the Wi-Fi network. Use this for scanning from another machine using nmap|
vEthernet (WSL) ->	172.28.96.1	-> This is the virtual interface for WSL/Docker. Use this if testing attacks on local containers.|
Loopback ->	127.0.0.1	-> Standard localhost. Use this for attacks originating from the same machine.|
```
- Important Guidelines:

- Local attacks / Docker containers: Use 127.0.0.1 and/or 172.28.96.1 as the target IP.

- Network attacks from another machine: Use your Wi-Fi IPv4 (172.16.6.208) as the target.

- Default gateway: Check Default Gateway in Wi-Fi adapter (172.16.69.78) if needed for routing tests.

- Always verify which interface your packet sniffer listens to. For your setup:

- Use `Intel(R) Wi-Fi 6 AX201 160MHz` (Wi-Fi adapter) for real network traffic.

- Use `\Device\NPF_Loopback` for localhost / Docker traffic.

- ⚠️ This ensures your SOC system captures the correct packets and identifies attacker IPs accurately.

#### 14. Identify Packet Sniffing Interface

- Run Python script:

```
from scapy.all import get_working_ifaces
print(get_working_ifaces())
```

- Example output:

'Intel(R) Wi-Fi 6 AX201 160MHz`

- This interface corresponds to the machine IP.

#### 15. Configure Packet Sniffer

- File:

`backend/packet_sniffer.py`

- Important configuration:

```
sniffer = AsyncSniffer(
    iface="Intel(R) Wi-Fi 6 AX201 160MHz",
    prn=process_packet,
    store=False
)
```

- This allows capturing packets on the active network interface.

#### 16. Start the SOC Dashboard

- Run frontend application:

`cd frontend`
`python main_app.py`

- Expected terminal output:

`SOC Packet Sniffer Started...`

- Dashboard will open and begin monitoring network traffic.

17. Generate Test Network Traffic

- To verify packet capture:

`ping google.com`

or

`ping 127.0.0.1`

- Packets should appear in the dashboard.

##### 18. Simulate Port Scan Attack

- Run Nmap scan.

- Example command:

`nmap -Pn -T4 -F 10.102.75.137`

- Explanation:

Flag	Meaning
-Pn	Skip host discovery
-T4	Faster scanning
-F	Scan top 100 ports

- This generates reconnaissance traffic.

#### 19. Detection Result

- The SOC system captures packets such as:

```
e.g.
src_ip : 10.102.75.150
dst_ip : 10.102.75.137
protocol : TCP
dst_port : 3000
stage : Reconnaissance
```

- Meaning:

- Field	Description
- src_ip	Attacker machine
- dst_ip	Target machine
- dst_port	Scanned service
- stage	Attack stage detected
  
#### 20. Firewall Behavior

- Sometimes Nmap results show:

- 100 filtered tcp ports

 Reason:

`Windows firewall blocks responses`

- Ports silently drop packets

- Even if ports are filtered, packet sniffing still detects scanning activity.

#### 21. Final Working Architecture

System workflow:

```
Attacker Machine
        │
        ▼
Nmap Scan
        │
        ▼
Network Packets
        │
        ▼
Scapy Packet Sniffer
        │
        ▼
Detection Engine
        │
        ▼
Machine Learning Model
        │
        ▼
SOC Dashboard
        │
        ▼
Attack Alert
```

#### 22. Contributor Work (Gauri Khedekar)

- The following tasks were implemented as part of the project contribution.

- Environment Setup

- Installed Python environment

- Installed Npcap driver

- Configured Scapy packet capture

- Dataset Integration

- Downloaded CIC IDS 2017 dataset

- Prepared dataset for ML training

- Machine Learning Implementation

- Implemented Isolation Forest model

- Trained detection model using network traffic dataset

- Packet Sniffing System

- Implemented Scapy packet capture

- Configured correct network interface

- Parsed packet fields such as:

```
source IP
destination IP
protocol
destination port
Attack Simulation
```

- Configured OWASP Juice Shop

- Generated attacks using Nmap

- Detection Pipeline

- Captured live packets

- Sent packet features to detection engine

- Detected reconnaissance (port scanning) attacks

- SOC Dashboard Integration

- Integrated sniffer output with dashboard alerts

- Displayed attack events in real time

#### 23. Current Working Features

- The system currently detects:

```
✔ Network traffic
✔ Port scanning (Reconnaissance)
✔ Attacker IP identification
✔ Target port detection
✔ Real‑time packet monitoring
```

#### 24. Future Improvements

- Possible enhancements include:

- Brute force detection

- SQL injection detection

- Automated firewall blocking

- AI‑based threat analysis

- Attack kill‑chain correlation
