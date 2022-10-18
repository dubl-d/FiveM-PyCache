import os
import time
import stat
import shutil

home_dir = os.path.expanduser( '~' )
cache = os.path.join( home_dir, 'AppData', 'Local', 'FiveM', 'Fivem.app', 'data', 'cache' )
server_cache = os.path.join( home_dir, 'AppData', 'Local', 'FiveM', 'Fivem.app', 'data', 'server-cache', )
cache_priv = os.path.join( home_dir, 'AppData', 'Local', 'FiveM', 'Fivem.app', 'data', 'server-cache-priv' )
if cache and server_cache and cache_priv:
    print( cache,"\n",server_cache,"\n",cache_priv,"\nWill all be deleted.")
if os.path.exists(cache):
    os.chmod(cache,stat.S_IRUSR|stat.S_IRGRP|stat.S_IROTH|stat.S_IXUSR|stat.S_IRUSR|stat.S_IWUSR|stat.S_IWGRP|stat.S_IXGRP)
    shutil.rmtree(cache)
if os.path.exists(server_cache):
    os.chmod(server_cache,stat.S_IRUSR|stat.S_IRGRP|stat.S_IROTH|stat.S_IXUSR|stat.S_IRUSR|stat.S_IWUSR|stat.S_IWGRP|stat.S_IXGRP)
    shutil.rmtree(server_cache)
if os.path.exists(cache_priv):
    os.chmod(cache_priv,stat.S_IRUSR|stat.S_IRGRP|stat.S_IROTH|stat.S_IXUSR|stat.S_IRUSR|stat.S_IWUSR|stat.S_IWGRP|stat.S_IXGRP)
    shutil.rmtree(cache_priv)
print("Your FiveM cache has been deleted please restart FiveM")
time.sleep(10)
