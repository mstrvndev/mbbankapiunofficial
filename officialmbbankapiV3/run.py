import subprocess
import os

class MBbankWrapper:
    def __init__(self, node_script_path="index.js"):
        # Full path to Node.js script (you can change it to "mbbank/dist/index.js" if you want to call that directly)
        self.node_script_path = os.path.abspath(node_script_path)

    def run_node_script(self):
        # Use shell=True so Windows can understand this command
        cmd = f'node "{self.node_script_path}"'
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.stdout:
                return result.stdout.strip()
            elif result.stderr:
                return "Error:\n" + result.stderr.strip()
            else:
                return "No output received from Node.js script."
        except Exception as e:
            return f"Exception occurred: {e}"

# ---- Run the script ----
if __name__ == "__main__":
    wrapper = MBbankWrapper()
    output = wrapper.run_node_script()
    print(output)
