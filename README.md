# An architecture to build a multimodal dataset for gesture recognition
This project consist in two software architectures, one that allows to easily acquire data from the three available sensors (i.e. Kinect, Smartwatch and MOCAP) in order to build a multimodal dataset and the other one is to visualize the data stored.
The dataset will be built for 5 types of gesture, namely pouring, drinking, sitting down, standing up and walking, using the sensors mentioned above.

## Authors
* Francesco Porta: francy857@gmail.com
* Davide Piccinini: piccio98dp@gmail.com
* Sara Romano: sara.romano.15@gmail.com
* FirstName LastName: email@email.com

## Architecture of the System
Here is the dataset creation architecture: the "Experimenter_GUI" is the graphical user interface used to actively interact with the underlying program; the "Gesture Sequence Generator" module is the implementation of a service-client pattern's server; 
(COMPLETE THE FOLLOWING PART)
the three sensor modules manage the interaction between the hardware and the software; the record modules create a rosbags containing all data from the sensors recorded when they are required by user; the "Conversion and Segmentation" module convert the "rosbag" into "csv" format and assigns labels to the data.

<p align="center"> 
<img src="https://github.com/FraPorta/Itslit/blob/master/ExperimenterDiagram.jpg?raw=true">
</p>

## Contents of the repository
In this section we will explain the repository's content.

### Pictures
This folder contains the several images that need to be displayed in the GUI in order to concisely communicate to the user what gesture he/she has to perform at a given time.

### Launch
This folder contains the launchfile that executes the whole program.

### Src
This folder contains all the nodes that make up the main program: "GUI_node" initializes the GUI and deals with the logic behind the graphical elements, which makes the user navigate between windows, write personal informations, select which sensors to use, and so on; the "gestures_nodes" implements the server which manages the request for a random gesture sequence; the "fake_node_imu" creates fake simulated data from the Smartwatch; the "Smartwatch_node" manages data from Smartwatch sensor: it saves data when it is required by user; the "Recorder_IMU" saves data Imu into a Rosbag; the "fake_node_pc" create fake simulated data from the Kinect; the "kinect_node" manages data from Kinect sensor: it saves data when it is required by user; the "Recorder_PC" saves data PointCloud2 into a Rosbag;
In addition to these 2 files, there's also the following folder.


#### Lib
This folder contains 2 important sub-folders.

##### Tools
This folder contains code which is needed in bigger programs: "gesture_sequence_client" implements the class to istantiate the client side of the service-client pattern; "startmsg_publisher" implements the class to create the publisher side of a publish-subscribe pattern.

##### Windows
This folder contains the code which encapsulates both the windows and their elements, which are istantiated in "GUI_node": here lies the code for the configuration window, the recording/communication with user window and the several tutorial windows.
The code consists in classes created using "Qt5Designer" a program which lets you build up a graphical user interface by dragging components onto a window: we end up with a ".ui" file, which is then converted to python code.

### Srv
This folder contains the simple ".srv" file that encodes the request-response structure of the service-client pattern.

## Installation and System Testing 
This section presents (in its sub-sections) how to install/run and test the modules. **Note that:** If all the modules have successfully completed their work and integrated everything together, then this section can present the overall **Installation and Testing** procedure for the the "whole" system, instead of having a sub-section dedicated for each module. 

Please keep in mind, **do not** include in your repository the “entire” code of the external libraries that your module may use. Hence accordingly, **describe** to the new users how they can “install” the external libraries and then **describe** how they can “install” your module that uses those libraries. Afterwhich, **describe** how to run and test your module. Finally, show **(i)** the rqt_graph generated when the module is running, **(ii)** images or links to the videos showing the working of the module (in real or in simulation).

## Installation
The first thing to do, after having cloned the repository in the Ros workspace, is to build the package and install in order to make the ‘msg’ and ‘srv’ files executable, using the following commands in the workspace:
    
    ```
    catkin_make
    catkin_make install
    ```

Then it is necessary to install a Ros related Python library (this passage may not be required if the pc on which the modules will be installed has already other Ros projects developed with Python 3). 
    
    ```
	sudo apt-update
	sudo apt install python3-pip
    sudo apt-get install python3-yaml	
    sudo pip3 install rospkg catkin-pkg 
    pip3 install --user pyqt5
	sudo apt-get install python3-pyqt5
    ```

To run the system:
    
    ```
    roslaunch multimodal_dataset_creation fake_nodes.launch
    roslaunch multimodal_dataset_creation experimenter_GUI.launch
    ```

# Rqt_graph
<p align="center"> 
<img src="">
</p>

### Modules
* "Experimenter_GUI" Module
* "Gesture Sequence Generator" Module
* "Fake Imu" Module
* "Smartwatch" Module
* "Fake PointCloud2" Module
* "Kinect" Module
* "Recorder Imu" Module
* "Recorder PC" Module
* "Conversion and Segmentation" Module



# What else should we add?
	
## Report (To be added)

This is the link to the report: [Project 13 report]()





# Useful GitHub readme syntax

## To make bullet points

* Do this
	* Do this

## To make hyper-link

For example, making a link to [ROS tutorials](http://wiki.ros.org/ROS/Tutorials)

## To show, how to execute some commands in the terminal

    ```
    sudo apt install ros-kinetic-opencv3 #(should be already installed with previous point)
    sudo apt install ros-kinetic-opencv-apps
    ```

## To exphasize about a particular command

For example: Please do a ```catkin_make```, once you have modified your code. 

## To add image(s) or video(s)

* To embbed an image

<p align="center"> 
<img src="https://github.com/yushakareem/test-delete/blob/master/light-bulb-2-256.gif">
</p>

* To link a [video](https://youtu.be/-yOZEiHLuVU)

## References

[Concept guide.](https://guides.github.com/features/wikis/)

[Syntax guide.](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)

[Link to the repository that has this readme.](https://github.com/EmaroLab/GitHub_Readme_Template)
