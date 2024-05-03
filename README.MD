# Cookie Stealing Server

This Python-based server is designed to intercept and log cookies sent via HTTP GET requests. It operates by masquerading as a benign server, extracting cookies from incoming requests, and storing them for later examination. The server is particularly useful for educational demonstrations of handling and displaying the potential risks associated with cross-site scripting (XSS) attacks.

## Overview

The `CookieStealingServer` extends `http.server.SimpleHTTPRequestHandler` to customize request handling, suppress typical HTTP server logs, and specifically target cookie data embedded within requests. Upon receiving a request containing a cookie, the server logs this data to both the console and a log file, indicating successful interception.

## Features

- **Silent Operation:** Does not log standard server requests to avoid clutter and remain unobtrusive.
- **Cookie Logging:** Captures and logs cookie data from query parameters.
- **Immediate Feedback:** Prints cookie capture information to the console.
- **Simple Confirmation Page:** Responds to all requests with a confirmation HTML page stating "Cookie stealing successful."

## Setup and Execution

### Prerequisites

- Python 3.x installed on your system

### Running the Server

1. Download the script to your local machine.
2. Run the server script with Python by executing:

   ```bash
   python cookie_stealing_server.py
