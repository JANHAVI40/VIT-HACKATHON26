from scapy.all import AsyncSniffer
from scapy.layers.inet import IP, TCP, UDP
from detection_engine import analyze_packet

callbacks = []

def register_callback(func):
    callbacks.append(func)

def process_packet(packet):

    if not packet.haslayer(IP):
        return

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst

    protocol = "OTHER"
    port = 0

    if packet.haslayer(TCP):
        protocol = "TCP"
        port = packet[TCP].dport

    elif packet.haslayer(UDP):
        protocol = "UDP"
        port = packet[UDP].dport

    packet_info = {
        "src_ip": src_ip,
        "dst_ip": dst_ip,
        "protocol": protocol,
        "dst_port": port
    }

    # Run detection
    attack = analyze_packet(packet_info)

    packet_info.update(attack)

    print(packet_info)

    if packet_info.get("stage") != "Normal":
        for cb in callbacks:
            cb(packet_info)

def start_sniffer():

    sniffer = AsyncSniffer(
        iface="Intel(R) Wi-Fi 6 AX201 160MHz",
        prn=process_packet,
        store=False
    )

    print("SOC Packet Sniffer Started...")
    sniffer.start()

    return sniffer