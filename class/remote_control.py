

class RemoteControl:
    def __init__(self, status=False, sound=0, channel_list=['fox'], channel='fox'):
        self.status = status
        self.sound = sound
        self.channel_list = channel_list
        self.channel = channel

    def on_off(self):
        self.status = not self.status
        if self.status:
            print('tv acik')
        else:
            print('tv kacik')


remote = RemoteControl()

remote.on_off()

remote.on_off()

