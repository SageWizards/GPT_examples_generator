import subprocess

import semver


def main():
    # Obtén la etiqueta más reciente en el repositorio
    result = subprocess.run(
        ["git", "describe", "--abbrev=0", "--tags"],
        capture_output=True,
        text=True,
        check=False,
    )
    latest_tag = result.stdout.strip()

    # Si no hay etiquetas, utiliza 0.0.0 como versión base
    if not latest_tag:
        latest_tag = "0.0.0"

    # Incrementa la versión utilizando semver (p.ej., 1.0.0 -> 1.0.1)
    incremented_version = semver.VersionInfo.parse(latest_tag).bump_patch()

    # Verificar si la etiqueta ya existe
    existing_tags = (
        subprocess.run(
            ["git", "tag", "--list"],
            capture_output=True,
            text=True,
            check=True,
        )
        .stdout.strip()
        .split("\n")
    )

    if str(incremented_version) in existing_tags:
        print(f"La etiqueta {incremented_version} ya existe.")
        return

    # Crear una nueva etiqueta con la versión incrementada
    subprocess.run(
        ["git", "tag", str(incremented_version)],
        check=True,
    )

    print(f"Etiqueta creada: {incremented_version}")


if __name__ == "__main__":
    main()
