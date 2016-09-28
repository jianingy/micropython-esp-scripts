all:
	./webrepl_cli boot.py $(MICROPYTHON_IP):/
	./webrepl_cli local_settings.py $(MICROPYTHON_IP):/
	./webrepl_cli main.py $(MICROPYTHON_IP):/
