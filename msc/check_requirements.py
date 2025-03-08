import pkg_resources

def get_installed_packages():
    """
    Returns a dictionary of installed packages and their versions.
    """
    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    return installed_packages

def write_requirements_to_file(packages, output_file="requirements.txt"):
    """
    Writes the installed packages and their versions to a requirements.txt file.
    """
    with open(output_file, "w") as file:
        for package, version in packages.items():
            file.write(f"{package}=={version}\n")
    print(f"Versions written to {output_file}")

if __name__ == "__main__":
    # Get installed packages and their versions
    installed_packages = get_installed_packages()

    # Write to requirements.txt
    write_requirements_to_file(installed_packages)