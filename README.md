# Fashion-fastAPI

## Instructions of use (Of course you will need [Python](python.org) to run this)

1. Download the code zip file by clicking on Code then Download ZIP
2. Extract the zip file (Just select extract here and not to another folder as there is already a folder inside the zip)
3. Create a new directory for this project
4. create a virtual environment in the project directory by running `python -m venv venv`
5. place the contents of the extracted zip folder into the root of the project directory you created 
6. Download the fashion-classifier model from https://huggingface.co/Odenusi/fashion-classifier/tree/main
7. place the pickle file in the root of the project directory. Your project directory should look like this: ![image](https://github.com/Odenusi/fashion-fastAPI/assets/126173522/6d5960d7-f261-4f71-9f21-317487d94dca)
8. Open a terminal window and run `pip install -r requirements.txt`
9. Run the main.py (this is the file that starts the RESTfulAPI so it needs to be running all the time. The reason it is not set to run automatically is because it can be "resource hungry on your system.)
10. You can now run the send_img.py file as it is to test the model on the test.zip file located in the zip_folder/zipped directory or you can put your own zip file in the zip_folder/zipped directory and edit the send_image.py file (line 8) with the name of your zip file. Then all you would need to do is change the zip file in the zip_folder/zipped directory (keeping the name the same as it is in send_img.py of course.)
11. Open Windows task scheduler and import the Send_images.xml file (this is the scheduler file that will run send_img.py every day at midnight) by clicking the "Import Task..." Button on the right side of the window.
12. Edit the Send_images task by going to Actions and changing the Program/Script path to the path of the Python executable in your virtual environment. (This would look something like this: `"...\.venv\Scripts\python.exe"`
13. Make sure that "Add arguments" is set to send_img.py and "Start in" is set to your project directory (Where send_img.py and main.py are)
14. It is probably not midnight so to test the scheduled task, click the run button on the right of the Windows task scheduler window
15. If Everything went well, you should have an "output.csv" file containing the predictions in your project directory.
