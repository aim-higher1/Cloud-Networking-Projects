from scapy.all import ARP, Ether, sendp

def send_arp_request(target_ip, target_mac):
    """
    Sends a crafted ARP request to the specified target.

    :param target_ip: IP address of the target.
    :param target_mac: MAC address of the target.
    """
    try:
        print(f"Sending ARP request to IP: {target_ip}, MAC: {target_mac}")
        
        # Create an Ethernet frame and an ARP packet
        arp_packet = Ether(dst=target_mac) / ARP(pdst=target_ip)
        
        # Send the packet
        sendp(arp_packet, verbose=False)
        print("ARP request sent successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    target_mac = input("Enter the target MAC address: ")
    send_arp_request(target_ip, target_mac)
