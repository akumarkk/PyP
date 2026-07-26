from jupyter_client import BlockingKernelClient

def run_code_on_kernel(connection_file_path, code_string):
    # Point to one of the valid JSON files found in your runtime directory
    client = BlockingKernelClient()
    client.load_connection_file(connection_file_path)
    client.start_channels()

    print("Successfully connected to active Jupyter kernel via ZMQ!")

    # Execute a quick test
    #code_to_run = 'print("Hello from ZMQ direct connection!")'
    client.execute(code_string)

    # Read output
    while True:
        try:
            io_msg = client.get_iopub_msg(timeout=1.0)
            if io_msg["msg_type"] == "stream":
                print(f"[Output]: {io_msg['content']['text'].strip()}")
                break
        except TimeoutError:
            break

    client.stop_channels()

connection_file = r"C:\Users\your-user-name\AppData\Roaming\jupyter\runtime\kernel-4117a7c1-150a-4bb3-8ce8-52671b4e96fe.json"
code_to_run = """
print("Hello from ZMQ direct connection!")
a = 10 + 800
print(f"10 + 800 = {a}")
"""
run_code_on_kernel(connection_file, code_to_run)