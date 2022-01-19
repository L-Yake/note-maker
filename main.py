"""
    NoteMaker,
        a python script run in the command line for getting a head start on taking notes!

        author, Marikit Cecilia
        date, 08-Jan-2022
        version, 0.1.1
        dependencies, {
            "templates" = [ 
                templates/defaultTemplate, 
                templates/annotatedBibliographyTemplate
                ]
        }

    noteGenerator() calls specifyDirectory() and noteNameGen() to validate paths and generate formatted note titles respectively.

    Current stable output formats: txt, md, html

    NEEDS: A GITHUB REPO
"""

import time
import os
import sys
import templates


def noteNameGen(destinationPath:str , fileName: str, fileFormat: str = "txt"):
    """
    Generates a new file path and title.
    :params:
        destinationPath (str): [description]
        fileName (str): [description]
        fileFormat (str, optional): [description]. Defaults to "txt".

    :returns:
        newFilePath: new file path generated using the new file name and its declared format.
        notesTitle: Title of the newly generated file name.
    """
    # Compatible formats:  txt, md, html
    notesTitle = fileName.split(".")[0].strip().replace(" ", "-")
    # Implicit list conversion for joining path to title and file format
    newFilePath = "/".join([str(destinationPath), (notesTitle + "_notes." + fileFormat)])
    return newFilePath, notesTitle


def specifyDirectory(pathType: str, path: str) -> str:
    """
    Walks user through specifying a source or destination directory.

    :params:
        pathType (str): source/destination, the type of path a user will be specifying to create files.

    :returns:
        str: Returns a validated destination path or 0
    """
    DEFAULT_DESTDIRECTORY_NAME = "./research-notes/"
    # Does user want to specify a directory?
    # If not, this will generate a destination directory automatically
    print(f"No {pathType} directory specified or detected.\n")
    response = input(f"\nWould you like to specify a {pathType} directory now? (Y/N): ").lower().strip()

    if response == "y":
        path = input("Please enter your desired directory name now: \n")
        if not os.path.exists(path):
            os.mkdir(path)
            print(f"\nCreating \"{path}\" for you now c:\n")
            return path


    elif response == "n":
        if not os.path.exists(path):
            os.mkdir(path)
            print(f"\nCreating \"{path}\" for you now c:\n")
            return path

    # elif response == "n" and not os.path.exists(path):
    #     print("Sorry! NoteMaker cannot help you this time since you don't have a source folder. ")

    elif response == "default":
        path = DEFAULT_DESTDIRECTORY_NAME
        if not os.path.exists(path):
            os.mkdir(path)
            print(f"\nCreating \"{path}\" for you now c:\n")
            return path

    else:
        print("\nPlease try again.")
        time.sleep(2.0)
        return 0


def noteGenerator(sourcePath: str = None, destPath: str = None, fileFormat: str = "txt", noteType: str = "note") -> None:
    """
    Generates notes originating from the source path and populates the destination path.

    :params:
        sourcePath (str): Source directory path containing files for note generation.
        destPath (str): Destination directory path for note generation.
        fileFormat (str): Can currently specify [txt, md, html] formats. (DO NOT include "." in argument)

    :returns:
        Files generated are named using the newFileName variable,
            newFileName = destPath + notesTitle + "." + fileFormat

            for example:
                newFileName = "./research-notes/INTERVIEW001_SUMMARY.txt"
    """
    STABLE_FORMATS = ["md", "txt", "html"]

    # If there is no specified source directory, prompts user to create one
    if sourcePath is None or not os.path.exists(sourcePath):
        specifyDirectory("source", sourcePath)

    # If there is no specified destination directory, prompts user to create one
    elif destPath is None or not os.path.exists(destPath):
        destPath = specifyDirectory("destination", destPath)

    # Reads the names of every file in Source Directory Path
    for fileName in os.listdir(sourcePath):
        newFileName = noteNameGen(destPath, fileName, fileFormat)

        # If the new file has not been created before, add it to the destination directory
        if (newFileName[1] + "." + fileFormat) not in os.listdir(destPath):
            if fileFormat in STABLE_FORMATS:
                match noteType:
                
                    case "note":
                        # Creates fileNames based on research paper titles and specified file format
                        templates.defaultTemplate(newFileName[0], newFileName[1], fileFormat)
                
                    case "bib":
                        # Creates fileNames based on research paper titles and specified file format
                        templates.annotatedBibliographyTemplate(newFileName[0], newFileName[1], fileFormat)
            else:
                print("Please use supported note formats! [txt, md, html]\nTIP: When entering file format, do NOT use a period.")

    print("\nResearch Notes Created!")
    return 1


if __name__ == "__main__":
    # print(sys.argv)
    source = sys.argv[1]
    destination = sys.argv[2]
    outputFormat = sys.argv[3]
    noteType = sys.argv[4]
    noteGenerator(source, destination, outputFormat, noteType)
