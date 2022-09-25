echo "Introduce story name: "

read storyname

echo "Calling IMB Watson NLP..."

/usr/bin/python3 Download_watson_info/ibm_watson_nlp.py --story $storyname

echo "IBM Watson NLP completed."

echo "Calling IBM Watson TTS..."

/usr/bin/python3 Download_watson_info/ibm_watson_tts.py --story $storyname

echo "IBM Watson TTS completed."

echo "Starting Watson ASR..."

/usr/bin/python3 Download_watson_info/ibm_watson_asr.py --story $storyname

echo "IBM Watson ASR completed."

echo "Done"
