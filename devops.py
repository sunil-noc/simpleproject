##########################
###this is simple script
import subprocess

def get_uptime_output():
    """
    Executes the 'uptime' command and returns its raw output as a string.
    This works primarily on Linux/macOS.
    """
    try:
        # 'uptime -p' provides a "pretty" format on Linux (e.g., "up 6 minutes")
        # For general compatibility, just 'uptime' works
        result = subprocess.run(['uptime'], capture_output=True, text=True, check=True, shell=False)
        return result.stdout.strip()
    except FileNotFoundError:
        return "Error: 'uptime' command not found (Windows might need a different method)"
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.stderr}"

if __name__ == "__main__":
    uptime_info = get_uptime_output()
    print(f"System Uptime Info: {uptime_info}")
