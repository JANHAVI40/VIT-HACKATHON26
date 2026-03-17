from collections import defaultdict
import time

ip_data = defaultdict(lambda: {
    "ports": set(),
    "packet_count": 0,
    "risk": 0,
    "stage": "Normal",
    "last_seen": time.time()
})

PORT_SCAN_THRESHOLD = 10

def analyze_packet(packet):

    src = packet["src_ip"]
    port = packet["dst_port"]

    data = ip_data[src]

    data["packet_count"] += 1
    data["ports"].add(port)

    if len(data["ports"]) > PORT_SCAN_THRESHOLD:
        data["stage"] = "Reconnaissance"
        data["risk"] = 60

    return {
        "src_ip": packet["dst_ip"],   # 🔥 swapped here
        "dst_ip": packet["src_ip"],   # 🔥 swapped here
        "protocol": packet["protocol"],
        "dst_port": packet["dst_port"],
        "stage": data["stage"],
        "risk": data["risk"]
    }