import os
import shutil


def copy_dir(src: str, dst: str) -> None:
    if not os.path.exists(src):
        print(f"{src} path does not exist")
        return
    if os.path.exists(dst):
        shutil.rmtree(dst)
    _copy_dir(src, dst)


def _copy_dir(src: str, dst: str) -> None:
    if not os.path.exists(dst) and not os.path.isfile(src):
        print(f"creating {dst}")
        os.mkdir(dst)
    if os.path.isfile(src):
        print(f"copying {src} to {dst}")
        shutil.copy(src, dst)
        return
    for content in os.listdir(src):
        _copy_dir(os.path.join(src, content), os.path.join(dst, content))


if __name__ == "__main__":
    copy_dir(
        "/home/lukas/Documents/Github/static-site-generator/static",
        "/home/lukas/Documents/Github/static-site-generator/public",
    )
