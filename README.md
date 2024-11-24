# Reverse Shell Tool
A Python-based Reverse Shell Tool designed to enable remote communication and command execution on a target machine. This tool demonstrates the core principles of socket programming and data serialization using the socket and json libraries. It provides basic functionality for remote file management and shell interaction.

Features
Remote Command Execution: Send commands to the target machine and receive output.
File Management:
Upload files to the target machine.
Download files from the target machine.
Change Directory: Navigate through directories on the target machine remotely.
Persistent Connection: Automatically reconnect if the connection is lost.
Cross-Platform Support: Works on Windows, macOS, and Linux (Python required).
Requirements
Python 3.x
Libraries: socket, json, os
How It Works
The Server (Controller):

Listens for incoming connections from the target.
Sends commands to the target machine.
Handles file uploads and downloads.
The Client (Target):

Connects to the server.
Executes received commands.
Handles file operations as requested.
