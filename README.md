Repository Context Generator

Overview
The `ingest.py` script allows users to generate a structured representation of a repository, including its directory structure and optionally its file contents. .
Reccomend just doing your SRC when you select a file, otherwise it'll be crazy long! Works best with Claude Sonnet 3.5 in my opionion.

Features
- Browse and select a repository directory.
- Specify an output file to save the repository context.
- Optionally Define an ignore list to exclude certain files or directories.
- Option to include only the structure or both structure and file contents.
- Graphical interface built with Tkinter.

Requirements
- Python 3.x
- Tkinter (comes pre-installed with most Python distributions)

Installation
No installation is required. Simply run the script using Python:
```sh
python ingest.py
```

Usage
1. Launch the script.
2. Select a repository directory.
3. Choose an output file where the generated context will be saved.
4. (Optional) Specify files or directories to ignore (comma-separated).
5. (Optional) Check the "Structure Only" box if you only want the directory structure.
6. Click "Generate Context" to create the repository context file.

Output Format
The generated file will include:
- Directory paths
- File names
- (Optional) File contents (excluding binary files)
- Errors or non-text file notices where applicable

Example Output
```
Repository Structure and Content:

Directory: ./

  File: README.md
    Content:
    ```
    # Project Title
    A brief description of the project.
    ```

Directory: src/

  File: main.py
    Content:
    ```
    print("Hello, World!")
    ```
```

Known Issues
- Binary files are omitted with a notice.
- Large repositories may take time to process. Don't do the entire repo.

License
This project is open-source and distributed under the MIT License.

