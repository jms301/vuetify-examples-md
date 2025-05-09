#!/usr/bin/env python3
"""
Script to convert Vue files in a directory to a single Markdown file.
Specifically designed for the v-timeline examples.
"""

import os
import sys
from pathlib import Path

def read_vue_file(file_path):
    """Read the content of a Vue file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def sort_vue_files(vue_files, component_name):
    """
    Sort Vue files with 'usage.vue' first and 'misc-advanced.vue' last.
    All other files will remain in their original order.
    """
    # Define the specific sorting order
    first_file = f"{component_name}/usage.vue"
    last_file = f"{component_name}/misc-advanced.vue"
    
    # Remove the first and last files if they exist in the list
    result = vue_files.copy()
    if first_file in result:
        result.remove(first_file)
    if last_file in result:
        result.remove(last_file)
    
    # Add them at the beginning and end
    if os.path.exists(first_file):
        result.insert(0, first_file)
    if os.path.exists(last_file):
        result.append(last_file)
    
    return result

def generate_heading(file_path):
    """Generate a heading by combining component name and file name"""
    parts = file_path.split('/')
    component_name = parts[-2]  # The directory name (e.g., 'v-timeline')
    file_name = parts[-1].replace('.vue', '')  # The file name without extension
    file_name = file_name.replace('-', ' ') # replace dashes with spaces
  
    item = "concept"

    if component_name.startswith('v-'):
        item = "component"

    # Create a formatted heading
    heading = f"# Vuetify {item} {component_name} - {file_name}"
    return heading

def convert_vue_to_md(component_dir):
    """
    Convert all Vue files in the specified directory to a single Markdown file.
    Places 'usage.vue' first and 'misc-advanced.vue' last.
    """
    # Check if directory exists
    if not os.path.isdir(component_dir):
        print(f"Error: Directory '{component_dir}' does not exist.")
        return None
    
    # Get the component name (the last part of the path)
    component_name = os.path.basename(component_dir)
    
    # Get all Vue files in the directory
    vue_files = []
    for root, _, files in os.walk(component_dir):
        for file in files:
            if file.endswith('.vue'):
                vue_files.append(os.path.join(root, file))
    
    if not vue_files:
        print(f"No .vue files found in {component_dir}")
        return None
    
    # Sort files with 'usage.vue' first and 'misc-advanced.vue' last
    sorted_files = sort_vue_files(vue_files, component_dir)
    
    # Generate the markdown content
    md_content = []
    
    for file_path in sorted_files:
        # Add heading
        heading = generate_heading(file_path)
        md_content.append(heading)
        md_content.append("")  # Empty line after heading
        md_content.append("Example code")
        md_content.append("")  # Empty line after heading
        # Add code block
        vue_content = read_vue_file(file_path)
        md_content.append("```vue")
        md_content.append(vue_content)
        md_content.append("```")
        md_content.append("")  # Empty line after code block
    
    return "\n".join(md_content)

def main():
    if len(sys.argv) != 2:
        print("Usage: python vue_to_md.py <directory_path>")
        sys.exit(1)
    
    component_dir = sys.argv[1]
    md_content = convert_vue_to_md(component_dir)
    
    if md_content:
        # Generate output filename based on component name
        component_name = os.path.basename(component_dir)
        output_file = f"{component_name}.md"
        
        # Write to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"Successfully converted Vue files to {output_file}")

if __name__ == "__main__":
    main()
