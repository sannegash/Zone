#from zeroconf import ZeroconfServiceTypes
#print('\n'.join(ZeroconfServiceTypes.find()))

from zeroconf import Zeroconf, ServiceBrowser, ServiceInfo

class Listener: 
  def remove_service(self, zeroconf, type, name):
    print(f"Service removed: {name}")

  def add_service(self, zeroconf, type, name, info):
    print(f"Service discoverd: {name}")
    print(f"Service info: {info}")

    print(f"Address:  {info.addresses[0]}")
    print(f"Port: {info.port}")
  def update_service(self, zeroconf, type, name, info):
    pass
zeroconf = Zeroconf()

service_type = "__http._tcp.local."

listener = Listener()
browser = ServiceBrowser(zeroconf, "_services._dns-sd._udp.local.", listener)

try: 
  input("Press Enter to exit...\n\n")
finally:
  zeroconf.close()

