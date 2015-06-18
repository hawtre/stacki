# @SI_Copyright@
# @SI_Copyright@

import stack.commands.set.network

class Command(stack.commands.set.network.command):
	"""
	Sets the network address of a network.

        <arg type='string' name='network' optional='0' repeat='0'>
        The name of the network.
	</arg>
	
	<param type='string' name='address' optional='0'>
        Address that the named network should have.
	</param>
	
	<example cmd='set network address ipmi address=192.168.10.0'>
        Sets the "ipmi" network address to 192.168.10.0.
	</example>
	"""
                
        def run(self, params, args):

                (networks, address) = self.fillSetNetworkParams(args, 'address')
                if len(networks) > 1:
                        self.abort('must specify a single network')
			        	
        	for network in networks:
			self.db.execute("""
                        	update subnets set address='%s' where
				subnets.name='%s'
                                """ % (address, network))
