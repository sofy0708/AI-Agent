import os

def get_files_info(working_directory, directory="."):
    candidate_abs = os.path.abspath(os.path.join(working_directory, directory))
    working_abs = os.path.abspath(working_directory)
    inside = candidate_abs == working_abs or candidate_abs.startswith(working_abs + os.sep)
    
    if not inside:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(candidate_abs):
        return f'Error: "{directory}" is not a directory'
    dir_contents = os.listdir(candidate_abs)
    try:
        result = []
        for file_name in dir_contents:
            result.append(f'- {file_name}: file_size={os.path.getsize(os.path.join(candidate_abs, file_name))} bytes, is_dir={os.path.isdir(os.path.join(candidate_abs, file_name))}')
        return "\n".join(result)
    except Exception as e:
        return f"Error: {e}"