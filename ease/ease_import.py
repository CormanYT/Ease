def import_file(strin):
    this = """
try:
    from {FILENAME} import *
except ImportError:
    from .{FILENAME} import *
"""
    this = this.replace("{FILENAME}", strin)
    exec(this)
def import_files(files):
    for item in files:
        import_file(item)
