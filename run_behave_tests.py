import os
import re
import subprocess
import sys
from multiprocessing import Process

from uvicorn import run


def start_fastapi_server(app_path: str, port: int) -> None:
    """
    Starts a FastAPI server using the given app_path and port.

    Args:
        app_path (str): The import path to the FastAPI application.
        port (int): The port number to run the server on.
    """
    run(app_path, host="localhost", port=port, log_level="warning")


def run_behave_tests() -> int:
    """
    Runs the Behave tests and returns the exit code, the behave result will give
    something like this:
    ```
    2 scenarios passed, 0 failed, 0 skipped
    9 steps passed, 1 failed, 1 skipped, 0 undefined
    Took 0m7.045s
    ```

    Returns:
        int: 0 if all tests passed, 1 if there were failures
    """
    result = subprocess.run(["behave"], capture_output=True, check=True)
    output = result.stdout.decode().strip()
    num_failures = 0
    num_failures = num_failures + int(re.findall(r"(\d+) failed", output)[0])
    return (
        {"code": 1, "content": output}
        if num_failures > 0
        else {"code": 0, "content": output}
    )


def kill_existing_processes_on_port(port: int) -> None:
    """
    Kills any existing processes running on the given port.

    Args:
        port (int): The port number to check for running processes.
    """
    try:
        if os.name == "nt":  # Windows
            find_process_cmd = f"netstat -ano | findstr :{port}"
            process_output = (
                subprocess.check_output(find_process_cmd, shell=True)
                .decode("utf-8")
                .strip()
                .split("\n")
            )
            pids = [line.split()[-1] for line in process_output if line]
            for pid in pids:
                if int(pid) > 0:
                    subprocess.run(
                        f"taskkill /F /PID {pid}",
                        shell=True,
                        stderr=subprocess.DEVNULL,
                        check=True,
                    )
        else:  # Linux and macOS
            find_process_cmd = f"lsof -i :{port} -t"
            process_ids = (
                subprocess.check_output(find_process_cmd, shell=True)
                .decode("utf-8")
                .strip()
                .split("\n")
            )
            for pid in process_ids:
                if pid:
                    subprocess.run(f"kill -9 {pid}", shell=True, check=True)
    except subprocess.CalledProcessError:
        pass


def main() -> None:
    """
    Main function to run the FastAPI server and Behave tests.
    """
    port = 4848
    app_path = "src.gpt_examples_generator.app:app"
    kill_existing_processes_on_port(port)

    fastapi_process = Process(target=start_fastapi_server, args=(app_path, port))
    fastapi_process.start()

    try:
        behave_exit_code = run_behave_tests()["code"]
        behave_response = run_behave_tests()["content"]
        print(behave_response)
        print(f"Behave exit code: {behave_exit_code}")
    finally:
        fastapi_process.terminate()
        fastapi_process.join()

    if behave_exit_code != 0:
        sys.exit()
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
