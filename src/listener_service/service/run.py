import argparse
from nameko.cli.run import main
AMQP_URI = 'pyamqp://guest:guest@172.17.0.5'
parser = argparse.ArgumentParser()
parser.add_argument(
    'services', nargs='+',
    metavar='module[:service class]',
    help='python path to one or more service classes to run')
parser.add_argument(
    '--config', default='',
    help='The YAML configuration file')
parser.add_argument(
    '--broker', default='pyamqp://guest:guest@localhost',
    help='RabbitMQ broker url')
parser.add_argument(
    '--backdoor-port', type=int,
    help='Specify a port number to host a backdoor, which can be'
         ' connected to for an interactive interpreter within the running'
         ' service process using `nameko backdoor`.')

args = parser.parse_args(["--broker", AMQP_URI, "service.service:ListenerService"])
main(args)
