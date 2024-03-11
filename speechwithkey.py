import azure.cognitiveservices.speech as speechsdk

# Replace with your own values
speech_key = "0adfbb35f1dc40df92669ccae4a9d4d1"
speech_region = "eastus2"
audio_file_path = "YOUR_AUDIO_FILE_PATH"

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
audio_config = speechsdk.AudioConfig(filename=audio_file_path)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

 print("Speak into your microphone.")
result = speech_recognizer.recognize_once_async().get()

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))
         print("Did you set the speech resource key and region values?")
