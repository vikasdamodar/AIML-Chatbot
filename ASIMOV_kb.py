# Manages the knowledge base used to think.
import aiml

kernel = aiml.Kernel()
# kernel.learn("/home/vikas/Py3kAiml-master/std-startup.xml")
kernel.learn("corpus/bot-startup.xml")
kernel.respond("load aiml b")

while True:
    print(kernel.respond(str(input("> "))))
    # print(kernel.respond(raw_input("Enter your message >> ")))
