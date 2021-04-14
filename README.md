# *QUICK NOTE about viewing our Jupyter Notebook on GitHub*
It has come to our attention that for some people, GitHub doesn't seem to like them viewing our Jupyter Notebook directly on the GitHub website.  Here is a workaround that we have found so that you can view it.  Just click on this link below and you can see our code in all its glory!

https://nbviewer.jupyter.org/github/racstyle/Caught-You-Phone-Handed/blob/main/TeamAsianeering_Project.ipynb

And now, back to our project!

# Staying in touch with your loved ones is important, but don't you think you should stay in touch with the road in front of you more?
Let's face it. We have places to go, sights to see, and people to meet! We also want to let those people know that we are safe and are on our way to meet them!

Wait, "safe"? How safe are we talking about? Safe as in "letting them know by texting on our phones as we drive 75 miles per hour on the highway" safe?

Umm, I do not think so.

Why? Let us see what a couple of reports say about what happens when you text and drive (especially at high speeds).

> * According to the National Safety Council, cell phone use while driving leads to 1.6 million crashes each year on average. [1]
> * In a recent study, at least 36% of all crashes would have been avoided if there was not any distraction while driving. [2]

__References__:
1. [1] "Texting and Driving Accident Statistics - Distracted Driving", [Online]. Available: https://www.edgarsnyder.com/car-accident/cause-of-accident/cell-phone/cell-phone-statistics.html. [Accessed: 01-Dec-2020].
2. [2] J. Atwood, F. Guo, G. Fitch, and T. A. Dingus, “The driver-level crash risk associated with daily cellphone use and cellphone use while driving,” vol. 119, pp. 149–154, 2018, doi: 10.1016/j.aap.2018.07.007.

# So what can be done about it?
I am glad you have asked! One solution is to create a device that can detect drivers on their phones while driving to minimize distracted driving! This is where our project comes in. If this project sees you driving with your phone in your hand, you've been, wait for it, Caught Phone-Handed! (Hence our project title, Caught You Phone-Handed 🙃)

# What is this project about?
This project is called Caught You Phone-Handed!  As the name suggests, our project aims to detect drivers on their phones while driving in order to enforce safe driving.

The basic idea is this device will use video processing via object detection on live video input to catch people using their hand-held phones while driving.  The camera will take the picture of the person on their phone and their number plate if they are caught using their phone while driving. (The camera will not take any picture for the stationary cars)

# What does this project look like?
Simply put, this project takes in live video input.  If our project detects the driver in question is on their phone, then a yellow box appears around the driver **and** their phone.  Otherwise, if there is no phone, nothing appears and the driver is safe.

Still don't see it?  I think it is best by showing you our test results!

[![Caught you phone-handed test results!](https://res.cloudinary.com/marcomontalbano/image/upload/v1618431182/video_to_markdown/images/vimeo--535723214-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://vimeo.com/535723214/settings "Caught you phone-handed test results!")

# Want to learn the nitty gritty details about this project?
Check out our Adobe Spark page for a more comprehensive description!
https://spark.adobe.com/page/rNh1NAZyYFG9T/

# Credits
Team Asianeering would like to thank our Professor Ahmet Enis Cetin for being our project mentor and for helping us make this project become reality!

We would also like to thank professors Renata Revelo and Matthew Alonso for helping us (and other teams) prepare for this Spring 2021 Expo event.

The team also says a big thank you to the following people who made the software we used open-sourced:
* Darren for labelImg that allowed us to annotate/label our images to help train our detection model (https://github.com/tzutalin/labelImg)
* Due to GitHub's limitations to pushing large files to a forked repo, a new repo had to be made.  So this project was "forked" from his repo (https://github.com/nicknochnack/RealTimeObjectDetection).  We thank Nicholas profoundly for providing the code and tutorials that helped us make this project possible!