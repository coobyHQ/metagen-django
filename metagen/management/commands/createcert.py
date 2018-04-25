import os
from django.core.management.base import BaseCommand
from metagen.app_settings import app_settings as settings


class Command(BaseCommand):
    help = 'Create a self-signed x509 certificate for METAGEN.'

    def handle(self, * args, ** options):
        print("METAGEN private key setting: %s" % settings.SP_PUBLIC_CERT_PATH)
        print("METAGEN public cert setting: %s" % settings.SP_PRIVATE_KEY_PATH)

        if os.path.isfile(settings.SP_PUBLIC_CERT_PATH) \
                and os.path.isfile(settings.SP_PRIVATE_KEY_PATH):

            print("\nAn x509 certificate for METAGEN settings already exists!!!\n")
            os.system("openssl x509 -text -noout -in %s" % settings.SP_PUBLIC_CERT_PATH)
            answer = input("\nOverwrite this certificate with a new one? ")
            if answer.upper() not in ('Y', 'YES'):
                return
            print()

        cmd = 'openssl req -new -newkey rsa:1024 -days 3650 -nodes -x509 -keyout %s -out %s'
        os.system(cmd % (settings.SP_PRIVATE_KEY_PATH, settings.SP_PUBLIC_CERT_PATH))

        print("\n\nInstalled x509 certificate for METAGEN settings:\n")
        os.system("openssl x509 -text -noout -in %s" % settings.SP_PUBLIC_CERT_PATH)
