import sys
import io

def before_all(context):
    context.stdout_mock = io.StringIO()
    sys.stdout = context.stdout_mock

def after_all(context):
    sys.stdout = sys.__stdout__