import pyaudio
import wave
import time

def play_sound(file):
	print "* playing..."
	chunk = 1024
	wf = wave.open(file, 'rb')
	p = pyaudio.PyAudio()

	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
					channels=wf.getnchannels(),
					rate=wf.getframerate(),
					output=True)

	data = wf.readframes(chunk)

	while data != '':
		stream.write(data)
		data = wf.readframes(chunk)

	stream.stop_stream()
	stream.close()

	p.terminate()
	print "* done playing."

def record_sound(file, time):
	form = pyaudio.paInt16
	chunk = 1024
	chans = 2
	r_rate = 44100
	p = pyaudio.PyAudio()

	stream = p.open(format=pyaudio.paInt16,
					channels=chans,
					rate=r_rate,
					input=True,
					frames_per_buffer=chunk)

	print("* recording")

	frames = []

	for i in range(0, int(r_rate / chunk * time)):
		data = stream.read(chunk)
		frames.append(data)

	print("* done recording")

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(file, 'wb')
	wf.setnchannels(chans)
	wf.setsampwidth(p.get_sample_size(form))
	wf.setframerate(r_rate)
	wf.writeframes(b''.join(frames))
	wf.close()

if __name__ == '__main__':
	filename = "C:/Users/dmetge/Desktop/output.wav"
	a_file = "C:/Users/dmetge/Desktop/amy.wav"
	record_sound(filename, 5)
	time.sleep(10)
	play_sound(filename)
