import psutil
import time

def monitor_cpu(threshold=80, interval=1):
    print("Monitoring CPU usage... (Press Ctrl+C to stop)")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=interval)
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
            else:
                print(f"CPU usage is normal: {cpu_usage}%")
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the monitor
if __name__ == "__main__":
    monitor_cpu(threshold=80, interval=1)