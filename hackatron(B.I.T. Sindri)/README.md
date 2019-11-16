Group namee---CODEON<br />
Team Members-<br />
Prakhar Shrivastava (8987608438)<br />
Shantanu Shubham (7209602442)<br />
Deepak Kumar<br />
Shubham Jha<br />
Roshan Kumar Singh<br />
PROBLEM STATEMENT-Conversion of Speech to text and search within the input for a given key and return its time stamp.<br />
Approach-The approach we have used is to create overlapping samples of the input and scan through the input for the key value using google API to give approximate range of the existence of key values.<br />
<br />
SOLUTION APPROACH:<br />
As our input contains an audio that needs to be searched, and a video where the audio needs to be searched,we need to convert all the input to a single format(text).We convert the video to audio(wav) and then the wav. is converted to a stream of strings that's the transcript of the video.Also the input as said by the user is taken in and converted to text format for ease of searching and processing.<br />As time stamp is required,we slice up the entire audio file into small overlapping chunks of 5 seconds each so each chunk and searching of the key is performed on these chunks.(Size of the chunks can be changed based on how much error margin that can be allowed by the developer.Higher the chunk size lesser the space complexity but greater the error margin.smaller the chunk,greater the accuracy but higher the space consumption.)Chunk size can be modified based on the length of the audio input by the user.<br />
Assumptions:<br />
--The audio to text API has low latency<br />
--The audio input size is less than 5 seconds(according to our work)<br />
FILE DESCRIPTION:<br />
finding text in a video.ipynb--A python notebook to incorporate all the steps required in the process of searching and taking inputs from system and user.this is the MAIN file.<br />
audio_to_text.py--A python file to create a transcript of any audio given to it.<br />
Speech_to_text.py--A python file to create a transcript of user input audio.<br />
YouTube.mp4-sample input<br />

