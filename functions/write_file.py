import os

def write_file(working_directory, file_path, content):
    candidate_abs = os.path.abspath(os.path.join(working_directory, file_path))
    working_abs = os.path.abspath(working_directory)
    inside = candidate_abs == working_abs or candidate_abs.startswith(working_abs + os.sep)

    if not inside:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        os.makedirs(os.path.dirname(candidate_abs), exist_ok=True)
        with open(candidate_abs, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"








