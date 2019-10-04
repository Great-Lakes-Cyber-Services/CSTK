from django.core.management.utils import get_random_secret_key

with open('CyberSecurityToolKit/.env', 'w+') as env_file:
	env_lines = ['DEBUG=on\n', 'SECRET_KEY=' + get_random_secret_key() + '\n']
	env_file.writelines(env_lines)