# remote_configurator

Send or receive configurations remotely. The configurations must be passed as a python dictionary (an error is raised otherwise).

remote_configurator(host, port, buffer_size=1024)

Inputs:

host: hostname or its IP address.
port: Port to be used (either for sending or receiving data).
buffer_size: Size of the buffer (data). Smaller means faster, perhaps, if the data to be sent is bigger than the buffer_size only the first buffer_size characters will be used.

Class methods:

remote_configurator.listen()
wait till some data is received, then return it.

remote_configurator.send(conf)
Send data to the specified host, conf must be a dictionary or a TypeError will be raised.



