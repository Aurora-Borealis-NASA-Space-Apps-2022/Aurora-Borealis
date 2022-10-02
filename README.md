# Aurora-Borealis
Official Submission of Team "Aurora Borealis" for NASA Space Apps Challenge 2022 participating in the challenge "SAVE THE EARTH FROM ANOTHER CARRINGTON EVENT!"





## Introduction
One of the most powerful solar events of the century was the Carrington Event in 1859. Powerful coronal mass ejections struck Earth directly throughout this event. Globally, including close to the equator, observers of the ensuing impacts and glimmering auroras in the night sky were noticed. Long lengths of the common telegraph transmission lines that were affected by this space weather phenomenon developed geomagnetically induced currents that produced enough current for the lines to function without batteries. In other cases, the induced currents even set some telegraph stations on fire. Fortunately, the Carrington Event had a minimal impact on both world safety and the economy because high voltage (HV) electrical power transmission lines weren't in use at the time.

However, such an occurrence would be terrible in the modern world, when almost everything is powered by electricity, computers, and other devices that are connected to the "grid." Large numbers of high energy particles that are ejected during solar storms as solar wind have the potential to harm electrical and electronic infrastructure like power lines and satellites for communication. Since it takes a very long time to get such large power transformers and they are expensive to replace, it is possible that the HV power lines and substations on which we rely could be damaged or rendered inoperable for months or years.

## Problem Statement/Solution
The effects on society could be catastrophic if a significant space weather catastrophe similar to the Carrington Event of 1859 occurred now. The goal of this challenge is to created neural network pipeline that can accurately track changes in the peak solar wind speed and give a head start on the possibility for the next Carrington-like event.



### What problem does it solve?
The issue of delayed transmission in solar flare changes.

### What do people gain?
Quick alert on any solar flare changes.

### Where is the opportunity? 
By speculation, the Carrington event is set to occur in the near future. This is a precautionary step to avoid widespread impact if eventually it happens.


## Idea Description
### How does it work?
- Method - Dataset was gathered every six months for 1 year, specifically 2021.
- Parameters - Magnetic field magnitude (BW[nT]) using "Wind Mission Magnetic Field Dataset".
- Model implementation - By using the parameters, an algorithm is created which predicts the intensity of electric flow. The algorithm uses a classifier that trains the dataset and generates a current voltage spectra.
- Language - Python v3.10.

![graph](https://user-images.githubusercontent.com/68698006/193462892-48b15b48-3d1e-40b5-b3fe-2180ad3541d0.jpeg)
![color](https://user-images.githubusercontent.com/68698006/193462863-9243044e-6b15-4ef4-b01c-3141a33193c7.jpeg)


## Into The Future
### What will your idea change? 
People can prepare in advance or even stay away from instruments that can trigger a reaction when the flare hits the Earth. Also, scientists can provide an anti-flare shield such that during the event, no one will be hurt even if close to conductors.

### What can your solution do for people, the world, and beyond? 
Save the world from unavoidable solar disasters.

## Video 
[*To be a champion, compete; to be a great champion, compete with the best; but to be the greatest champion, compete with yourself*](https://www.youtube.com/watch?v=B_uEVxWl69A&feature=youtu.be)


## Team Members
![team canvas](https://drive.google.com/file/d/1z7IPuBvjmg1Fn4uWV9e4Lgw5dQqW7Rhq/view?usp=sharing)

