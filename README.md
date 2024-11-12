# NTP Mode 6 Research

This repository contains a Python script that simulates sending an NTP mode 6 query to a remote host. This script is intended for educational purposes only and should be used in a controlled environment with explicit permission from the system owner.

## Disclaimer

**Using this script without proper authorization is illegal and unethical. The author is not responsible for any misuse of this script.**

By using the materials provided in this repository, you agree to the following:

1. You will use the script only in a controlled and legal environment.
2. You will not use the script for any malicious or unauthorized activities.
3. You will not hold the author or contributors responsible for any damage or legal issues arising from the use of this script.

**Use at your own risk.**

## Prerequisites
- Python 3.x

## Vulnerability Description

### NTP Mode 6 Query Vulnerability

**NTP (Network Time Protocol)** is a protocol used to synchronize the clocks of computers over a network. NTP mode 6 is used for control messages, which can be exploited if not properly secured. This mode allows an attacker to send control messages to the NTP server, potentially leading to unauthorized access, configuration changes, or denial of service.

#### Key Points:
- **Mode 6 Control Messages:** Mode 6 is used for control messages such as peer list queries, statistics requests, and other administrative commands.
- **Lack of Authentication:** If the NTP server is not configured to require authentication for mode 6 queries, an attacker can send these queries from any IP address.
- **Potential Impact:** Unauthorized access to mode 6 can lead to:
  - **Configuration Changes:** An attacker can modify the NTP server configuration.
  - **Information Disclosure:** Sensitive information about the NTP server and its peers can be disclosed.
  - **Denial of Service:** The server can be overwhelmed with control messages, leading to a denial of service.

### Example Vulnerable Configuration

A vulnerable NTP server configuration might look like this:

```plaintext
# /etc/ntp.conf

# Allow all hosts to send control messages
restrict default kod nomodify notrap nopeer
```

In this configuration, the `restrict default` directive allows all hosts to send control messages, which can be exploited.

### 1. **Restrict Access to NTP Server:**
   - **Allow Only Trusted Clients:** Configure the NTP server to accept requests only from trusted IP addresses. This can be done using the `restrict` directive in the NTP configuration file (`/etc/ntp.conf` on Linux systems).

   ```plaintext
   restrict default kod nomodify notrap nopeer noquery
   restrict 127.0.0.1
   restrict [::1]
   restrict 192.168.1.0 mask 255.255.255.0 nomodify notrap
   ```

### 2. **Disable Mode 6 Queries:**
   - **Restrict Mode 6:** Explicitly restrict mode 6 queries to prevent unauthorized access.

   ```plaintext
   restrict default kod nomodify notrap nopeer noquery
   restrict 127.0.0.1
   restrict [::1]
   restrict 192.168.1.0 mask 255.255.255.0 nomodify notrap
   restrict ::1 mask ::1 nomodify notrap
   restrict 192.168.1.0 mask 255.255.255.0 kod nomodify notrap nopeer noquery
   ```

### 3. **Use Authentication:**
   - **Enable Authentication:** Configure the NTP server to use authentication to ensure that only authorized clients can send control messages.

   ```plaintext
   keys /etc/ntp.keys
   trustedkey 1
   requestkey 1
   controlkey 1
   ```

   - **Generate Keys:** Use `ntp-keygen` to generate the keys and store them in `/etc/ntp.keys`.

### 4. **Update NTP Software:**
   - **Patch NTP Server:** Ensure that the NTP server software is up to date with the latest security patches.

### 5. **Monitor and Log:**
   - **Logging:** Enable logging to monitor and detect any suspicious activities on the NTP server.

   ```plaintext
   logfile /var/log/ntp.log
   ```

### 6. **Firewall Configuration:**
   - **Firewall Rules:** Use firewall rules to restrict access to the NTP port (UDP 123) from unauthorized sources.

   ```bash
   iptables -A INPUT -p udp --dport 123 -s 192.168.1.0/24 -j ACCEPT
   iptables -A INPUT -p udp --dport 123 -j DROP
   ```

### Example Configuration for `/etc/ntp.conf`:

```plaintext
# /etc/ntp.conf

# Use public servers from the pool.ntp.org project.
server 0.pool.ntp.org iburst
server 1.pool.ntp.org iburst
server 2.pool.ntp.org iburst
server 3.pool.ntp.org iburst

# Restrict default access
restrict default kod nomodify notrap nopeer noquery

# Allow localhost
restrict 127.0.0.1
restrict ::1

# Allow specific subnet
restrict 192.168.1.0 mask 255.255.255.0 nomodify notrap

# Enable authentication
keys /etc/ntp.keys
trustedkey 1
requestkey 1
controlkey 1

# Log file
logfile /var/log/ntp.log
```

By implementing these measures, you can significantly reduce the risk associated with NTP mode 6 queries and enhance the security of your NTP server.
## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Kaneki-hash/NTP-Mode6-Research.git
   cd NTP-Mode6-Research
   ```

2. Ensure you have Python 3 installed:
   ```bash
   python3 --version
   ```

## Usage
1. Modify the `ntp_server` variable in `ntp_mode6_query.py` to the target NTP server IP address.
2. Run the script:
   ```bash
   python3 ntp_mode6_query.py
   ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
