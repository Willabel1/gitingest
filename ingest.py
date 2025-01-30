import os
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

def create_repo_context_file(repo_path, output_file, ignore_list, include_structure):
    """
    (Original create_repo_context_file function from the Python script)
    Generates a file containing the structure and (optionally) content of a repository.
    """
    with open(output_file, "w") as outfile:
        outfile.write("Repository Structure and Content:\n\n")

        for root, dirs, files in os.walk(repo_path):
            # Remove ignored directories from traversal
            dirs[:] = [d for d in dirs if d not in ignore_list]

            relative_path = os.path.relpath(root, repo_path)

            if relative_path != ".":
              outfile.write(f"\nDirectory: {relative_path}/\n")
            else:
              outfile.write(f"\nDirectory: ./\n") # To indicate the root dir

            for file in files:
                if file not in ignore_list:
                    file_path = os.path.join(root, file)
                    relative_file_path = os.path.join(relative_path, file)

                    outfile.write(f"\n  File: {relative_file_path}\n")
                    if not include_structure: # Include content only if include_structure is False
                        try:
                            with open(file_path, "r") as infile:
                                outfile.write("    Content:\n")
                                outfile.write("    ```\n")
                                for line in infile:
                                    outfile.write("    " + line)
                                outfile.write("    ```\n")
                        except UnicodeDecodeError:
                            outfile.write("    ```\n")
                            outfile.write("    Binary or non-text file. Content omitted.\n")
                            outfile.write("    ```\n")
                        except Exception as e:
                            outfile.write("    ```\n")
                            outfile.write(f"    Error reading file: {e}\n")
                            outfile.write("    ```\n")

def browse_repo():
    repo_path = filedialog.askdirectory()
    repo_path_entry.delete(0, tk.END)
    repo_path_entry.insert(0, repo_path)

def browse_output():
    output_file = filedialog.asksaveasfilename(defaultextension=".txt")
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(0, output_file)

def generate_context():
    repo_path = repo_path_entry.get()
    output_file = output_file_entry.get()
    ignore_list = [item.strip() for item in ignore_list_entry.get("1.0", tk.END).split(',')]
    structure_only = structure_only_var.get()

    if not repo_path or not output_file:
        messagebox.showerror("Error", "Please specify both repository path and output file.")
        return

    try:
        create_repo_context_file(repo_path, output_file, ignore_list, structure_only)
        messagebox.showinfo("Success", f"Repository context written to {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create main window
window = tk.Tk()
window.title("Repository Context Generator")

# Repository Path
repo_path_label = tk.Label(window, text="Repository Path:")
repo_path_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
repo_path_entry = tk.Entry(window, width=50)
repo_path_entry.grid(row=0, column=1, padx=5, pady=5)
repo_path_button = tk.Button(window, text="Browse", command=browse_repo)
repo_path_button.grid(row=0, column=2, padx=5, pady=5)

# Output File
output_file_label = tk.Label(window, text="Output File:")
output_file_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
output_file_entry = tk.Entry(window, width=50)
output_file_entry.grid(row=1, column=1, padx=5, pady=5)
output_file_button = tk.Button(window, text="Browse", command=browse_output)
output_file_button.grid(row=1, column=2, padx=5, pady=5)

# Ignore List
ignore_list_label = tk.Label(window, text="Ignore List (comma-separated):")
ignore_list_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
ignore_list_entry = tk.Text(window, width=50, height=4)
ignore_list_entry.grid(row=2, column=1, padx=5, pady=5)
ignore_list_entry.insert(tk.END, ".git, __pycache__, .DS_Store")  # Default values

# Structure Only Checkbox
structure_only_var = tk.BooleanVar()
structure_only_check = tk.Checkbutton(window, text="Structure Only", variable=structure_only_var)
structure_only_check.grid(row=3, column=1, padx=5, pady=5, sticky="w")

# Generate Button
generate_button = tk.Button(window, text="Generate Context", command=generate_context)
generate_button.grid(row=4, column=1, padx=5, pady=10)

window.mainloop()