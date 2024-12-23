from scapy.all import ICMP, IP, sr1

def send_icmp_request(destination_ip):
    """
    Sends an ICMP Echo Request (ping) to the specified destination IP.

    :param destination_ip: Target IP address to ping.
    """
    try:
        print(f"Sending ICMP request to {destination_ip}...")
        # Create an IP packet with ICMP
        icmp_packet = IP(dst=destination_ip) / ICMP()
        
        # Send the packet and wait for the response
        response = sr1(icmp_packet, timeout=2, verbose=False)
        
        if response:
            print(f"Received response from {destination_ip}:")
            print(response.summary())
        else:
            print(f"No response from {destination_ip}. Host may be down.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target_ip = input("Enter the destination IP to ping: ")
    send_icmp_request(target_ip)
