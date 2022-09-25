import qi
from code.Gestures import RuleBasedMovements as rb

if __name__ == "__main__":

	nao_ip = "127.0.0.1"
	simulation = False
	if nao_ip=="127.0.0.1":
		simulation = True

	# Start app session
	connection_url = "tcp://" + nao_ip + ":9559"
	app = qi.Application(["PepperGestures", "--qi-url=" + connection_url])
	app.start()
	session = app.session
	motion = session.service("ALMotion")
	memory = session.service("ALMemory")
	aup = session.service("ALAudioPlayer")
	motion.wakeUp()

	# posture = rb.BabyMotion()
	# posture = rb.monster()
	# posture = rb.AgoMotion()
	# posture = rb.BegMotion()
	# posture = rb.CarefulMotion()
	posture = rb.BigAgMotion()

	motion.angleInterpolation(posture[0], posture[1], posture[2], True, _async=False)