![This is Image](https://miro.medium.com/max/1400/1*PDA9zADqD9qqCu-CmJ9Ddw.gif)
# Automation Face Recognization Based Attandance System
Face recognition system is very useful in life applications especially in security
control systems. The airport protection system uses face recognition to identify suspects and
FBI (Federal Bureau of Investigation) uses face recognition for criminal investigations. In our
proposed approach, firstly, video framing is performed by activating the camera through a user-
friendly interface. The face ROI (Regions of Interest) is detected and segmented from the video
frame by using LBPH algorithm. In the pre-processing stage, scaling of the size of images is
performed if necessary, in order to prevent loss of information. The median filtering is applied
to remove noise followed by conversion of color images to grayscale images. After that,
contrast-limited adaptive histogram equalization (CLAHE) is implemented on images to
enhance the contrast of images. In face recognition stage, enhanced local binary pattern (LBP)
and is applied in order to extract the features from facial images. In our proposed approach, the
enhanced local binary pattern outperforms the original LBP by reducing the illumination effect
and increasing the recognition rate. Next, the features extracted from the test images are
compared with the features extracted from the training images. The facial images are then
classified and recognized based on the best result obtained from the combination of algorithm,
enhanced LBP. Finally, the attendance of the recognized student will be marked and saved in
the excel file as well as in database. The student who is not registered will also be able to
register on the spot and teacher would also not mark his/her attendance. The average accuracy
of recognition is 100 % for good quality images, 94.12 % of low-quality images and 95.76 %
for face stored in directory when two images per person are trained.

## The repository includes:
* Source Code
* GUI Screen Shoots
### What steps you have to follow??
- Create a `TrainingImage` folder in a project.
- Open a `AMS_Run.py` and change the all paths with your system path
- install xamp server for data base
- create a user `username: ali` and `password: 123`
- create following db's: `Face_reco_DB`, `manually_fill_attendance` and `userdata`
- Run `setup.exe`.

### Project Structure
- First an admin should be login into the system and then it enters data for enrollment.
  `username: ali` `password: 123`
- After run you need to give your face data to system so enter your ID and name in box than click on `Take Images` button.
- It will collect 70 images of your faces, it save a images in `TrainingImage` folder
<br />
  ![This is Dataset]()

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
