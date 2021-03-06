#!/usr/bin/env python

def main():
	try:
		from src import main
		main.start()
		if main.update_after_shutdown: # Updater
			import update, sys, os, gc
			# Update
			update.update()

			# Close log files
			logger = sys.modules["src.main"].logging.getLogger()

			for handler in logger.handlers[:]:
				handler.flush()
				handler.close()
				logger.removeHandler(handler)

	except Exception, err: # Prevent closing
		import traceback
		traceback.print_exc()
		raw_input("-- Error happened, press enter to close --")

	if main.update_after_shutdown: # Updater
		# Restart
		gc.collect() # Garbage collect
		print "Restarting..."
		args = sys.argv[:]
		args.insert(0, sys.executable) 
		if sys.platform == 'win32':
			args = ['"%s"' % arg for arg in args]
		os.execv(sys.executable, args)
		print "Bye."

if __name__ == '__main__':
	main()
