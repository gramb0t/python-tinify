import tinify
import apikey
import os

tinify.key = hidden
activeDir = 'c:/users/gnanke/PycharmProjects/tinify/images/'
dirListing = os.listdir(activeDir)
compressions_this_month = str(tinify.compression_count)

def directoryList() :
    for file in dirListing:
        fileSize = round(os.path.getsize(activeDir+'/'+file) / 1000000, 2)
        print(file + ' and is ' +str(fileSize)+' mb')
        full_dir_path = 'c:/users/gnanke/PycharmProjects/tinify/images/'
        compressed_dir_path = 'c:/users/gnanke/PycharmProjects/tinify/images/compressed/'
        fullFilePath = full_dir_path + file
        fullCompressedFilePath = compressed_dir_path + file
        print('About to compress: ' + file)
        print('started compression of: ' + file)
        try:
            source = tinify.from_file(fullFilePath).to_file(fullCompressedFilePath)
        except:
            print('compression has failed.')
        else:
            # define new file name file_comp.jpg
            print('Compression success!')
            print(fullCompressedFilePath + ' Has been created')


def title() :
    print('***************************************************')
    print('* TINIFY ****** making things smaller ****** V.01 *')
    print('***************************************************')
    print('* ' + activeDir +'  *')
    print('***************************************************')
    print('* ' +str(len(dirListing)) + ' files in current dir.                        *')
    print('***************************************************')
    print('* Actions this month: '+compressions_this_month +'              *')
    print('***************************************************')
    # directoryList()
    print('\n')

def compressDirectory(toCompress) :
    for file in toCompress :
        print(file)
        print('About to compress: ' + fileName)
        print('started compression of: ' + fileName)
        try:
            source = tinify.from_file(fullFilePath).to_file(compressedFilePath)
        except:
            print('compression has failed.')
        else:
            # define new file name file_comp.jpg
            print('Compression success!')
            print(compressedFilePath + ' Has been created')
            return compressedFilePath


def compressImage(dir, fileName) :
    fullFilePath = str(dir + fileName)
    compressedFilePath = str(dir + 'compressed/' + fileName)
    print('About to compress: '+fileName)
    proceed = input('Proceed? ')
    if proceed == "y" or "yes" :
        print('started compression of: '+fileName)
        try:
            source = tinify.from_file(fullFilePath).to_file(compressedFilePath)
        except :
            print('compression has failed.')
        else:
            # define new file name file_comp.jpg
            print('Compression success!')
            print(compressedFilePath +' Has been created')
            return compressedFilePath


    else:
        print('compression aborted.')
title()

current_image_name = 'Page 07 March 2017'
current_file_extension = '.jpg'
current_file_to_compress = current_image_name + current_file_extension

# compressImage(activeDir, current_file_to_compress)
# compressDirectory(activeDir)



