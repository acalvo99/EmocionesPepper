echo "$PWD"
echo "Introduce story name: "

read storyname

echo "Calling IBM Watson TTS..."

/usr/bin/python3 Download_watson_info/ibm_watson_tts.py --story $storyname

echo "IBM Watson TTS completed."
echo "Starting Watson ASR..."
/usr/bin/python3 Download_watson_info/ibm_watson_asr.py --story $storyname
echo "IBM Watson ASR completed."
echo "Done"