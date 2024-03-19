First step is to either ssh or download the files locally, I decided to do the ssh method
You first need all of the sha256 sums and then do a figurative ctrl+'F' in terminal.
The command that does this is: sha256sum files/* | grep -F '5848768e56185707f76c1d74f34f4e03fb0573ecc1ca7b11238007226654bcda'
The output looks like this 

<img width="347" alt="image" src="https://github.com/CountDraculaDaughter/projects/assets/155210038/ebd5a558-14d3-43cd-a7dc-fdc30cbe39ea">

So then you basically have to run this to get the flag: sh decrypt.sh /files/8eee7195
Which gives you this:

<img width="188" alt="image" src="https://github.com/CountDraculaDaughter/projects/assets/155210038/73a33245-bf79-45e4-9838-2813480486a5">
