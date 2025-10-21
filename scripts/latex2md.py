#!/usr/bin/env python3
import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path

## will be useful for converting LaTex blogs to md later.

def convert_latex_to_md(latex_file):
    """Convert LaTeX file to Markdown with YAML frontmatter."""
    output_file = Path('content/posts') / (Path(latex_file).stem + '.md')
    
    # Extract title from LaTeX file (assuming it's in \title{} command)
    with open(latex_file, 'r') as f:
        content = f.read()
        title_start = content.find('\\title{') + 7
        title_end = content.find('}', title_start)
        title = content[title_start:title_end] if title_start > 6 else "Untitled"
    
    # Create YAML frontmatter
    frontmatter = f"""---
title: "{title}"
date: {datetime.now().strftime('%Y-%m-%d')}
draft: false
math: true
---

"""
    
    # Convert LaTeX to Markdown using pandoc
    try:
        result = subprocess.run([
            'pandoc',
            '--from=latex',
            '--to=markdown',
            '--wrap=none',
            '--standalone',
            latex_file
        ], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Error converting {latex_file}: {result.stderr}")
            return
        
        # Write the converted content with frontmatter
        with open(output_file, 'w') as f:
            f.write(frontmatter)
            f.write(result.stdout)
            
        print(f"Successfully converted {latex_file} to {output_file}")
        
    except Exception as e:
        print(f"Error processing {latex_file}: {str(e)}")

def main():
    # Create posts directory if it doesn't exist
    os.makedirs('content/posts', exist_ok=True)
    
    # Process all .tex files in the latex directory
    latex_dir = Path('content/latex')
    for tex_file in latex_dir.glob('*.tex'):
        convert_latex_to_md(str(tex_file))

if __name__ == '__main__':
    main()