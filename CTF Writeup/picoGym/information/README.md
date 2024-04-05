To do this challenge, you need to download the file from picoCTF.
The challenge description tells you that the information is hidden in the file
I personally downloaded the image to my kali box where I have exiftools installed
If you run exiftool cat.jpg, you get this

![image](https://github.com/CountDraculaDaughter/projects/assets/155210038/15f519d4-daf7-4cd0-bc88-1abd791d6c70)

If you look the License is a bit out of place, so if you plug it into Cyberchef, you get (btw the data is in Base64):

![image](https://github.com/CountDraculaDaughter/projects/assets/155210038/03cd6bc7-5856-4278-8e6a-fe6d192f62bd)
