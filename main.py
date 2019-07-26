import TextRotation
import fileHandle
import ImageRotation

# Enter file address here like this
# textFileAddress = "C:/Users/Administrator/PycharmProjects/openCV/img/"
textFileAddress = ""
jpgFileAddress = ""

listFileTXT = fileHandle.files_LTXT(textFileAddress)
listFileJPG = fileHandle.files_LJPG(jpgFileAddress)

for file in listFileJPG:
    ImageRotation.rotImage(file)

# update list
listFileJPG = fileHandle.files_LJPG(jpgFileAddress)

for file in listFileJPG:
    ImageRotation.rotImage180(file)

listFileJPG = fileHandle.files_LJPG(jpgFileAddress)

for file in listFileJPG:
    ImageRotation.rotImage270(file)


for file in listFileTXT:
    TextRotation.rotTextC(file)

listFileTXT = fileHandle.files_LTXT(textFileAddress)

for file in listFileTXT:
    TextRotation.rotTextC180(file)

listFileTXT = fileHandle.files_LTXT(textFileAddress)

for file in listFileTXT:
    TextRotation.rotTextC270(file)

TextRotation.rotTextC("cv.txt")
TextRotation.rotTextC180("cv-ROT90.txt")
TextRotation.rotTextC270("cv-ROT180.txt")

#
# TextRotation.rotTextC("cv.txt")

# TextRotation.rotTextC("cv.txt")


# test = "0 0.255674 0.565456 0.752567 0.667356\n" + \
#        "1 0.333334 0.734346 0.232567 0.867356\n" +  \
#        "2 0.255674 0.865456 0.852567 0.267356\n" + \
#        "1 0.733334 0.134346 0.932567 0.167356\n" + \
#        "3 0.733334 0.134346 0.932567 0.167356\n"
#
#
# originalList = TextRotation.getValues(test)
#
#
# rotList = TextRotation.rotatedList(originalList)
#
# # print(rotList)
#
# intCList = TextRotation.IntCLIST(rotList)
#
# finalStr = TextRotation.finalString(intCList)
