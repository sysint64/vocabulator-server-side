import os

from django.conf import settings
from django.core.management.base import BaseCommand
from grpc_tools import protoc


class Command(BaseCommand):
    help = "Generate python files from proto"

    def handle(self, *args, **options):
        for proto in settings.PROTOS:
            proto_name, proto_dest = proto
            proto_dest = os.path.join(settings.BASE_DIR, proto_dest, "")
            proto_src = os.path.join(settings.PROTO_ROOT, proto_name)

            protoc.main((
                "",
                f"-I{settings.PROTO_ROOT}",
                f"--python_out={proto_dest}",
                f"--grpc_python_out={proto_dest}",
                f"{proto_src}",
            ))

            self.stdout.write(self.style.SUCCESS(f"Successfully generated {proto_src} to {proto_dest}"))
