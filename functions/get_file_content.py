import os
from config import char_limit

def get_file_content(working_directory, file_path):
    candidate_abs = os.path.abspath(os.path.join(working_directory, file_path))
    working_abs = os.path.abspath(working_directory)
    inside = candidate_abs == working_abs or candidate_abs.startswith(working_abs + os.sep)

    if not inside:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    try:
        if not os.path.isfile(candidate_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(candidate_abs, 'r') as file:
            content = file.read(char_limit + 1)
            if len(content) > char_limit:
                return content[:char_limit] + f'[...File "{file_path}" truncated at 10000 characters]'
        
            return content
    except Exception as e:
        return f"Error: {e}"