Fashion-fastAPI

Instructions of use
1. Download the code zip file by clicking on Code then Download ZIP
2. Extract the zip file
3. Create a new directory for this project
4. create a virtual environment in the project directory by running python -m venv venv
5. place the contents of the extracted zip folder into the root of the project directory you created 
6. Download the fashion-classifier model from https://huggingface.co/Odenusi/fashion-classifier/tree/main
7. place the pickle file in the root of the project directory
   Your project directory should look like this: ![image](https://github.com/Odenusi/fashion-fastAPI/assets/126173522/cba3a948-9744-437a-945e-10b05f2fdb3c)
8. Open a terminal window and run "pip install -r requirements.txt"
9. While the requirements are being installed import the Send_Images.xml file as a task in Windows Task Scheduler
10. Run the main.py (this is the file that starts the RESTfulAPI so it needs to be running all the time)
11. You can now run the send_img.py file as it is to test the model on the test.zip file located in the zip_folder/zipped directory or you can put your own zip file in the zip_folder/zipped directory and edit the send_image.py file (line 8) with the name of your zip file.
12. Open Windows task scheduler and import the Send_images.xml file (this is the scheduler file that will run send_img.py every day at midnight)
13. Edit the Send_images task by going to Actions and changing the Program/Script path to the path of the Python executable in your virtual environment.
14. Make sure that "Add arguments" is set to send_img.py and "Start in" is set to your project directory (Where send_img.py and main.py are)
15. It is probably not midnight so to test the scheduled task, click the run button on the right of the windows task scheduler window
