import datetime

def defaultTemplate(notesFilePath: str, notesTitle: str, fileType:str) -> None:
    """
    input: Name of notes file for writing to
    output: Default notes template output,

        'Title: name-of-file


        Date Generated: xx-xx-xxxx


        Keypoints:

            -

            -

            -


        Notes:


        '
    """
    match fileType:
        case "md":
            # Creates fileNames based on research paper titles and specified file format
            with open(notesFilePath, mode="w") as notesFile:
                notesFile.write("# " + notesTitle)
                notesFile.write("\nDate Generated: " + str(datetime.date.today()) + "\n<hr>")
                notesFile.write("\n\n## Keypoints: \n\n\t-\n\n\t-\n\n\t-")
                notesFile.write("\n\n## Notes:  \n\n")

        case "txt":
            # Creates fileNames based on research paper titles and specified file format
            with open(notesFilePath, mode="w") as notesFile:
                notesFile.write("Title: " + notesTitle)
                notesFile.write("\n\nDate Generated: " + str(datetime.date.today()))
                notesFile.write("\n\nKeypoints: \n\n\t-\n\n\t-\n\n\t-")
                notesFile.write("\n\nNotes:  \n\n")


def annotatedBibliographyTemplate(notesFilePath: str, notesTitle: str, fileType:str) -> None:
    """
    input: Name of notes file for writing to
    output: Default notes template output,

        'Title: name-of-file

        Date Generated: xx-xx-xxxx

        Notes:




        Citation:

            easybib.com, replace with citation.
    
        '
    """
    match fileType:
        case "md":
            # Creates fileNames based on research paper titles and specified file format
            with open(notesFilePath, mode="w") as notesFile:
                notesFile.write("# " + notesTitle)
                notesFile.write("\nDate Generated: " + str(datetime.date.today()) + "\n<hr>")
                notesFile.write("\n\n## Notes:\n\n")
                notesFile.write("\n\n\n\n## Citations:\n\n\t\teasybib.com, replace with citation.")
        
        case "txt":
            # Creates fileNames based on research paper titles and specified file format
            with open(notesFilePath, mode="w") as notesFile:
                notesFile.write("Title: " + notesTitle)
                notesFile.write("\n\nDate Generated: " + str(datetime.date.today()))
                notesFile.write("\n\nNotes:\n\n")
                notesFile.write("\n\n\n\nCitation:\n\n\t\teasybib.com, replace with citation.")
