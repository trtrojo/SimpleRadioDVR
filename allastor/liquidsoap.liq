#!/usr/bin/liquidsoap -v

# Loop the source to continuously play it
src_stream_offline = mksafe(
    rewrite_metadata(
        [("title", "Radio Offline")], 
        single("/workspace/polycom_hold.wav")
        ))

input_channel1 = input.harbor("radio_input", port = 8001, user="radio", password = "channel1password")
input_channel2 = input.harbor("radio_input", port = 8002, user="radio", password = "channel2password")
input_channel3 = input.harbor("radio_input", port = 8003, user="radio", password = "channel3password")

radio_channel1 = fallback(track_sensitive=false, [input_channel1, src_stream_offline])
radio_channel2 = fallback(track_sensitive=false, [input_channel2, src_stream_offline])
radio_channel3 = fallback(track_sensitive=false, [input_channel3, src_stream_offline])


# Channel One
output.icecast(%vorbis,
  host = "icecast2",
  port = 8000,
  password = "1bHwVPZlPLIUlt",
  mount = "/channel1.ogg",
  radio_channel1)

# Channel Two
output.icecast(%vorbis,
  host = "icecast2",
  port = 8000,
  password = "1bHwVPZlPLIUlt",
  mount = "/channel2.ogg",
  radio_channel2)

# Channel Two
output.icecast(%vorbis,
  host = "icecast2",
  port = 8000,
  password = "1bHwVPZlPLIUlt",
  mount = "/channel3.ogg",
  radio_channel3)
