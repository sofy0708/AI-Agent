import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    candidate_abs = os.path.abspath(os.path.join(working_directory, file_path))
    working_abs = os.path.abspath(working_directory)
    inside = candidate_abs == working_abs or candidate_abs.startswith(working_abs + os.sep)

    if not inside:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(candidate_abs):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:

        commands = ['python', candidate_abs] + args

        result = subprocess.run(
            commands, 
            capture_output=True, 
            cwd=working_abs, 
            timeout=30, 
            text=True)
        
        output =[]
        
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if output == []:
            return "No output produced."
        return "\n".join(output)
    
    except Exception as e:
        return f"Error: executing Python file: {e}"

