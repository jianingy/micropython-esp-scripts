# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import sys
import machine
print("mcu: starting boot procedure ...")
print("mcu: boot version = 0.1.0")
print("mcu: python version = %s" % sys.version)
print("mcu: core freq = %s)" % machine.freq())

from machine import Timer
import gc
import network
import utime
import webrepl

def connect_wifi():
    sta = network.WLAN(network.STA_IF)
    if sta.isconnected():
        return
    print("wifi: activate wifi station mode ...")
    sta.active(True)
    wifi_ssid, wifi_secret = WIFI_SSID, WIFI_SECRET
    sta.connect(wifi_ssid, wifi_secret)
    while not sta.isconnected():
        print("wifi: connecting to %s (%s) ..." % (wifi_ssid, wifi_secret))
        utime.sleep_ms(1000)
    print("wifi: connected. ip=%s/%s, gateway=%s, dns=%s" % sta.ifconfig())
    sta = None

print("mcu: starting webrepl ...")
webrepl.start()

try:
    from local_settings import *
    print("mcu: local settings loaded.")
except:
    print("mcu: no local settings found. continue to boot.")

connect_wifi()

print("mcu: calling gc.collect ...")
gc.collect()
