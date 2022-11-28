# Schleppe UPS Consumption

Pulls UPS power draw over ModBus and logs to ElasticSearch.

## Install
Download repo:

```bash
git clone https://github.com/kevinmidboe/schleppeUPSConsumption
cd schleppeUPSConsumption
```

Install python requirements:

```bash
pip3 install -r requirements.txt
```

## Configure
Create copy of config and edit follow values:

```bash
cp config.yaml.default config.yaml
```

```yaml
logger:
  name: schleppe_ups_consumption
  ch_level: INFO

modbus:
  host:
  port:

elastic:
  host:
  port:
  ssl:
  apiKey:
```

## Run

```bash
python3 apcWatts.py
```
