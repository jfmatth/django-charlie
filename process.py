import argparse
import csv

CSVHEADER=["folder",'file','size']

def processline(linein):
    # returns a better CSV version of the line

    # strip out the folder + filename 
    intflagspos = linein.find("flags=")

    # folder + filename is [1:flagpos]
    strFolderAndFile = linein[1:intflagspos]

    # split the folderAndFile into a set by ' 1:'
    slcFolderParts = strFolderAndFile.split(" 1:")

    strFilename = slcFolderParts[-1].strip()
    strFolder = strFolderAndFile[:-len(strFilename)].replace(" 1:","/").strip()

    # the size of the file is at size=xxxxxx in the original line
    intSize = linein[linein.find("size="):].split(" ")[0][5:]

    return [strFolder, strFilename, intSize]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filein")
    parser.add_argument("fileout")

    args = parser.parse_args()

    with open(args.filein) as fIn:
        with open(args.fileout,"w") as fOut:
            writer = csv.writer(fOut, delimiter=',', quotechar='"')

            # write the header to the CSV first
            writer.writerow(CSVHEADER)

            for l in fIn.readlines():
                if l[0] == "f":
                    writer.writerow(processline(l) )

    fIn.close()
    fOut.close()



if __name__ == "__main__":
    main()


    # with open('eggs.csv', 'w', newline='') as csvfile:
    # spamwriter = csv.writer(csvfile, delimiter=' ',
    #                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    # spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
