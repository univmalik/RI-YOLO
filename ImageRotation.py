import cv2

def rotImage(fileNameJPG):
    img = cv2.imread(fileNameJPG)
    out = cv2.transpose(img)
    out = cv2.flip(out, flipCode=1)

    newFileSize = len(fileNameJPG)
    newFileName = fileNameJPG[0:newFileSize - 4] + "-ROT90.jpg"
    print(newFileName)
    cv2.imwrite(newFileName, out)

def rotImage180(fileNameJPG):
    if (fileNameJPG.find("-ROT90") != -1):
        img = cv2.imread(fileNameJPG)
        out = cv2.transpose(img)
        out = cv2.flip(out, flipCode=1)

        newFileSize = len(fileNameJPG)
        newFileName = fileNameJPG[0:newFileSize - 10] + "-ROT180.jpg"
        print(newFileName)
        cv2.imwrite(newFileName, out)

def rotImage270(fileNameJPG):
    if (fileNameJPG.find("-ROT180") != -1):
        img = cv2.imread(fileNameJPG)
        out = cv2.transpose(img)
        out = cv2.flip(out, flipCode=1)

        newFileSize = len(fileNameJPG)
        newFileName = fileNameJPG[0:newFileSize - 11] + "-ROT270.jpg"
        print(newFileName)
        cv2.imwrite(newFileName, out)
