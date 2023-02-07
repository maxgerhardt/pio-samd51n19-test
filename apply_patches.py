from os.path import join, isfile
import shutil

Import("env")

FRAMEWORK_DIR = env.PioPlatform().get_package_dir("framework-arduino-samd-adafruit")
PLATFORM_DIR = env.PioPlatform().get_dir()
patchflag_path = join(FRAMEWORK_DIR, ".patching-done")

# patch file only if we didn't do it before
if not isfile(join(FRAMEWORK_DIR, ".patching-done")):
    original_file = join(FRAMEWORK_DIR, "cores", "arduino", "WVariant.h")
    original_file_backup = join(FRAMEWORK_DIR, "cores", "arduino", "WVariant.h.backup")
    patched_file = join("patched_core_files", "WVariant.h")

    assert isfile(original_file) and isfile(patched_file)

    # make a backup of the orignal file
    shutil.copy(original_file, original_file_backup)
    # copy our patched file to the original file
    shutil.copy(patched_file, original_file)
    # also take the opportunity to copy the SVD file to the platform folder
    svd_src = join("boards", "ATSAMD51N19A.svd")
    svd_dest = join(PLATFORM_DIR, "misc", "svd", "ATSAMD51N19A.svd")
    assert isfile(svd_src)
    shutil.copy(svd_src, svd_dest)

    def _touch(path):
        with open(path, "w") as fp:
            fp.write("")
        print("=== PATCHED FRAMEWORK AND PLATFORM FILES OK ===")

    env.Execute(lambda *args, **kwargs: _touch(patchflag_path))