# Unit Personnal Management System

## Folder structure
project/ 
│ 
├── main.py // The main file with server and methods
├── utils/ 
    ├── io.py // For work with json 
    ├──helper.py // Every functions You need for Your work that not endpoint/IO 
├── logger_config.py // 
├── soldiers.json // Storage the list of all soldiers
├── system.log // Documentation of all logs from the moment the server was started
│ 
└── requirements.txt // Library from what you need to instaal before running
└── readme.md // Exsplanantion about the project and how to run
└── diagram.pdf // Server Flowchart

## Explanation of the construction of the project
In this project I bild a crud server with five methods, It can to get all soldiers,
Get a single soldier, Create a new soldier, Update soldier, And delete soldier.
The list of all soldiers is stored in a json file for that i had to made functions that load and save,
In methods create and update I had to did validatin and I did it with 
base modul from modlue pydntic I made a class that ensurs 
that all fields in the sildier dictionary filled currectly.

## What to install
pip install -r requierments.txt

## how to run
uvicorn main:app