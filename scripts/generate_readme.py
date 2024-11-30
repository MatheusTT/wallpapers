#!/usr/bin/env python3
from os import listdir, path
import yaml


this_path: str = path.dirname(path.realpath(__file__))
root_path: str = path.dirname(this_path)
authors_path: str = path.join(root_path, "authors")


def yaml_to_dict(file_path: str):
  with open(file_path, "r", encoding="utf8") as yaml_file:
    return_dict = yaml.safe_load(yaml_file)
    return return_dict


def yaml_to_md(file: str) -> str:
  author_name: str = path.basename(path.dirname(file)).split("/")[-1]
  readme: str = f"<details>\n<summary>{author_name}</summary>\n\n"
  data = yaml_to_dict(file)
  for i in data["links"]:
    readme += f"- [{i}]({data["links"][i]})\n"
  readme += "\n  <details>\n  <summary>Wallpapers</summary>\n"
  for i in data["wallpapers"]:
    readme += f"""
  <a href=\"{i["link"]}\">
    <img src=\"./authors/{author_name}/{i["path"]}\" title=\"{i["name"]}\" width=600/>
  </a>"""

  readme += "\n\n  </details>\n</details>\n"
  return readme


def read_md(md_file: str) -> str:
  with open(md_file, "r", encoding="utf-8") as f:
    return f.read()


def write_md(md_file: str, content: str) -> None:
  with open(md_file, "w", encoding="utf-8") as f:
    _ = f.write(content)


readme_contents: str = read_md("base_readme.md")
authors: list[str] = sorted(listdir(path=authors_path), key=str.lower)

for author in authors:
  info_file: str = path.join(authors_path, author, "info.yaml")
  if path.exists(info_file):
    readme_contents += yaml_to_md(info_file)
    if author != authors[-1]:
      readme_contents += "\n\n"

write_md(path.join(root_path, "README.md"), readme_contents)
