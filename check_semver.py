"""Crea una nueva etiqueta semver basada en la última etiqueta existente en el
repositorio."""
import subprocess

import semver


def main():
    # Fetch all tags from the remote repository
    subprocess.run(["git", "fetch", "--tags"], check=True)

    # Obtain the latest tag from the repository
    result = subprocess.run(
        ["git", "describe", "--abbrev=0", "--tags"],
        capture_output=True,
        text=True,
        check=False,
    )
    latest_tag = result.stdout.strip()

    # If there are no tags, use 0.0.0 as the base version
    if not latest_tag:
        latest_tag = "0.0.0"

    # Increment the version using semver
    incremented_version = semver.VersionInfo.parse(latest_tag).bump_patch()

    # Create a new tag with the incremented version
    subprocess.run(
        ["git", "tag", str(incremented_version)],
        check=True,
    )

    print(f"Tag created: {incremented_version}")


if __name__ == "__main__":
    main()
