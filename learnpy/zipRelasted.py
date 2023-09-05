import zipfile
import os
import shutil

def file_compress(files,output_zipfile):
    try:
        zf = zipfile.ZipFile(output_zipfile,mode='w')
        zf.write(files,compress_type=zipfile.ZIP_DEFLATED)
    except Exception as e:
        print("Exception occured during zip process")
    finally:
        zf.close()

def folder_compress(files,output_zipfile):
    shutil.make_archive(output_zipfile,'zip',files)

def folders_compress(folders,output_zipfile):
    try:
        with zipfile.ZipFile(output_zipfile,'w') as zipObj:
            for onefolder in folders:
                for folderName , subFolders , fileNames in os.walk(onefolder):
                    for onefile in fileNames:
                        onefile_path = os.path.join(folderName,onefile)
                        zipObj.write(onefile_path)
    except Exception as e:
        print("Exception occured during zip process")
    finally:
        zipObj.close()


zipfilename = "test.zip"
folders = ["./data","./packge"]
folders_compress(folders,zipfilename)
