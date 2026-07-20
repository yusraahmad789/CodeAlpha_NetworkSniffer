from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

packet_count = 0

def process_packet(packet):
    global packet_count
    packet_count += 1

    print(f"\n{'='*60}")
    print(f"Packet #{packet_count} | Time: {datetime.now().strftime('%H:%M:%S')}")

    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto_num = ip_layer.proto

        if TCP in packet:
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            print(f"Protocol: TCP")
            print(f"Source IP:Port      -> {src_ip}:{sport}")
            print(f"Destination IP:Port -> {dst_ip}:{dport}")

        elif UDP in packet:
            sport = packet[UDP].sport
            dport = packet[UDP].dport
            print(f"Protocol: UDP")
            print(f"Source IP:Port      -> {src_ip}:{sport}")
            print(f"Destination IP:Port -> {dst_ip}:{dport}")

        elif ICMP in packet:
            print(f"Protocol: ICMP")
            print(f"Source IP      -> {src_ip}")
            print(f"Destination IP -> {dst_ip}")

        else:
            print(f"Protocol: Other (proto #{proto_num})")
            print(f"Source IP      -> {src_ip}")
            print(f"Destination IP -> {dst_ip}")

        if Raw in packet:
            payload = packet[Raw].load
            print(f"Payload (first 50 bytes): {payload[:50]}")
    else:
        print("Non-IP packet captured (e.g., ARP)")
        print(packet.summary())

def main():
    print("Starting network sniffer... Press Ctrl+C to stop.\n")
    try:
        sniff(prn=process_packet, count=0, store=False)
    except KeyboardInterrupt:
        print(f"\n\nSniffer stopped. Total packets captured: {packet_count}")
    except PermissionError:
        print("Permission denied. Run this script with admin/root privileges.")

if __name__ == "__main__":
    main()
