import subprocess

def test_speed():
    speedtest_output = subprocess.run(["speedtest-cli"], capture_output=True, text=True).stdout
    return speedtest_output

if __name__ == "__main__":
    print("Start Test - check your internet connection")
    input("Press ENTER...")
    print("Testing")
    output = test_speed()
    print("--- Speedtest Results ---")
    print(output)
    
