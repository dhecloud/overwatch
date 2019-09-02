# Overwatch

Transmit your training losses and messages to your very own discord server!

This package should never ever halt your training process (except when initializing the class).   
please let me know if it does :cold_sweat: 

## Installation & Requirements

`Python 3.6+`  
No extra packages needed! Just git clone this repository to your project folder

## Usage

1. Create a webhook on a channel on your own discord server and get the `webhook url`, `webhook name`, `channel_id`
2. In `overwatch/config.py`, amend or create a config according to your new `webhook url`, `webhook name`, `channel_id`
3. At the start of your training script,  

```
import overwatch as ow
wc = ow.webhook.WebHookConfig()
wh = ow.webhook.WebHook(wc)
```

There will be an exception called if your webhook details are invalid

4. During training/eval
```
wh.send_payload('your message')
```

As simple as that! :smiley:
 
