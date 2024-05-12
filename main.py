import os
import re
import json
import subprocess


def install_dependencies():
    try:
        subprocess.run("npm install", shell=True, check=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as error:
        print("Error occurred while installing dependencies:", error)


def main():
    project_name = input(
        "Enter project name to rename this project, press enter if you do not want to rename \n"
    )
    project_name = re.sub(r"[^\w\s-]", "", project_name).replace(" ", "-")
    if not project_name:
        return
    install_dependencies()

    file_names = ["package.json", "package-lock.json"]

    try:

        for file_name in file_names:
            if os.path.exists(file_name):
                with open(file_name, "r") as file:
                    data = json.load(file)
                data["name"] = project_name
                if file_name == "package-lock.json":
                    for pkg_info in data.get("packages", {}).values():
                        pkg_info["name"] = project_name

                with open(file_name, "w") as file:
                    json.dump(data, file, indent=2)
                print(f"Renamed {file_name} with new project name: {project_name}")
            else:
                print(f"{file_name} does not exist.")
    except Exception as error:
        print("Error occurred while renaming the project ->", error)


main()
