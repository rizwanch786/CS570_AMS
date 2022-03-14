##  Attendance Management system using Face👦🏻👧 Recognition 

### Code Requirements
- Python 3.8(install from official site)
- Pycharm (latest Version)
- Opencv(`pip install opencv-python`)
- Tkinter(Available in python)
- PIL (`pip install Pillow`)
- Pandas(`pip install pandas`)

### What steps you have to follow??
- Create a `TrainingImage` folder in a project.
- Open a `AMS_Run.py` and change the all paths with your system path
- Run `setup.exe`.

### Project Structure
- First an admin should be login into the system and then it enters data for enrollment.
- After run you need to give your face data to system so enter your ID and name in box than click on `Take Images` button.
- It will collect 200 images of your faces, it save a images in `TrainingImage` folder
- After that we need to train a model(for train a model click on `Train Image` button.
- It will take 5-10 minutes for training(for 10 person data).
- After training click on `Automatic Attendance` ,it can fill attendace by your face using our trained model (model will save in `TrainingImageLabel` )
- it will create `.csv` file of attendance according to time & subject.
- You can store data in database (install wampserver),change the DB name according to your in `AMS_Run.py`.
- `Manually Fill Attendace` Button in UI is for fill a manually attendance (without facce recognition),it's also create a `.csv` and store in a database.
- Then for quit you click on X on the top right corner.

### Notes
- It will require high processing power(I have 8 GB RAM & 2 GB GC)
- If you think it will recognise person just like humans,than leave it ,its not possible.
- Noisy image can reduce your accuracy so quality of images matter.