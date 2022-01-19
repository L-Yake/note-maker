# NoteMaker

Date : 19 Jan 2022
Author : Marikit Yake


Update Details:


        version 0.1.1 -- Pushed to Github for easier sharing.

        version 0.1.0 -- Added match/case syntax from Python 3.10 to declutter my code base.

        version 0.9.0 -- Updated/Added templates to Templates.py 
<hr>

A python script for generating notes ready to write in!

<br>
<hr>

## Code Execution Examples:

        /c/User/marikit/desktop>main.py source-folder/ notes-folder/ fileFormat noteFormat

My personal use-case:

        /c/User/marikit/desktop>main.py research-articles/ research-notes/ md bib

<br>
<br>

(REQUIRED) Arguments breakdown:

        main.py -- Runs the noteGenerator function with the following inputs.

        source-folder/ -- A folder containing all of the desired files and directiories you want to generate a templated note for.

        notes-folder/ -- The target folder. Where we'd like all of our templated notes to go.

        fileFormat -- The output format for the templated notes. 
                Stable formats include: txt, md, html (so, basically any plain text files)

        noteFormat -- The desired output template format. Current 
                accepted formats: note, bib (short for annotated-bibliography)

