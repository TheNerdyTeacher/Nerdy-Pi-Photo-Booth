# Nerdy-Pi-Photo-Booth
A Photo Booth to use for school events and parties.

Check my website, TheNerdyTeacher.com for the full post with images and links. 

Over the past week, I've become a bit obsessed with creating a photo booth. I saw this very cool article in Make: Magazine and thought I could do that. Well, it turned out that that I could not do that. For whatever reason, I was having serious trouble getting the code to work and it was becoming a headache. So, I turned to The Google to find a different approach to creating a photo booth. 

Materials:

Raspberry Pi 3
Micro SD card - The larger the GB, the more pics it can hold. 
Monitor - I used the 7" Raspberry Pi Touchscreen, but any screen will do. 
Tactile button
Wire to connect Pi to button
PiCamera

I found some interesting resources and wonderfully helpful people online and they helped me put together a slightly different photo booth. I settled on a great code written by jallwine that was shared on Github. This was a great starting point for me to see what the photo booth could be and I could tweak the code to add different things. Not only did he have amazing code, but he helped me when I got stuck trying to tweak his code. Jallwine is the perfect example of how awesome the Maker community can be. He didn't have to help me with his code that was a few years old, but he did it anyway. 

I added a button line so the photo booth would work with the press of a button. I found a version I could use on Raspberry Pi's website that was helpful. The idea of using stop motion as the trigger for the camera made sense to me, so I dropped that in there. 

I also wanted to add a countdown clock so people know when to expect the picture. I really struggled with this because I was approaching the problem from the wrong angle. I was looking for a code to create a timer, but that was overly complicated. Instead, I used the camera.annotate_text line to create text over the picture. For the text, I used numbers that lasted for one second. That created the timer for me. It worked great!

I didn't use the the next parts in the final code, but I figured out how to use random effects on the pictures so they could be really silly photos. The regular photo is currently in, but I could quickly drop it in. You can find out how to do that on Raspberry Pi's website.

Next, I wanted the pictures uploaded to the Cloud so I could grab the when I wanted and share them with others easily. I found a great code for DropboxUploader on Adafruit. I took the code for something different from a photo booth and was able to spin it into a nice addition to my project. I felt super cool being able to put this together. 

I added a few more lines so that the Camera Preview would say "Ready" when it was ready to take pictures and "Processing" when it was formatting and uploading to Dropbox. 

When I was finally done, I had a full photo booth system that will take 3 pictures, duplicate them side by side, upload them to Dropbox, and start all over again. 

I used the Raspberry Pi 7" touchscreen because it was easy to use everything together. You could use any HDMI connected screen you wanted. It could be cool to connect to a large TV screen at family functions are large events so people can really see the images. 

The final step for me will be to create a case to package everything together so it can easily be moved around from place to place. I have a big red button ordered from Adafruit. I can place that on the box and people can give that a push and have their pics. I was thinking of  simple box that had a dry erase or chalkboard front that would allow people to personalize the booth based on the event. 

Here are some pictures of what I was able to put together.
