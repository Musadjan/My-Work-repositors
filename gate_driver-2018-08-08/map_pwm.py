#!/usr/bin/python
'''
Script to create adc->pmw mapping
'''
def generate_freqs():
	freqs = []
	for x in range (1,256):
		freqs.append(x*392)
	return freqs

def generate_pwm(in_list):
	pwm_pr = []
	for x in range(len(in_list)):
		pwm_pr.append( int( round(4000000.0/in_list[x],0) ) )
	return pwm_pr

def main():
	freq_list = []
	freq_list = generate_freqs()
	pwm_pr = generate_pwm(freq_list)
	print pwm_pr
	print "Length: %d" % (len(pwm_pr))

main()
