import sys
import io

def before_all(context):
    context.outFile = open('./tests/features/output.txt', 'w')

def after_all(context):
    context.outFile.close()