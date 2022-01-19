# NoteMaker

Date : 19 Jan 2022
Author : Marikit Yake


Update Details:


        version 0.1.1 -- Pushed to Github for easier sharing.

        version 0.1.0 -- Added match/case syntax from Python 3.10 to declutter my code base.

        version 0.9.0 -- Updated/Added templates to Templates.py 
<br>
<hr>

## Dependencies
**Python Version 3.10**

Templates/templates.py -- A python module I wrote for this project, containing functions-as-formats.

<hr>

## Purpose
A **command-line** application for automating generation of templated notes, ready-to-write in. A use-case I find myself needing often, especially when I'm having a hard time starting an assignment. This abstracts and automate away "setting up" my notes which helps me get to taking notes faster and in a better format.
<br>

### Current personal use-case
For a research project's literature review, I needed a quick way to template my notes so I could take them in a quick, well-organized manner since I need to read <18 research papers. Instead of copying and pasting a template "by-hand", I automated the process through Python.
<br>
<hr>

## Project Goals
- Trying to create a Python program in the functional programming paradigm (to the exent of my knowledge).
- Using as few external libraries as possible. (a.k.a. Pure Python)
- Capture user-input from the command line interface ( CLI ).
- Creating an application that is not solely for personal use.
<br>
<hr>


## Code Execution Examples:

        /c/User/marikit/desktop>main.py source-folder/ notes-folder/ fileFormat noteFormat

My personal use-case:

        /c/User/marikit/desktop>main.py research-articles/ research-notes/ md bib

<br>


(REQUIRED) Arguments breakdown:

        main.py -- Runs the noteGenerator function with the following inputs.

        source-folder/ -- A folder containing all of the desired files and directiories you want to generate a templated note for.

        notes-folder/ -- The target folder. Where we'd like all of our templated notes to go.

        fileFormat -- The output format for the templated notes. 
                Stable formats include: txt, md, html (so, basically any plain text files)

        noteFormat -- The desired output template format. Current 
                accepted formats: note, bib (short for annotated-bibliography)

