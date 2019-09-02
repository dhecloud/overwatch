# Overwatch

Transmit your training losses and messages to your very own discord server!

This package should never ever halt your training process (please let me know if it does :cold_sweat:)

## Installation & Requirements

`Python 3.6+`  
No extra packages needed! Just git clone this repository to your project folder

## Usage

1. Create a webhook on a channel on your own discord server and get the `webhook url`, `webhook name`, `channel_id`
2. In `overwatch/config.py`, amend or create a config according to your new `webhook url`, `webhook name`, `channel_id`
3. In your training script,  

```
import overwatch as ow
wc = ow.webhook.WebHookConfig()
wh = ow.webhook.WebHook(wc)
wh.send_payload('your message')
```



