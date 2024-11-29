#!/usr/bin/env python3
from os import listdir, path

this_path: str = path.dirname(path.realpath(__file__))
root_path: str = path.dirname(this_path)
authors_path: str = path.join(root_path, "authors")


def read_md(md_file: str) -> str:
  with open(md_file, "r", encoding="utf-8") as f:
    return f.read()


def write_md(md_file: str, content: str) -> None:
  with open(md_file, "w", encoding="utf-8") as f:
    _ = f.write(content)


readme_contents: str = read_md("base_readme.md")
authors: list[str] = sorted(listdir(path=authors_path), key=str.lower)

for author in authors:
  md_file: str = path.join(authors_path, author, f"{author}.md")
  if path.exists(md_file):
    readme_contents += read_md(md_file)
    if author != authors[-1]:
      readme_contents += "\n\n"

write_md(path.join(root_path, "README.md"), readme_contents)
