import os
import os.path
import shutil

lib_path = os.path.join('lib', 'Middlewares')

shutil.rmtree(lib_path, ignore_errors=True)
os.mkdir(lib_path)

for root, dirs, files in os.walk('Middlewares'):
    for file in files:
        if file.endswith('.c') or file.endswith('.h'):
            shutil.copy2(os.path.join(root, file), lib_path)

lib_path = os.path.join('lib', 'Drivers')
shutil.rmtree(lib_path, ignore_errors=True)
os.mkdir(lib_path)

for root, dirs, files in os.walk('Drivers'):
    for file in files:
        if file.endswith('.c') or file.endswith('.h'):
            shutil.copy2(os.path.join(root, file), lib_path)