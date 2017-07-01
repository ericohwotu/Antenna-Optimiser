# compress zip arcives for
"""Compress all files in a folder to a zip

except other zip files"""
import zipfile, os, shutil

def run():
    #get number of zip files from folder
    exempt = ['.zip','.py','.bat']
    count = len([f for f in os.listdir() if '.zip' in f]) + 1
    files = [f for f in os.listdir() if not any(x in f for x in exempt)]

    #transfer everything to zipfile
    zipname = 'Antenna_run_' + str(count) + '.zip'
    if not len(files)==0:
        myzip = zipfile.ZipFile(zipname, 'w')

    #copy files to zip
    for file in files:
        
        if '.' in file:
            try:
                myzip.write(file, file, zipfile.ZIP_DEFLATED)
                os.remove(file)
            except Exception:
                pass
        else:
            subs = [f for f in os.listdir(file)]
            for sub in subs:
                myzip.write(file + '\\' + sub, file +'\\' + sub, zipfile.ZIP_DEFLATED)

            try:
                shutil.rmtree(file)
            except Exception:
                pass
        
    
if __name__ == "__main__":
    run()
