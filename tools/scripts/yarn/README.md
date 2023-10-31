```bash
{
    "state": "<preloaded, to_be_preloaded, not_loaded, tested, failed>",
    "release": "2023",
    "release_version": "0.0.1",
    "vm_type": "<ova, bin>",
    "pool": "<eng, pipeline>",
    "leases": 0, 1, #(TODO ... (+n))
    "lease_end_time": 1234567890, # (unix time)
}
```


```bash
#data_yarn.json
{
  "$ENV_NAME": {
    "args": {"": ""},
    "lease_end_time": $unixtime,
    "leased": 0,
    "pool": "$pool",
    "release": "$release",
    "release_version": "$release_version",
    "state": "$state",
    "type": "$type"
  }
}
