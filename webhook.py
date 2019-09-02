import json
import requests
from .exceptions import *
from .config import *
from .utils import *

class WebHook():
    def __init__(self, config, quiet=True):
        super().__init__()
        self.config = config
        self.quiet = quiet
        self.valid = self.check_webhook_validity()
        
        
    def send_payload(self, payload):
        check = internet_on()
        if not self.quiet:
            print('no internet connection')
            return
        else:
            res = requests.post(webhook.url, data=payload).json()
            print(res)
        

    def check_webhook_validity(self, strict = False):
        internet = internet_on()
        if not internet:
            if not self.quiet: print('no_internet detected.')
            return False
        msg = requests.get(self.config.url).json()
        if 'code' in msg.keys():
            #assuming only error codes returned
            raise InvalidWebHookException()
        else:
            # check name and
            assert('name' and 'channel_id' in msg.keys())
            if strict:
                if msg['name'] != webhook.name or msg['channel_id'] != webhook.channel_id:
                    raise InvalidWebHookParticulars()
            print('webhook validated!')
            return True
    
    
    def send_payload(self, message):
        if not self.valid:
            self.valid = self.check_webhook_validity()
            if self.valid == False:
                if not self.quiet: print('webhook still not validated! no message sent')
                return
        
        internet = internet_on()
        payload = self.create_payload(message)
        if not internet:
            if not self.quiet:
                print('no internet connection')
                return
        else:
            res = requests.post(self.config.url, data=payload)
            if res.status_code < 200 or res.status_code > 300:
                if not self.quiet:
                    print('payload failed for some reason, check response code', res.status_code)
    
    def create_payload(self, message):
        payload = {"content": message, "tts": False}
        return payload
    
if __name__ == '__main__':
    webhook_c = WebHookConfig()
    webhook = WebHook(webhook_c, quiet=False)
    webhook.send_payload('hellloo test estest')
